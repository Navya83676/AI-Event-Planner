from fastapi.responses import FileResponse

from utils.pdf_generator import generate_pdf

import tempfile


from fastapi import APIRouter
from fastapi import APIRouter, Body

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
        result["theme"] = getattr(event, "theme", "")
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
                getattr(
                    event,
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
        print("=" * 50)
        print("FRONTEND DATA")
        print(frontend_data)
        print("=" * 50)

        event = db.query(Event).filter(
            Event.id == event_id
        ).first()

        if not event:

            return {

                "success": False,

                "message": "Event not found"
            }

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        )

        temp_file.close()

        pdf_path = temp_file.name

        pdf_data = dict(
            event.workflow_data or {}
        )

        # Merge frontend data

        pdf_data.update(
            frontend_data
        )

        pdf_data["customer_name"] = event.customer_name
        pdf_data["event_name"] = event.event_name
        pdf_data["event_type"] = event.event_type
        pdf_data["event_duration"] = event.event_duration
        pdf_data["guests"] = event.guests
        pdf_data["budget"] = event.budget
        pdf_data["event_date"] = str(event.event_date)
        pdf_data["venue"] = event.workflow_data.get(
            "venue",
            {
                "venue_name": event.venue
            }
        )
        pdf_data["theme"] = event.theme
        pdf_data["requirements"] = event.requirements

        pdf_data["status"] = event.status

        pdf_data["created_at"] = str(
            event.created_at
        )
        pdf_data["event_id"] = event.id

        pdf_data["plannerName"] = "Navya"
        pdf_data["plannerEmail"] = "navya@gmail.com"
        pdf_data["plannerRole"] = "Event Planner"


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

        

        generate_pdf(
            pdf_data,
            pdf_path
        )

        return FileResponse(
            path=pdf_path,
            media_type="application/pdf",
            filename=f"{event.event_name}_Report.pdf"
        )

    finally:

        db.close()
   