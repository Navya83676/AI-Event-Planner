from fastapi.responses import FileResponse

from utils.pdf_generator import generate_pdf

import tempfile

import os


from fastapi import (
    APIRouter,
    Body
)

from graph.workflow import build_workflow

from models.event_model import (
    EventRequest,
    Event
)

from database import SessionLocal

import json

router = APIRouter()

# =========================
# GENERATE EVENT
# =========================

@router.post("/generate")
def generate_event(event: EventRequest):

    print("=" * 50)
    print("EVENT TYPE:", event.event_type)
    print("EVENT DURATION:", event.event_duration)
    print("REQUIREMENTS:", event.requirements)

    print("LOCATION:", getattr(event, "location", None))
    print("VENUE:", event.venue)

    print("=" * 50)

    db = SessionLocal()

    try:

        # =========================
        # BUILD WORKFLOW
        # =========================

        workflow = build_workflow()

        # =========================
        # INITIAL STATE
        # =========================

        initial_state = {

            "customer_name":
                event.customer_name,

            "event_name":
                event.event_name,

            "event_type":
                event.event_type,

            "event_duration":
                event.event_duration,

            "theme":
                getattr(
                    event,
                    "theme",
                    ""
                ),

            "guests":
                event.guests,

            "budget":
                event.budget,

            "event_date":
                event.event_date,

            "location":
                getattr(
                    event,
                    "location",
                    event.venue
                ),

            "venue":
                event.venue,

            "requirements":
                event.requirements
        }

        # =========================
        # RUN AI WORKFLOW
        # =========================

        result = workflow.invoke(
            initial_state
        )

        print("\n===== INITIAL STATE =====")
        print(json.dumps(initial_state, indent=2, default=str))
        print("=========================\n")

        print("VENUE AFTER WORKFLOW")
        print(result.get("venue"))


        result["customer_name"] = event.customer_name
        result["event_name"] = event.event_name
        result["event_type"] = event.event_type
        result["event_duration"] = event.event_duration
        result["guests"] = event.guests
        result["budget"] = event.budget
        result["event_date"] = str(event.event_date)
        if not isinstance(result.get("venue"), dict):

            result["venue"] = {
                "venue_name": event.venue,
                "capacity": 0,
                "estimated_cost": 0
            }
        result["theme"] = result.get(
            "theme",
            result.get(
                "recommended_theme",
                ""
            )
        )
        result["requirements"] = event.requirements

        result["readiness_score"] = 95

        result["location"] = getattr(
            event,
            "location",
            event.venue
        )

        # =========================
        # VALIDATE RESULT
        # =========================

        if not isinstance(
            result,
            dict
        ):

            raise ValueError(
                "Workflow returned invalid result"
            )

        # =========================
        # SAFE FALLBACKS
        # =========================

        if "execution_flow" not in result:

            result[
                "execution_flow"
            ] = []

        result.setdefault(
            "event_id",
            None
        )

        # =========================
        # DEBUG LOGGING
        # =========================

        print("\n====================")
        print("FINAL WORKFLOW RESULT")
        print("====================")

        print(

            json.dumps(

                result,

                indent=2,

                default=str
            )
        )

        print("====================\n")

        # =========================
        # SAVE EVENT TO DATABASE
        # =========================

        new_event = Event(

            customer_name=
                event.customer_name,

            event_name=
                event.event_name,

            event_type=
                event.event_type,

            event_duration=
                event.event_duration,

            guests=
                event.guests,

            budget=
                event.budget,

            event_date=
                event.event_date,

            venue=
                event.venue,
            theme=
                result.get(
                    "theme",
                    ""
                ),

            requirements=
                event.requirements,

            workflow_data=
                result
        )

        db.add(
            new_event
        )

        db.commit()

        db.refresh(
            new_event
        )

        # =========================
        # UPDATE EVENT ID
        # =========================

        result["event_id"] = (
            new_event.id
        )

        # =========================
        # SUCCESS RESPONSE
        # =========================

        return {

            "success": True,

            "message":
                "Event plan generated successfully",

            "event_id":
                new_event.id,

            "data":
                result
        }

    except Exception as e:

        db.rollback()

        return {

            "success": False,

            "error":
                str(e)
        }

    finally:

        db.close()

# =========================
# GET ALL EVENTS
# =========================

@router.get("/events")
def get_events():

    db = SessionLocal()

    try:

        events = db.query(
            Event
        ).all()

        formatted_events = []

        for event in events:

            formatted_events.append({

                "id":
                    event.id,

                "customer_name":
                    event.customer_name,

                "event_name":
                    event.event_name,

                "event_type":
                    event.event_type,

                "event_duration":
                    event.event_duration,

                "guests":
                    event.guests,

                "budget":
                    event.budget,

                "event_date":
                    event.event_date,

                "venue":
                    event.venue,
                "theme":
                    event.theme,

                "requirements":
                    event.requirements,

                "status":
                    event.status,

                "created_at":
                    event.created_at
            })

        return {

            "success": True,

            "total_events":
                len(formatted_events),

            "data":
                formatted_events
        }

    except Exception as e:

        return {

            "success": False,

            "error":
                str(e)
        }

    finally:

        db.close()

# =========================
# GET SINGLE EVENT
# =========================

@router.get("/events/{event_id}")
def get_single_event(
    event_id: int
):

    db = SessionLocal()

    try:

        event = db.query(
            Event
        ).filter(
            Event.id == event_id
        ).first()

        if not event:

            return {

                "success": False,

                "message":
                    "Event not found"
            }

        return {

            "success": True,

            "data": {

                "id":
                    event.id,

                "customer_name":
                    event.customer_name,

                "event_name":
                    event.event_name,

                "event_type":
                    event.event_type,

                "event_duration":
                    event.event_duration,

                "guests":
                    event.guests,

                "budget":
                    event.budget,

                "event_date":
                    event.event_date,

                "venue":
                    event.venue,
                "theme":
                    event.theme,

                "requirements":
                    event.requirements,

                "status":
                    event.status,

                "workflow_data":
                    event.workflow_data,

                "created_at":
                    event.created_at
            }
        }

    except Exception as e:

        return {

            "success": False,

            "error":
                str(e)
        }

    finally:

        db.close()

# =========================
# DELETE EVENT
# =========================

@router.delete("/events/{event_id}")
def delete_event(
    event_id: int
):

    db = SessionLocal()

    try:

        event = db.query(
            Event
        ).filter(
            Event.id == event_id
        ).first()

        if not event:

            return {

                "success": False,

                "message":
                    "Event not found"
            }

        db.delete(
            event
        )

        db.commit()

        return {

            "success": True,

            "message":
                f"Event {event_id} deleted successfully"
        }

    except Exception as e:

        db.rollback()

        return {

            "success": False,

            "error":
                str(e)
        }
    finally:
         db.close()
    



@router.post("/events/{event_id}/report")
def download_report(
    event_id: int,
    frontend_data: dict = Body(...)
):

    db = SessionLocal()

    try:


        print("FRONTEND DATA")
        print(frontend_data)
        print("=" * 50)
        print("=" * 50)
        print("FOOD")
        print(frontend_data.get("food"))

        print("=" * 50)
        print("DECORATION")
        print(frontend_data.get("decoration"))

        print("=" * 50)
        print("ENTERTAINMENT")
        print(frontend_data.get("entertainment"))

        print("=" * 50)
        print("SECURITY")
        print(frontend_data.get("security"))

        print("=" * 50)

        event = db.query(Event).filter(
            Event.id == event_id
        ).first()

        print("EVENT ID REQUESTED:", event_id)

        if not event:
            return {
                "success": False,
                "message": "Event not found"
            }

        print("DB EVENT NAME:", event.event_name)
        print("DB EVENT TYPE:", event.event_type)

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        )

        temp_file.close()

        pdf_path = temp_file.name

       # pdf_data = frontend_data.copy()

        #workflow_data = event.workflow_data or {}

        #for key, value in workflow_data.items():
           # if key not in pdf_data or not pdf_data.get(key):
                #pdf_data[key] = value
        pdf_data = frontend_data.copy()

        print("=" * 80)
        print("USING ONLY FRONTEND DATA")
        print("=" * 80)


        print("=" * 100)
        print("EVENT ID:", event_id)

        print("EVENT NAME:")
        print(
            pdf_data.get("eventName")
            or pdf_data.get("event_name")
        )

        print("TIMELINE:")
        print(pdf_data.get("timeline"))

        print("VENDORS:")
        print(pdf_data.get("vendors"))

        print("BUDGET:")
        print(
            pdf_data.get("budgetPlan")
            or pdf_data.get("budget_plan")
        )

        print("=" * 100)

        pdf_data["customer_name"] = (
            frontend_data.get("customerName")
            or frontend_data.get("customer_name")
            or event.customer_name
        )

        pdf_data["event_name"] = (
            frontend_data.get("eventName")
            or frontend_data.get("event_name")
            or event.event_name
        )

        pdf_data["event_type"] = (
            frontend_data.get("eventType")
            or frontend_data.get("event_type")
            or event.event_type
        )

        pdf_data["event_duration"] = frontend_data.get(
            "duration",
            event.event_duration
        )

        pdf_data["guests"] = frontend_data.get(
            "guests",
            event.guests
        )

        pdf_data["budget"] = frontend_data.get(
            "budget",
            event.budget
        )

        pdf_data["event_date"] = (
            frontend_data.get("eventDate")
            or frontend_data.get("event_date")
            or str(event.event_date)
        )
        pdf_data["venue"] = (
            frontend_data.get("venue")
            or {
                "venue_name": event.venue
            }
        )

        pdf_data["theme"] = (
            frontend_data.get("theme")
            or event.theme
        )

        pdf_data["requirements"] = frontend_data.get(
            "requirements",
            event.requirements
        )

        pdf_data["status"] = event.status

        pdf_data["created_at"] = str(
            event.created_at
        )
        pdf_data["event_id"] = event.id

        pdf_data["plannerName"] = "Navya"
        pdf_data["plannerEmail"] = "navya@gmail.com"
        pdf_data["plannerRole"] = "Event Planner"
        print("=" * 50)

        print(
            "PDF IMAGE:"
        )

        print(
            pdf_data.get("image")
        )

        print("=" * 50)

        
        print("=" * 80)
        print("FINAL PDF DATA")
        print(pdf_data)
        print("=" * 80)

        print("=" * 80)
        print("FINAL PDF DATA")
        print(pdf_data)

        print("=" * 80)
        print("TIMELINE")
        print(pdf_data.get("timeline"))

        print("=" * 80)
        print("VENDORS")
        print(pdf_data.get("vendors"))

        print("=" * 80)
        print("BUDGET PLAN")
        print(
            pdf_data.get("budgetPlan")
            or pdf_data.get("budget_plan")
        )

        print("=" * 80)

        if "budgetPlan" in pdf_data:
            pdf_data["budget_plan"] = pdf_data["budgetPlan"]

        if "budget_plan" in pdf_data:
            pdf_data["budgetPlan"] = pdf_data["budget_plan"]

        try:
            print("STARTING PDF GENERATION")

            generate_pdf(
                pdf_data,
                pdf_path
            )

            print("PDF GENERATED SUCCESSFULLY")

        except Exception as e:
            print("PDF GENERATION FAILED")
            print(str(e))
            raise e

        print("=" * 80)
        print("PDF GENERATED")
        print("PDF PATH:", pdf_path)
        print("PDF EXISTS:", os.path.exists(pdf_path))

        if os.path.exists(pdf_path):
            print("PDF SIZE:", os.path.getsize(pdf_path))

        with open(pdf_path, "rb") as f:
            print("FIRST 20 BYTES:", f.read(20))

        print("=" * 80)

        return FileResponse(
            path=pdf_path,
            media_type="application/pdf",
            filename=f"{event.event_name}_Report.pdf"
        )

    finally:

        db.close()
   