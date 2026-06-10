from services.llm_service import run_agent_prompt

from langchain_core.prompts import PromptTemplate

import json


def event_classifier_agent(data):

    if "execution_flow" not in data:

        data["execution_flow"] = []

    data["execution_flow"].append(
        "event_classifier_agent"
    )

    if "shared_memory" not in data:

        data["shared_memory"] = {

            "event_scale": "",

            "budget_priority": "",

            "needs_entertainment": False,

            "needs_security": False,

            "available_tools": [],

            "agent_messages": []
        }

    prompt = PromptTemplate(

        input_variables=[

            "name",

            "event_type",

            "requirements",

            "guests"
        ],

        template="""
You are an AI event classification system.

Return ONLY valid JSON.

Event Name: {name}
Event Type: {event_type}
Requirements: {requirements}
Guests: {guests}

Return format:

{{
  "event_category": "",
  "event_scale": "",
  "event_style": "",
  "priority": "",
  "needs_security": true,
  "needs_entertainment": true,
  "budget_priority": "",
  "recommended_tools": []
}}
"""
    )

    try:

        result = run_agent_prompt(

            prompt,

            {

                "name":
                    data.get(
                        "event_name"
                    ),

                "event_type":
                    data.get(
                        "event_type"
                    ),

                "requirements":
                    data.get(
                        "requirements"
                    ),

                "guests":
                    data.get(
                        "guests"
                    )
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

        classification = json.loads(
            result
        )
        guests = int(
            data.get(
                "guests",
                0
                )
                )
        if guests >= 1000:
            classification["event_scale"] = "Mega"
        elif guests >= 500:
            classification["event_scale"] = "Large"
        elif guests >= 200:
            classification["event_scale"] = "Medium"
        else:
            classification["event_scale"] = "Small"

        data["classification"] = {
            "event_category":
                classification.get(
                    "event_category",
                     "general"
                    ),
            "event_scale":
                classification.get(
                    "event_scale",
                     "Medium"
                    ),
                "event_style":
                    classification.get(
                        "event_style",
                        "modern"
                    ),
                  "priority":
                    classification.get(
                        "priority",
                        "balanced"
                    )
        }

        data["shared_memory"][
            "event_scale"
        ] = classification.get(
            "event_scale",
            "Medium"
        )

        data["shared_memory"][
            "budget_priority"
        ] = classification.get(
            "budget_priority",
            "balanced"
        )

        data["shared_memory"][
            "needs_security"
        ] = classification.get(
            "needs_security",
            False
        )

        data["shared_memory"][
            "needs_entertainment"
        ] = classification.get(
            "needs_entertainment",
            False
        )

        data["shared_memory"][
            "available_tools"
        ] = classification.get(
            "recommended_tools",
            []
        )
        if "insights" not in data:
            data["insights"] = []
        data["insights"].append(
            f"AI classified this as a {classification.get('event_scale')} scale event"
        )

        data["shared_memory"][
            "agent_messages"
        ].append({

            "from":
                "event_classifier_agent",

            "to":
                "all_agents",

            "message":
                f"""
        Event classified as
        {classification.get('event_category')}
        with
        {classification.get('event_scale')}
        scale.
        """
        })

    except Exception as e:

        data["classification"] = {

            "event_category":
                "general",

            "event_scale":
                "Medium",

            "event_style":
                "modern",

            "priority":
                "balanced"
        }

        data["shared_memory"][
            "agent_messages"
        ].append({

            "from":
                "event_classifier_agent",

            "to":
                "supervisor_agent",

            "message":
                f"Classification failed: {str(e)}"
        })

    return data