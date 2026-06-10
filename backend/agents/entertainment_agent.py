from services.llm_service import run_agent_prompt
from langchain_core.prompts import PromptTemplate

from tools.entertainment_tool import (
    generate_entertainment_plan
)

import json


def get_dynamic_entertainment(
    event_type="",
    theme=""
):

    event_type = event_type.lower()
    theme = theme.lower()

    # =========================
    # TECH / STARTUP EVENTS
    # =========================

    if (
        "tech" in event_type or
        "startup" in event_type or
        "conference" in event_type
    ):

        return {

            "main_entertainment": [

                "AI-powered LED stage experience",

                "Tech product demo zones",

                "Interactive VR experience",

                "Startup pitch battle",

                "Live innovation showcase"
            ],

            "guest_engagement":
                "Interactive networking lounges with AI matchmaking and digital participation activities",

            "stage_performance":
                "Futuristic keynote visuals with synchronized lighting and holographic stage effects",

            "estimated_cost":
                180000
        }

    # =========================
    # HACKATHON
    # =========================

    elif (
        "hackathon" in event_type or
        "coding" in event_type
    ):

        return {

            "main_entertainment": [

                "Live coding challenge arena",

                "Gaming chill zone",

                "AI debugging contests",

                "Midnight coding competitions",

                "Team collaboration activities"
            ],

            "guest_engagement":
                "Mentor interaction booths and coding mini-games for participants",

            "stage_performance":
                "Live project demo presentations and innovation award sessions",

            "estimated_cost":
                120000
        }

    # =========================
    # GAMING TOURNAMENT
    # =========================

    elif (
        "gaming" in event_type or
        "tournament" in event_type
    ):

        return {

            "main_entertainment": [

                "Esports main arena",

                "Live shoutcasting setup",

                "Streamer interaction zone",

                "VR gaming booths",

                "Audience gaming competitions"
            ],

            "guest_engagement":
                "Interactive gaming battles and audience participation contests",

            "stage_performance":
                "Grand esports finals with cinematic lighting and laser effects",

            "estimated_cost":
                250000
        }

    # =========================
    # FASHION SHOW
    # =========================

    elif (
        "fashion" in event_type or
        "runway" in event_type
    ):

        return {

            "main_entertainment": [

                "Luxury runway showcase",

                "Celebrity guest appearances",

                "Designer showcase presentations",

                "Live DJ performance",

                "Photo and media experience zones"
            ],

            "guest_engagement":
                "VIP photo sessions and interactive brand experiences",

            "stage_performance":
                "High-end runway production with synchronized lighting and cinematic visuals",

            "estimated_cost":
                300000
        }

    # =========================
    # CULTURAL FESTIVAL
    # =========================

    elif (
        "cultural" in event_type or
        "festival" in event_type
    ):

        return {

            "main_entertainment": [

                "Traditional dance performances",

                "Live music bands",

                "Cultural competitions",

                "Food and art exhibition",

                "Folk performance showcases"
            ],

            "guest_engagement":
                "Community participation activities and public engagement performances",

            "stage_performance":
                "Large-scale cultural performances with immersive lighting and sound",

            "estimated_cost":
                220000
        }

    # =========================
    # PRODUCT LAUNCH
    # =========================

    elif (
        "product" in event_type or
        "launch" in event_type
    ):

        return {

            "main_entertainment": [

                "Immersive product reveal",

                "Interactive demo experience",

                "Media interaction zone",

                "Brand storytelling visuals",

                "Celebrity launch appearance"
            ],

            "guest_engagement":
                "Hands-on product experiences and influencer engagement sessions",

            "stage_performance":
                "Cinematic launch presentation with synchronized visual effects",

            "estimated_cost":
                200000
        }

    # =========================
    # CORPORATE EVENTS
    # =========================

    elif (
        "corporate" in event_type or
        "business" in event_type
    ):

        return {

            "main_entertainment": [

                "Corporate award ceremony",

                "Executive networking lounge",

                "Live business presentations",

                "Motivational speaker session",

                "Corporate gala dinner"
            ],

            "guest_engagement":
                "Professional networking activities and team collaboration experiences",

            "stage_performance":
                "Corporate visual presentation with premium event production",

            "estimated_cost":
                150000
        }

    # =========================
    # BIRTHDAY / PARTY
    # =========================

    elif (
        "birthday" in event_type or
        "party" in event_type
    ):

        return {

            "main_entertainment": [

                "Live DJ party",

                "Dance performances",

                "Interactive games",

                "Photo booth experience",

                "Cake celebration ceremony"
            ],

            "guest_engagement":
                "Fun social interaction games and live audience participation",

            "stage_performance":
                "High-energy dance floor lighting and celebration visuals",

            "estimated_cost":
                80000
        }

    # =========================
    # DEFAULT
    # =========================

    return {

        "main_entertainment": [

            "Live music performance",

            "Guest interaction activities",

            "Stage hosting",

            "Entertainment sessions"
        ],

        "guest_engagement":
            "Interactive audience engagement experiences",

        "stage_performance":
            "Professional stage performance setup",

        "estimated_cost":
            100000
    }


def entertainment_agent(data):

    if "execution_flow" not in data:

        data["execution_flow"] = []

    data["execution_flow"].append(
        "entertainment_agent"
    )

    event_type = data.get(
        "event_type",
        ""
    )

    theme = data.get(
        "theme",
        ""
    )

    guests = int(
        data.get(
            "guests",
            100
        )
    )

    # =========================
    # TOOL DATA
    # =========================

    tool_data = generate_entertainment_plan(

        event_type,

        theme
    )

    # =========================
    # RULE-BASED INTELLIGENCE
    # =========================

    smart_entertainment = (
        get_dynamic_entertainment(

            event_type,
            theme
        )
    )

    # =========================
    # EVENT SCALE LOGIC
    # =========================

    if guests >= 1000:

        smart_entertainment[
            "estimated_cost"
        ] += 150000

        smart_entertainment[
            "main_entertainment"
        ].append(
            "Mega crowd laser experience"
        )

    elif guests >= 500:

        smart_entertainment[
            "estimated_cost"
        ] += 70000

        smart_entertainment[
            "main_entertainment"
        ].append(
            "Premium audience engagement zone"
        )

    # =========================
    # PROMPT
    # =========================

    prompt = PromptTemplate(

        input_variables=[

            "event_type",
            "theme",
            "tool_data",
            "smart_entertainment",
            "guests"
        ],

        template="""
You are an advanced AI entertainment planner.

Return ONLY valid JSON.
Do NOT return explanations.
Do NOT use markdown.

Event Type:
{event_type}

Theme:
{theme}

Guests:
{guests}

Entertainment Tool:
{tool_data}

Smart Entertainment Plan:
{smart_entertainment}

Improve the entertainment plan intelligently.

Return format:

{{
  "main_entertainment": [],
  "guest_engagement": "",
  "stage_performance": ""
}}
"""
    )

    try:

        result = run_agent_prompt(

            prompt,

            {

                "event_type":
                    event_type,

                "theme":
                    theme,

                "tool_data":
                    str(tool_data),

                "smart_entertainment":
                    str(smart_entertainment),

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

        parsed = json.loads(result)

        parsed[
            "main_entertainment"
        ] = parsed.get(
            "main_entertainment",
            smart_entertainment[
                "main_entertainment"
            ]
        )

        parsed[
            "guest_engagement"
        ] = parsed.get(
            "guest_engagement",
            smart_entertainment[
                "guest_engagement"
            ]
        )

        parsed[
            "stage_performance"
        ] = parsed.get(
            "stage_performance",
            smart_entertainment[
                "stage_performance"
            ]
        )

        parsed[
            "tool_recommendation"
        ] = tool_data

        data["entertainment"] = parsed
        
    except Exception as e:
        data["entertainment"] = {
            "main_entertainment":
            smart_entertainment[
                "main_entertainment"
            ],
            "guest_engagement":
            smart_entertainment[
                "guest_engagement"
            ],
            "stage_performance":
            smart_entertainment[
                "stage_performance"
            ],
            "tool_recommendation":
            tool_data,
            "error":
            str(e)
    }

    return data