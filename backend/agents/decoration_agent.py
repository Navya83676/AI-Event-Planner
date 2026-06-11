from services.llm_service import run_agent_prompt
from langchain_core.prompts import PromptTemplate

import json
from utils.parser import safe_json_parse


def get_dynamic_decoration(
    event_type="",
    theme="",
    guests=100
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

        decoration = {

            "theme_style":
                "Futuristic Tech Experience",

            "stage_design":
                "Massive LED wall with holographic stage visuals and AI-inspired setup",

            "lighting":
                "Blue neon ambient lighting with synchronized smart lights",

            "flower_arrangement":
                "Minimal modern decor with premium indoor plants",

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

        decoration = {

            "theme_style":
                "Cyberpunk Innovation Arena",

            "stage_design":
                "Interactive coding stage with giant digital displays",

            "lighting":
                "RGB gaming lights with dynamic moving effects",

            "flower_arrangement":
                "Minimal industrial decoration with tech aesthetics",

            "estimated_cost":
                140000
        }

    # =========================
    # GAMING TOURNAMENT
    # =========================

    elif (
        "gaming" in event_type or
        "tournament" in event_type
    ):

        decoration = {

            "theme_style":
                "Esports Championship Experience",

            "stage_design":
                "Professional gaming arena with immersive LED visuals",

            "lighting":
                "Dynamic laser lighting and RGB synchronized effects",

            "flower_arrangement":
                "Gaming-themed stage props and futuristic decor",

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

        decoration = {

            "theme_style":
                "Luxury Fashion Runway",

            "stage_design":
                "Premium runway with cinematic visual backdrop",

            "lighting":
                "Elegant spotlight systems with luxury ambiance",

            "flower_arrangement":
                "Premium floral entrance and VIP decor setup",

            "estimated_cost":
                320000
        }

    # =========================
    # CULTURAL FESTIVAL
    # =========================

    elif (
        "cultural" in event_type or
        "festival" in event_type
    ):

        decoration = {

            "theme_style":
                "Traditional Cultural Celebration",

            "stage_design":
                "Grand cultural stage with heritage-inspired backdrop",

            "lighting":
                "Warm traditional lighting with festival ambiance",

            "flower_arrangement":
                "Traditional floral decor with vibrant colors",

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

        decoration = {

            "theme_style":
                "Premium Brand Showcase",

            "stage_design":
                "Luxury reveal stage with cinematic product presentation",

            "lighting":
                "Focused product spotlight system with premium ambiance",

            "flower_arrangement":
                "Minimal luxury floral decoration",

            "estimated_cost":
                200000
        }

    # =========================
    # CORPORATE EVENT
    # =========================

    elif (
        "corporate" in event_type or
        "business" in event_type
    ):

        decoration = {

            "theme_style":
                "Executive Corporate Experience",

            "stage_design":
                "Professional conference stage with executive branding",

            "lighting":
                "Clean professional lighting setup",

            "flower_arrangement":
                "Elegant corporate floral arrangements",

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

        decoration = {

            "theme_style":
                "Premium Celebration Party",

            "stage_design":
                "Colorful celebration stage with LED dance floor",

            "lighting":
                "Party lighting with vibrant visual effects",

            "flower_arrangement":
                "Balloon and floral combination decor",

            "estimated_cost":
                90000
        }

    # =========================
    # WEDDING
    # =========================

    elif (
        "wedding" in event_type or
        "marriage" in event_type
    ):

        decoration = {

            "theme_style":
                "Royal Luxury Wedding",

            "stage_design":
                "Grand wedding mandap with premium stage setup",

            "lighting":
                "Warm golden luxury lighting ambiance",

            "flower_arrangement":
                "Premium rose and orchid floral arrangements",

            "estimated_cost":
                400000
        }

    # =========================
    # DEFAULT
    # =========================

    else:

        decoration = {

            "theme_style":
                "Modern Event Experience",

            "stage_design":
                "Professional modular stage setup",

            "lighting":
                "Ambient premium lighting",

            "flower_arrangement":
                "Standard floral decoration",

            "estimated_cost":
                100000
        }

    # =========================
    # GUEST SCALING
    # =========================

    if guests >= 1000:

        decoration["estimated_cost"] += 200000

        decoration[
            "stage_design"
        ] += (
            " with mega crowd visual systems"
        )

    elif guests >= 500:

        decoration["estimated_cost"] += 100000

    return decoration


def decoration_agent(data):

    if "execution_flow" not in data:

        data["execution_flow"] = []

    data["execution_flow"].append(
        "decoration_agent"
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

    budget = int(
        data.get(
            "budget",
            0
        )
    )

    # =========================
    # SMART DECORATION
    # =========================

    smart_decoration = (
        get_dynamic_decoration(

            event_type,
            theme,
            guests
        )
    )

    # =========================
    # BUDGET CONTROL
    # =========================

    if budget <= 200000:

        smart_decoration[
            "estimated_cost"
        ] = min(

            smart_decoration[
                "estimated_cost"
            ],

            60000
        )

    elif budget <= 500000:

        smart_decoration[
            "estimated_cost"
        ] = min(

            smart_decoration[
                "estimated_cost"
            ],

            150000
        )

    # =========================
    # PROMPT
    # =========================

    prompt = PromptTemplate(

        input_variables=[

            "event_type",
            "theme",
            "guests",
            "budget",
            "smart_decoration"
        ],

        template="""
You are an advanced AI decoration planner.

Return ONLY valid JSON.
Do NOT return explanations.
Do NOT use markdown.

Event Type:
{event_type}

Theme:
{theme}

Guests:
{guests}

Budget:
{budget}

Smart Decoration Plan:
{smart_decoration}

Improve the decoration plan intelligently.

Return format:

{{
  "theme_style": "",
  "stage_design": "",
  "lighting": "",
  "flower_arrangement": ""
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

                "guests":
                    guests,

                "budget":
                    budget,

                "smart_decoration":
                    str(smart_decoration)
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

        parsed["theme_style"] = parsed.get(

            "theme_style",

            smart_decoration[
                "theme_style"
            ]
        )

        parsed["stage_design"] = parsed.get(

            "stage_design",

            smart_decoration[
                "stage_design"
            ]
        )

        parsed["lighting"] = parsed.get(

            "lighting",

            smart_decoration[
                "lighting"
            ]
        )

        parsed[
            "flower_arrangement"
        ] = parsed.get(

            "flower_arrangement",

            smart_decoration[
                "flower_arrangement"
            ]
        )
        data["decoration"] = parsed

        data["theme"] = parsed.get(
            "theme_style",
            smart_decoration["theme_style"]
        )

    except Exception as e:

        data["decoration"] = {

            "theme_style":
                smart_decoration["theme_style"],

            "stage_design":
                smart_decoration["stage_design"],

            "lighting":
                smart_decoration["lighting"],

            "flower_arrangement":
                smart_decoration["flower_arrangement"],

            "error":
                str(e)
        }

        data["theme"] = smart_decoration[
            "theme_style"
        ]

    return data