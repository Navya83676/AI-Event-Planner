from services.llm_service import run_agent_prompt

from langchain_core.prompts import PromptTemplate

import json
from utils.parser import safe_json_parse

def supervisor_agent(state):

    print(
        "\n===== SUPERVISOR AGENT ====="
    )

    # =========================
    # EXECUTION FLOW
    # =========================

    if "execution_flow" not in state:

        state["execution_flow"] = []

    state["execution_flow"].append(
        "supervisor_agent"
    )

    # =========================
    # SHARED MEMORY
    # =========================

    if "shared_memory" not in state:

        state["shared_memory"] = {}

    shared_memory = state[
        "shared_memory"
    ]

    # =========================
    # EVENT DETAILS
    # =========================

    event_type = str(
        state.get(
            "event_type",
            ""
        )
    ).lower()

    event_theme = str(
        state.get(
            "theme",
            ""
        )
    ).lower()

    guests = int(
        state.get(
            "guests",
            0
        )
    )

    budget = int(
        state.get(
            "budget",
            0
        )
    )

   # =========================
    # EVENT SCALE
    # =========================

    if guests >= 1000:

        event_scale = "Mega"

    elif guests >= 500:

        event_scale = "Large"

    elif guests >= 200:

        event_scale = "Medium"

    else:

        event_scale = "Small"

    # =========================
    # VENUE COMPLEXITY
    # =========================

    if (

        "gaming" in event_type or
        "festival" in event_type or
        "concert" in event_type or
        "fashion" in event_type

    ):

        venue_complexity = "extreme"

    elif (

        "conference" in event_type or
        "hackathon" in event_type or
        "expo" in event_type or
        "startup" in event_type

    ):

        venue_complexity = "high"

    else:

        venue_complexity = "standard"

    # =========================
    # VIP LEVEL
    # =========================

    if budget >= 5000000:

        vip_level = "elite"

    elif budget >= 2000000:

        vip_level = "premium"

    else:

        vip_level = "standard"

    # =========================
    # CROWD DENSITY
    # =========================

    if guests >= 5000:

        crowd_density = "extreme"

    elif guests >= 1500:

        crowd_density = "high"

    elif guests >= 500:

        crowd_density = "medium"

    else:

        crowd_density = "low"

    # =========================
    # EVENT ENERGY
    # =========================

    high_energy_events = [

        "gaming",
        "concert",
        "festival",
        "dj",
        "party",
        "fashion"
    ]

    medium_energy_events = [

        "conference",
        "startup",
        "hackathon",
        "expo"
    ]

    if any(
        word in event_type
        for word in high_energy_events
    ):

        event_energy = "high"

    elif any(
        word in event_type
        for word in medium_energy_events
    ):

        event_energy = "medium"
    elif(
        "wedding" in event_type or
        "marriage" in event_type
    ):
        event_energy="medium"

    else:

        event_energy = "balanced"

    # =========================
    # SECURITY REQUIREMENTS
    # =========================

    security_keywords = [

        "gaming",
        "festival",
        "concert",
        "fashion",
        "expo",
        "launch"
    ]

    needs_security = (

        guests >= 1000 or

        any(
            word in event_type
            for word in security_keywords
        )
    )

    # =========================
    # AI RISK LEVEL
    # =========================

    if (

        venue_complexity == "extreme" or
        crowd_density == "extreme"

    ):

        ai_risk_level = "critical"

    elif (

        venue_complexity == "high" or
        crowd_density == "high"

    ):

        ai_risk_level = "high"

    elif guests >= 300:

        ai_risk_level = "medium"

    else:

        ai_risk_level = "low"

    # =========================
    # RECOMMENDED THEME
    # =========================

    if "gaming" in event_type:

        recommended_theme = (
            "Cyberpunk Neon Arena"
        )

    elif "fashion" in event_type:

        recommended_theme = (
            "Luxury Runway Experience"
        )

    elif "startup" in event_type:

        recommended_theme = (
            "Innovation Hub"
        )
    elif (
        "wedding" in event_type or
         "marriage" in event_type
):

     recommended_theme = (
        "Royal Luxury Wedding"
    )

    elif "conference" in event_type:

        recommended_theme = (
            "Corporate Intelligence"
        )

    elif "hackathon" in event_type:

        recommended_theme = (
            "Future Tech Lab"
        )

    elif "festival" in event_type:

        recommended_theme = (
            "Cultural Celebration"
        )

    elif event_theme:

        recommended_theme = (
            event_theme
        )

    else:

        recommended_theme = (
            "AI Smart Event Experience"
        )

    # =========================
    # ENTERTAINMENT FLAG
    # =========================

    entertainment_events = [

        "wedding",
        "marriage",
        "concert",
        "festival",
        "gaming",
        "party",
        "fashion",
        "celebration"
]

    needs_entertainment = any(

        word in event_type

        for word in entertainment_events
    )

    # =========================
    # FOOD COMPLEXITY
    # =========================

    if guests >= 2000:

        food_complexity = "massive"

    elif guests >= 1000:

        food_complexity = "large"

    elif guests >= 300:
        food_complexity = "medium"

    else:

        food_complexity = "standard"

    # =========================
    # AVAILABLE TOOLS
    # =========================

    available_tools = [

        "venue_search_tool",

        "budget_optimizer_tool",

        "timeline_generator_tool",

        "food_recommendation_tool",

        "security_planning_tool",

        "guest_prediction_tool",

        "crowd_management_tool",

        "vendor_matching_tool",

        "ai_theme_engine"
    ]

    # =========================
    # SHARED MEMORY UPDATE
    # =========================

    shared_memory.update({

        "event_scale":
            event_scale,

        "venue_complexity":
            venue_complexity,

        "needs_security":
            needs_security,

        "vip_level":
            vip_level,

        "crowd_density":
            crowd_density,

        "event_energy":
            event_energy,

        "ai_risk_level":
            ai_risk_level,

        "recommended_theme":
            recommended_theme,

        "needs_entertainment":
            needs_entertainment,

        "food_complexity":
            food_complexity,

        "available_tools":
            available_tools,

        "agent_messages":
            shared_memory.get(
                "agent_messages",
                []
            )
    
    })

    # =========================
    # AI SUPERVISOR INSIGHTS
    # =========================

    insights = [
         
         f"Expected attendance: {guests} guests",

         f"Budget allocated: Rs. {budget:,}",
        
        f"Venue complexity detected as {venue_complexity}",

        f"Crowd density risk evaluated as {crowd_density}",

        f"Security risk level marked as {ai_risk_level}",

        f"Recommended event experience theme: {recommended_theme}"
    ]

    # =========================
    # LLM INTELLIGENCE
    # =========================

    prompt = PromptTemplate(

        input_variables=[

            "event_type",
            "guests",
            "budget",
            "shared_memory"
        ],

        template="""
You are an AI event supervisor.

Return ONLY valid JSON.

Event Type:
{event_type}

Guests:
{guests}

Budget:
{budget}

Shared Memory:
{shared_memory}

Return format:

{{
  "ai_summary": "",
  "risk_advisory": "",
  "optimization_tip": "",
  "execution_priority": ""
}}
"""
    )

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

                "shared_memory":
                    str(shared_memory)
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

        insights.extend([

            parsed.get(
                "ai_summary",
                ""
            ),

            parsed.get(
                "risk_advisory",
                ""
            ),

            parsed.get(
                "optimization_tip",
                ""
            ),

            parsed.get(
                "execution_priority",
                ""
            )
        ])

    except Exception as e:

        insights.append(
            f"Supervisor AI fallback activated: {str(e)}"
        )

    # =========================
    # SAVE INSIGHTS
    # =========================

    state["insights"] = insights

    print(
        "Supervisor initialized advanced orchestration state"
    )

    return state