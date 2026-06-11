from services.llm_service import run_agent_prompt

from langchain_core.prompts import PromptTemplate

from tools.security_tool import (
    generate_security_plan
)

import json
from utils.parser import safe_json_parse


def get_dynamic_security_plan(

    event_type="",
    guests=0

):

    event_type = str(
        event_type
    ).lower()

    guests = int(guests)

    # =========================
    # BASE SECURITY LEVEL
    # =========================

    if guests >= 3000:

        base_level = "Critical"

        guards = 80

    elif guests >= 1500:

        base_level = "High"

        guards = 45

    elif guests >= 500:

        base_level = "Medium"

        guards = 20

    else:

        base_level = "Basic"

        guards = 8

    # =========================
    # GAMING EVENT
    # =========================

    if (

        "gaming" in event_type or
        "esports" in event_type or
        "tournament" in event_type

    ):

        return {

            "security_level":
                "High",

            "guards_required":
                max(guards, 30),

            "emergency_services":
                "Medical Booth + Emergency Response Team",

            "crowd_management":
                "Arena crowd barricades and player-zone isolation",

            "surveillance":
                "AI CCTV monitoring enabled",

            "entry_control":
                "RFID gaming access verification",

            "risk_alert":
                "High crowd excitement and equipment theft risk"
        }

    # =========================
    # FASHION EVENT
    # =========================

    elif (

        "fashion" in event_type or
        "runway" in event_type

    ):

        return {

            "security_level":
                "Premium",

            "guards_required":
                max(guards, 25),

            "emergency_services":
                "VIP medical support",

            "crowd_management":
                "VIP runway access restriction",

            "surveillance":
                "Backstage security monitoring",

            "entry_control":
                "VIP QR verification",

            "risk_alert":
                "Celebrity crowd control required"
        }

    # =========================
    # CONFERENCE / EXPO
    # =========================

    elif (

        "conference" in event_type or
        "expo" in event_type or
        "corporate" in event_type

    ):

        return {

            "security_level":
                base_level,

            "guards_required":
                max(guards, 18),

            "emergency_services":
                "Corporate emergency response desk",

            "crowd_management":
                "Smart registration queue handling",

            "surveillance":
                "Hall-wide CCTV coverage",

            "entry_control":
                "Digital badge access system",

            "risk_alert":
                "VIP business security monitoring"
        }

    # =========================
    # FESTIVAL / CONCERT
    # =========================

    elif (

        "festival" in event_type or
        "concert" in event_type or
        "music" in event_type

    ):

        return {

            "security_level":
                "Critical",

            "guards_required":
                max(guards, 60),

            "emergency_services":
                "Ambulance + Fire Safety + Emergency Crew",

            "crowd_management":
                "Large-scale barricading and emergency exits",

            "surveillance":
                "Drone and AI surveillance enabled",

            "entry_control":
                "Multi-layer ticket verification",

            "risk_alert":
                "Extreme crowd surge possibility"
        }

    # =========================
    # HACKATHON
    # =========================

    elif (

        "hackathon" in event_type or
        "coding" in event_type

    ):

        return {

            "security_level":
                "Medium",

            "guards_required":
                max(guards, 15),

            "emergency_services":
                "24/7 technical support and medical assistance",

            "crowd_management":
                "Device and workstation monitoring",

            "surveillance":
                "Server room security enabled",

            "entry_control":
                "Developer access authentication",

            "risk_alert":
                "Cybersecurity and device theft monitoring"
        }

    # =========================
    # PRODUCT LAUNCH
    # =========================

    elif (

        "launch" in event_type or
        "product" in event_type

    ):

        return {

            "security_level":
                "High",

            "guards_required":
                max(guards, 22),

            "emergency_services":
                "Media emergency response support",

            "crowd_management":
                "Stage and media-zone barricading",

            "surveillance":
                "Product showcase protection enabled",

            "entry_control":
                "Press and VIP verification",

            "risk_alert":
                "High-value prototype protection required"
        }

    # =========================
    # DEFAULT
    # =========================

    return {

        "security_level":
            base_level,

        "guards_required":
            guards,

        "emergency_services":
            "Basic Ambulance Support",

        "crowd_management":
            "Standard crowd control",

        "surveillance":
            "Standard CCTV monitoring",

        "entry_control":
            "Guest verification system",

        "risk_alert":
            "Normal operational monitoring"
    }


def security_agent(data):

    if "execution_flow" not in data:

        data["execution_flow"] = []

    data["execution_flow"].append(
        "security_agent"
    )

    # =========================
    # INPUTS
    # =========================

    event_type = data.get(
        "event_type",
        ""
    )

    guests = int(
        data.get(
            "guests",
            0
        )
    )
    shared_memory = data.get(
        "shared_memory",
        {}
    )


    venue_complexity = shared_memory.get(
          "venue_complexity",
           "standard"
    )

    needs_security = shared_memory.get(
            "needs_security",
            False
    )

    crowd_density = shared_memory.get(
            "crowd_density",
             "low"
    )

    # =========================
    # TOOL RESULT
    # =========================

    tool_result = generate_security_plan(
        guests=guests,
        event_type=event_type
    )

    # =========================
    # SMART SECURITY PLAN
    # =========================

    smart_security = (
        get_dynamic_security_plan(
            event_type,
            guests
        )
    )
    if needs_security:

        smart_security[
            "guards_required"
        ] += 5

    if venue_complexity == "high":

        smart_security[
            "guards_required"
        ] += 10

    elif venue_complexity == "extreme":

        smart_security[
            "guards_required"
        ] += 20

    if crowd_density == "high":

        smart_security[
            "guards_required"
        ] += 10

    elif crowd_density == "extreme":

         smart_security[
            "guards_required"
        ] += 25

    # =========================
    # PROMPT
    # =========================

    prompt = PromptTemplate(

        input_variables=[

            "tool_result",
            "smart_security",
            "event_type",
            "guests"
        ],

        template="""
You are an AI event security planner.

Return ONLY valid JSON.

Event Type:
{event_type}

Guests:
{guests}

Tool Result:
{tool_result}

Smart Security:
{smart_security}

Improve the security plan intelligently.

Return format:

{{
  "security_level": "",
  "guards_required": 0,
  "emergency_services": "",
  "crowd_management": "",
  "surveillance": "",
  "entry_control": "",
  "risk_alert": ""
}}
"""
    )

    try:

        result = run_agent_prompt(

            prompt,

            {

                "tool_result":
                    str(tool_result),

                "smart_security":
                    str(smart_security),

                "event_type":
                    event_type,

                "guests":
                    guests
            }
        )

        result = result.replace(
            "```json",
            ""
        )

        result = result.replace(
            "```",
            ""
        )

        result = result.strip()

        parsed = safe_json_parse(result)

        parsed["guards_required"] = int(
            parsed.get(
                "guards_required",
                smart_security[
                    "guards_required"
                ]
            ) or 0
        )

        parsed["security_level"] = parsed.get(

            "security_level",

            smart_security[
                "security_level"
            ]
        )

        parsed["emergency_services"] = parsed.get(

            "emergency_services",

            smart_security[
                "emergency_services"
            ]
        )

        parsed["crowd_management"] = parsed.get(

            "crowd_management",

            smart_security[
                "crowd_management"
            ]
        )

        parsed["surveillance"] = parsed.get(

            "surveillance",

            smart_security[
                "surveillance"
            ]
        )

        parsed["entry_control"] = parsed.get(

            "entry_control",

            smart_security[
                "entry_control"
            ]
        )

        parsed["risk_alert"] = parsed.get(

            "risk_alert",

            smart_security[
                "risk_alert"
            ]
        )

        parsed[
            "tool_recommendation"
        ] = tool_result

        data["security"] = parsed

    except Exception as e:

        smart_security["error"] = str(e)

        smart_security[
            "tool_recommendation"
        ] = tool_result

        data["security"] = smart_security

    return data