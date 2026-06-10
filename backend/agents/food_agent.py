from services.llm_service import run_agent_prompt

from langchain_core.prompts import PromptTemplate

from tools.food_tool import (
    calculate_food_plan
)

import json


def food_agent(data):

    # =========================
    # EXECUTION FLOW
    # =========================

    if "execution_flow" not in data:

        data["execution_flow"] = []

    data["execution_flow"].append(
        "food_agent"
    )

    # =========================
    # INPUTS
    # =========================

    event_type = str(
        data.get(
            "event_type",
            ""
        )
    ).lower()

    guests = int(
        data.get(
            "guests",
            100
        )
    )

    budget = int(
        data.get(
            "budget",
            50000
        )
    )

    classification = data.get(
        "classification",
        {}
    )

    # =========================
    # TOOL EXECUTION
    # =========================

    tool_result = calculate_food_plan(

        guests=guests,

        event_type=event_type
    )

    # =========================
    # EVENT-AWARE CUISINE LOGIC
    # =========================

    cuisine_style = "Multi Cuisine"

    service_type = "Buffet"

    vip_services = []

    # TECH / STARTUP / HACKATHON

    if any(

        keyword in event_type

        for keyword in [

            "tech",
            "startup",
            "hackathon",
            "conference",
            "expo"
        ]
    ):

        cuisine_style = (
            "Modern Fusion"
        )

        service_type = (
            "Live Food Stations"
        )

        vip_services = [

            "Coffee Bar",

            "Energy Drink Counter",

            "Snack Pods",

            "Midnight Refreshments"
        ]

    # WEDDING

    elif any(

        keyword in event_type

        for keyword in [

            "wedding",
            "marriage",
            "reception"
        ]
    ):

        cuisine_style = (
            "Royal Indian"
        )

        service_type = (
            "Grand Buffet"
        )

        vip_services = [

            "Live Chaat Counter",

            "Mocktail Bar",

            "Premium Dessert Lounge",

            "Traditional Sweet Section"
        ]

    # BIRTHDAY

    elif any(

        keyword in event_type

        for keyword in [

            "birthday",
            "party"
        ]
    ):

        cuisine_style = (
            "Fun Party Menu"
        )

        service_type = (
            "Casual Buffet"
        )

        vip_services = [

            "Cake Zone",

            "Ice Cream Counter",

            "Snack Bar"
        ]

    # GAMING EVENTS

    elif any(

        keyword in event_type

        for keyword in [

            "gaming",
            "tournament"
        ]
    ):

        cuisine_style = (
            "Fast Casual"
        )

        service_type = (
            "Quick Serve Stations"
        )

        vip_services = [

            "Gaming Snack Counter",

            "Cold Beverage Station",

            "24x7 Energy Snacks"
        ]

    # FASHION EVENTS

    elif any(

        keyword in event_type

        for keyword in [

            "fashion",
            "runway"
        ]
    ):

        cuisine_style = (
            "Luxury Continental"
        )

        service_type = (
            "Premium Fine Dining"
        )

        vip_services = [

            "VIP Mocktail Lounge",

            "Designer Dessert Plating",

            "Luxury Dining Experience"
        ]

    # =========================
    # BUDGET LOGIC
    # =========================

    budget_tier = "Standard"

    if budget >= 1000000:

        budget_tier = "Ultra Luxury"

    elif budget >= 500000:

        budget_tier = "Premium"

    elif budget >= 200000:

        budget_tier = "Professional"

    # =========================
    # SHARED MEMORY
    # =========================

    if "shared_memory" not in data:

        data["shared_memory"] = {}

    data["shared_memory"][
        "food_service_type"
    ] = service_type

    data["shared_memory"][
        "food_estimated_cost"
    ] = tool_result.get(
        "estimated_cost",
        0
    )

    # =========================
    # PROMPT
    # =========================

    prompt = PromptTemplate(

        input_variables=[

            "event_type",

            "guests",

            "budget",

            "classification",

            "tool_result",

            "cuisine_style",

            "service_type",

            "vip_services",

            "budget_tier"
        ],

        template="""
You are an elite AI catering planner.

Return ONLY valid JSON.
Do NOT return explanations.
Do NOT use markdown.

Event Type: {event_type}

Guests: {guests}

Budget: {budget}

Budget Tier:
{budget_tier}

Cuisine Style:
{cuisine_style}

Service Type:
{service_type}

VIP Services:
{vip_services}

Classification:
{classification}

Food Tool Recommendation:
{tool_result}

Generate a realistic,
premium-quality food plan.

Return format:

{{
  "cuisine_style": "",
  "service_type": "",
  "starters": [],
  "main_course": [],
  "desserts": [],
  "beverages": [],
  "vip_services": []

}}
"""
    )

    # =========================
    # AI EXECUTION
    # =========================

    try:

        result = run_agent_prompt(

            prompt,

            {

                "event_type":
                    event_type,

                "guests":
                    guests,

                "budget":
                    budget,

                "budget_tier":
                    budget_tier,

                "classification":
                    str(classification),

                "tool_result":
                    str(tool_result),

                "cuisine_style":
                    cuisine_style,

                "service_type":
                    service_type,

                "vip_services":
                    str(vip_services)
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

        # SAFE FALLBACKS

        parsed[
            "cuisine_style"
        ] = parsed.get(
            "cuisine_style",
            cuisine_style
        )

        parsed[
            "service_type"
        ] = parsed.get(
            "service_type",
            service_type
        )

        parsed[
            "starters"
        ] = parsed.get(
            "starters",
            []
        )

        parsed[
            "main_course"
        ] = parsed.get(
            "main_course",
            []
        )

        parsed[
            "desserts"
        ] = parsed.get(
            "desserts",
            []
        )

        parsed[
            "beverages"
        ] = parsed.get(
            "beverages",
            []
        )

        parsed[
            "vip_services"
        ] = parsed.get(
            "vip_services",
            vip_services
        )

        parsed[
            "tool_recommendation"
        ] = tool_result

        data["food"] = parsed

    except Exception as e:

        data["food"] = {

            "cuisine_style":
                cuisine_style,

            "service_type":
                service_type,

            "starters": [
                "Veg Starters"
            ],

            "main_course": [
                tool_result.get(
                    "catering_type",
                    "Premium Buffet"
                )
                
            ],

            "desserts": [
                "Dessert Counter"
            ],

            "beverages": [
                "Soft Drinks"
            ],

            "vip_services":
                vip_services,

            "tool_recommendation":
                tool_result,

            "error":
                str(e)
        }

    return data