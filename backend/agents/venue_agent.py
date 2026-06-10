from services.llm_service import run_agent_prompt

from langchain_core.prompts import PromptTemplate

from tools.venue_tool import (
    get_venue_recommendation
)

import json


def venue_agent(data):

    if "execution_flow" not in data:

        data["execution_flow"] = []

    data["execution_flow"].append(
        "venue_agent"
    )

    classification = data.get(
        "classification",
        {}
    )

    tool_result = get_venue_recommendation(

        location=data.get(
            "location"
        ),

        guests=data.get(
            "guests"
        ),

        budget=data.get(
            "budget"
        ),
        event_type=data.get(
            "event_type",
            ""
        )
    )

    print("\n===== VENUE TOOL RESULT =====")
    print(tool_result)
    print("============================\n")

    if "tool_outputs" not in data:

        data["tool_outputs"] = {}

    data["tool_outputs"][
        "venue_tool"
    ] = tool_result

    if "shared_memory" not in data:

        data["shared_memory"] = {}

    data["shared_memory"][
        "venue_capacity"
    ] = tool_result.get(
        "capacity",
        0
    )
    data["shared_memory"][
        "venue_cost"
    ] = tool_result.get(
         "estimated_cost",
             0
    )

    capacity = int(
        tool_result.get(
            "capacity",
            0
        ) or 0
    )

    if capacity >= 5000:

        data["shared_memory"][
            "venue_complexity"
        ] = "extreme"

    elif capacity >= 1000:

        data["shared_memory"][
            "venue_complexity"
        ] = "high"

    else:

        data["shared_memory"][
            "venue_complexity"
        ] = "standard"

    prompt = PromptTemplate(

        input_variables=[

            "event_type",

            "location",

            "guests",

            "budget",

            "theme",

            "classification",

            "tool_result"
        ],

        template="""
You are an AI venue planning system.

Return ONLY valid JSON.

Event Type: {event_type}
Location: {location}
Guests: {guests}
Budget: {budget}
Theme: {theme}

Classification: {classification}

Venue Tool Recommendation:
{tool_result}

Return format:

{{
  "venue_name": "",
  "capacity": 0,
  "estimated_cost": 0,
  "location_advantage": ""
}}
"""
    )

    try:

        result = run_agent_prompt(

            prompt,

            {

                "event_type":
                    data.get(
                        "event_type"
                    ),

                "location":
                    data.get(
                        "location"
                    ),

                "guests":
                    data.get(
                        "guests"
                    ),

                "budget":
                    data.get(
                        "budget"
                    ),

                "theme":
                    data.get(
                        "theme"
                    ),

                "classification":
                    str(classification),

                "tool_result":
                    str(tool_result)
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

        parsed = json.loads(
            result
        )

        print("\n===== LLM VENUE RESPONSE =====")
        print(parsed)
        print("=============================\n")

        parsed["venue_name"] = parsed.get(
            "venue_name"
        ) or tool_result.get(
              "venue_name",
               "Unknown Venue"
            )
        

        tool_capacity = tool_result.get(
            "capacity",
            0
        )

        llm_capacity = parsed.get(
            "capacity"
        )

        parsed["capacity"] = int(
            tool_capacity
            if not llm_capacity or llm_capacity <= 0
            else llm_capacity
        )

        tool_cost = tool_result.get(
            "estimated_cost",
            0
        )

        llm_cost = parsed.get(
            "estimated_cost"
        )

        parsed["estimated_cost"] = int(
            tool_cost
            if not llm_cost or llm_cost <= 0
            else llm_cost
        )

        parsed["location_advantage"] = parsed.get(
           "location_advantage",
            tool_result.get(
                "location_advantage",
                ""
            )
        )

        parsed[
            "tool_recommendation"
        ] = tool_result

        data["venue"] = parsed
        data["venueName"] = parsed["venue_name"]

    except Exception as e:

        data["venue"] = {

            "venue_name":
                "Grand Convention Center",

            "capacity":
                1000,

            "estimated_cost":
                500000,

            "location_advantage":
                "Central City Access",

            "tool_recommendation":
                tool_result,

            "error":
                str(e)
        }

    return data