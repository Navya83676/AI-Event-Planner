from services.llm_service import run_agent_prompt
from langchain_core.prompts import PromptTemplate

from tools.timeline_tool import (
    generate_timeline_plan
)

import json


def build_duration_based_timeline(
    event_type,
    event_duration,
    requirements=""
):

    event_type = str(event_type).lower()
    duration = str(event_duration).lower()

    # =====================
    # 2 HOURS
    # =====================

    if "2 hours" in duration:

        if "wedding" in event_type:

            return {
                "event": [
                    {"activity":"Venue Decoration","time":"08:00 AM"},
                    {"activity":"Stage Setup","time":"08:20 AM"},
                    {"activity":"Guest Arrival","time":"08:40 AM"},
                    {"activity":"Wedding Ceremony","time":"09:00 AM"},
                    {"activity":"Family Rituals","time":"09:30 AM"},
                    {"activity":"Live Music & Dance","time":"09:50 AM"},
                    {"activity":"Premium Catering","time":"10:10 AM"},
                    {"activity":"Event Closing","time":"10:30 AM"}
                ]
            }

        elif "conference" in event_type:

            return {
                "event": [
                    {"activity":"Registration","time":"09:00 AM"},
                    {"activity":"Opening Keynote","time":"09:15 AM"},
                    {"activity":"Speaker Session","time":"09:40 AM"},
                    {"activity":"Industry Discussion","time":"10:05 AM"},
                    {"activity":"Networking","time":"10:30 AM"},
                    {"activity":"Closing Remarks","time":"10:50 AM"}
                ]
            }

        elif "music" in event_type or "festival" in event_type:

            return {
                "event": [
                    {"activity":"Gate Opening","time":"05:00 PM"},
                    {"activity":"Opening Performance","time":"05:20 PM"},
                    {"activity":"Main Music Session","time":"05:50 PM"},
                    {"activity":"Audience Engagement","time":"06:30 PM"},
                    {"activity":"Headline Performance","time":"06:50 PM"},
                    {"activity":"Festival Closing","time":"07:00 PM"}
                ]
            }

        elif "fashion" in event_type:

            return {
                "event": [
                    {"activity":"Guest Arrival","time":"06:00 PM"},
                    {"activity":"Designer Introduction","time":"06:15 PM"},
                    {"activity":"Runway Show","time":"06:30 PM"},
                    {"activity":"Brand Showcase","time":"07:00 PM"},
                    {"activity":"Photography Session","time":"07:30 PM"},
                    {"activity":"Closing Ceremony","time":"08:00 PM"}
                ]
            }

        elif "hackathon" in event_type:

            return {
                "event": [
                    {"activity":"Participant Registration","time":"09:00 AM"},
                    {"activity":"Problem Statement","time":"09:15 AM"},
                    {"activity":"Coding Sprint","time":"09:30 AM"},
                    {"activity":"Project Submission","time":"10:30 AM"},
                    {"activity":"Demo Session","time":"10:45 AM"},
                    {"activity":"Winner Announcement","time":"11:00 AM"}
                ]
            }

        elif "gaming" in event_type:

            return {
                "event": [
                    {"activity":"Player Registration","time":"10:00 AM"},
                    {"activity":"Qualifier Match","time":"10:20 AM"},
                    {"activity":"Semi Final","time":"10:50 AM"},
                    {"activity":"Grand Final","time":"11:20 AM"},
                    {"activity":"Prize Distribution","time":"11:50 AM"}
                ]
            }

    # =====================
    # 4 HOURS
    # =====================

    elif "4 hours" in duration:

        if "music" in event_type or "festival" in event_type:

            return {
                "event":[
                    {"activity":"Gate Opening","time":"05:00 PM"},
                    {"activity":"Opening DJ Set","time":"05:30 PM"},
                    {"activity":"Artist Performance","time":"06:30 PM"},
                    {"activity":"Headliner Show","time":"08:00 PM"},
                    {"activity":"Festival Closing","time":"09:00 PM"}
                ]
            }

        elif "fashion" in event_type:

            return {
                "event":[
                    {"activity":"Guest Arrival","time":"06:00 PM"},
                    {"activity":"VIP Reception","time":"06:30 PM"},
                    {"activity":"Runway Show","time":"07:00 PM"},
                    {"activity":"Designer Showcase","time":"08:00 PM"},
                    {"activity":"Closing Ceremony","time":"09:00 PM"}
                ]
            }

        elif "gaming" in event_type:

            return {
                "event":[
                    {"activity":"Player Registration","time":"10:00 AM"},
                    {"activity":"Qualifier Match","time":"11:00 AM"},
                    {"activity":"Semi Final","time":"12:30 PM"},
                    {"activity":"Grand Final","time":"02:00 PM"}
                ]
            }
        elif "conference" in event_type:

            return {
            "event":[
                {"activity":"Registration","time":"08:00 AM"},
                {"activity":"Opening Keynote","time":"08:30 AM"},
                {"activity":"Industry Session","time":"09:15 AM"},
                {"activity":"Panel Discussion","time":"10:00 AM"},
                {"activity":"Networking Break","time":"11:00 AM"},
                {"activity":"Closing Remarks","time":"12:00 PM"}
            ]
        }

        elif "hackathon" in event_type:

            return {
            "event":[
                {"activity":"Participant Registration","time":"09:00 AM"},
                {"activity":"Problem Statement Release","time":"09:30 AM"},
                {"activity":"Team Formation","time":"10:00 AM"},
                {"activity":"Coding Sprint","time":"10:30 AM"},
                {"activity":"Project Submission","time":"12:00 PM"},
                {"activity":"Demo Session","time":"12:30 PM"},
                {"activity":"Winner Announcement","time":"01:00 PM"}
            ]
        }

        elif "wedding" in event_type:

            return {
            "event":[
                {"activity":"Venue Decoration","time":"08:00 AM"},
                {"activity":"Guest Arrival","time":"09:00 AM"},
                {"activity":"Wedding Ceremony","time":"10:00 AM"},
                {"activity":"Blessing Ceremony","time":"11:00 AM"},
                {"activity":"Photography Session","time":"11:30 AM"},
                {"activity":"Lunch Service","time":"12:00 PM"}
            ]
        }
    
        else:

            return {
            "event":[
                {"activity":"Venue Preparation","time":"09:00 AM"},
                {"activity":"Guest Arrival","time":"09:30 AM"},
                {"activity":"Opening Session","time":"10:00 AM"},
                {"activity":"Main Activities","time":"11:00 AM"},
                {"activity":"Networking","time":"12:00 PM"},
                {"activity":"Closing Ceremony","time":"01:00 PM"}
            ]
        }

    # =====================
    # HALF DAY
    # =====================

    elif "half day" in duration:

        if "wedding" in event_type:

            return {
                "event":[
                    {"activity":"Venue Decoration","time":"08:00 AM"},
                    {"activity":"Guest Arrival","time":"09:00 AM"},
                    {"activity":"Wedding Ceremony","time":"10:00 AM"},
                    {"activity":"Family Rituals","time":"11:00 AM"},
                    {"activity":"Photography Session","time":"12:00 PM"},
                    {"activity":"Lunch Service","time":"01:00 PM"},
                    {"activity":"Reception","time":"02:00 PM"}
                ]
            }

        elif "conference" in event_type:

            return {
                "event":[
                    {"activity":"Registration","time":"08:00 AM"},
                    {"activity":"Opening Keynote","time":"09:00 AM"},
                    {"activity":"Speaker Session","time":"10:00 AM"},
                    {"activity":"Panel Discussion","time":"11:00 AM"},
                    {"activity":"Networking","time":"12:00 PM"},
                    {"activity":"Lunch","time":"01:00 PM"},
                    {"activity":"Closing Remarks","time":"02:00 PM"}
                ]
            }

        elif "music" in event_type or "festival" in event_type:

            return {
                "event":[
                    {"activity":"Artist Arrival","time":"02:00 PM"},
                    {"activity":"Sound Check","time":"03:00 PM"},
                    {"activity":"Gate Opening","time":"04:00 PM"},
                    {"activity":"Opening Performance","time":"05:00 PM"},
                    {"activity":"Main Artist Show","time":"06:30 PM"},
                    {"activity":"Headliner Concert","time":"08:00 PM"}
                ]
            }

        elif "fashion" in event_type:

            return {
                "event":[
                    {"activity":"Model Check-in","time":"01:00 PM"},
                    {"activity":"Makeup Session","time":"02:00 PM"},
                    {"activity":"Designer Preparation","time":"03:00 PM"},
                    {"activity":"Runway Rehearsal","time":"04:00 PM"},
                    {"activity":"VIP Reception","time":"05:30 PM"},
                    {"activity":"Fashion Show","time":"07:00 PM"}
                ]
            }

        elif "hackathon" in event_type:

            return {
                "event":[
                    {"activity":"Registration","time":"09:00 AM"},
                    {"activity":"Problem Statement","time":"10:00 AM"},
                    {"activity":"Coding Sprint","time":"11:00 AM"},
                    {"activity":"Mentor Review","time":"01:00 PM"},
                    {"activity":"Submission","time":"02:00 PM"},
                    {"activity":"Winner Announcement","time":"03:00 PM"}
                ]
            }

        elif "gaming" in event_type:

            return {
                "event":[
                    {"activity":"Player Registration","time":"09:00 AM"},
                    {"activity":"Arena Setup","time":"10:00 AM"},
                    {"activity":"Group Stage Matches","time":"11:00 AM"},
                    {"activity":"Qualifier Matches","time":"01:00 PM"},
                    {"activity":"Semi Finals","time":"03:00 PM"},
                    {"activity":"Grand Finals","time":"05:00 PM"}
                ]
            }
        else:

            return {
                "event":[
                    {"activity":"Venue Setup","time":"09:00 AM"},
                    {"activity":"Registration","time":"10:00 AM"},
                    {"activity":"Opening Session","time":"11:00 AM"},
                    {"activity":"Main Activities","time":"12:00 PM"},
                    {"activity":"Networking","time":"02:00 PM"},
                    {"activity":"Closing Session","time":"03:00 PM"}
                ]
            }

    # =====================
    # FULL DAY
    # =====================

    elif "full day" in duration:

        if "music" in event_type or "festival" in event_type:

            return {
                "event":[
                    {"activity":"Stage Setup","time":"10:00 AM"},
                    {"activity":"Artist Arrival","time":"12:00 PM"},
                    {"activity":"Sound Check","time":"02:00 PM"},
                    {"activity":"Gate Opening","time":"04:00 PM"},
                    {"activity":"Opening Performance","time":"05:00 PM"},
                    {"activity":"Main Artist Show","time":"07:00 PM"},
                    {"activity":"Headliner Concert","time":"09:00 PM"},
                    {"activity":"Festival Closing","time":"11:30 PM"}
                ]
            }

        elif "fashion" in event_type:

            return {
                "event":[
                    {"activity":"Model Arrival","time":"12:00 PM"},
                    {"activity":"Makeup Session","time":"01:00 PM"},
                    {"activity":"Photography Session","time":"03:00 PM"},
                    {"activity":"Runway Rehearsal","time":"05:00 PM"},
                    {"activity":"VIP Reception","time":"06:00 PM"},
                    {"activity":"Fashion Show","time":"07:00 PM"},
                    {"activity":"Press Conference","time":"09:00 PM"}
                ]
            }

        elif "conference" in event_type:

            return {
                "event":[
                    {"activity":"Registration","time":"08:00 AM"},
                    {"activity":"Opening Keynote","time":"09:00 AM"},
                    {"activity":"Speaker Session","time":"10:00 AM"},
                    {"activity":"Panel Discussion","time":"11:30 AM"},
                    {"activity":"Lunch","time":"01:00 PM"},
                    {"activity":"Workshop","time":"02:00 PM"},
                    {"activity":"Networking","time":"04:00 PM"},
                    {"activity":"Closing Session","time":"06:00 PM"}
                ]
            }

        elif "gaming" in event_type:

            return {
                "event":[
                    {"activity":"Arena Setup","time":"08:00 AM"},
                    {"activity":"Player Registration","time":"09:00 AM"},
                    {"activity":"Group Matches","time":"10:00 AM"},
                    {"activity":"Qualifier Matches","time":"01:00 PM"},
                    {"activity":"Semi Finals","time":"04:00 PM"},
                    {"activity":"Grand Finals","time":"07:00 PM"},
                    {"activity":"Prize Distribution","time":"09:00 PM"}
                ]
            }

        elif "hackathon" in event_type:

            return {
                "event":[
                    {"activity":"Registration","time":"08:00 AM"},
                    {"activity":"Hackathon Launch","time":"09:00 AM"},
                    {"activity":"Coding Sprint","time":"10:00 AM"},
                    {"activity":"Mentor Session","time":"01:00 PM"},
                    {"activity":"Project Development","time":"03:00 PM"},
                    {"activity":"Submission","time":"06:00 PM"},
                    {"activity":"Judging","time":"07:00 PM"}
                ]
            }

        elif "wedding" in event_type:

            return {
                "event":[
                    {"activity":"Venue Decoration","time":"08:00 AM"},
                    {"activity":"Guest Arrival","time":"10:00 AM"},
                    {"activity":"Wedding Ceremony","time":"11:00 AM"},
                    {"activity":"Family Rituals","time":"01:00 PM"},
                    {"activity":"Lunch Service","time":"02:00 PM"},
                    {"activity":"Photography Session","time":"04:00 PM"},
                    {"activity":"Reception","time":"07:00 PM"}
                ]
            }
        
        else:

            return {
                "event":[
                    {"activity":"Venue Setup","time":"08:00 AM"},
                    {"activity":"Registration","time":"09:00 AM"},
                    {"activity":"Opening Session","time":"10:00 AM"},
                    {"activity":"Main Activities","time":"11:00 AM"},
                    {"activity":"Lunch Break","time":"01:00 PM"},
                    {"activity":"Workshops","time":"02:00 PM"},
                    {"activity":"Networking","time":"04:00 PM"},
                    {"activity":"Closing Ceremony","time":"06:00 PM"}
                ]
            }

   # =====================
    # 2 DAYS
    # =====================

    elif "2 days" in duration:

        # =====================
        # MUSIC FESTIVAL
        # =====================

        if "music" in event_type or "festival" in event_type:

            return {
                "day_1":[
                {"activity":"Gate Opening","time":"04:00 PM"},
                {"activity":"Opening DJ Set","time":"05:00 PM"},
                {"activity":"Live Band Performance","time":"06:30 PM"},
                {"activity":"Main Artist Performance","time":"08:00 PM"},
                {"activity":"Headliner Concert","time":"10:00 PM"},
                {"activity":"Day 1 Closing","time":"11:30 PM"}
            ],

            "day_2":[

                {"activity":"Gate Opening","time":"04:00 PM"},
                {"activity":"Artist Warmup Session","time":"05:00 PM"},
                {"activity":"Live Concert","time":"07:00 PM"},
                {"activity":"Special Guest Performance","time":"09:00 PM"},
                {"activity":"Grand Finale","time":"10:30 PM"},
                {"activity":"Festival Closing","time":"11:30 PM"}
                ]
            }
                

        # =====================
        # GAMING TOURNAMENT
        # =====================

        elif "gaming" in event_type or "tournament" in event_type:

            return {
                    "day_1":[
                    {"activity":"Arena Setup","time":"08:00 AM"},
                    {"activity":"Player Registration","time":"09:00 AM"},
                    {"activity":"Opening Ceremony","time":"10:00 AM"},
                    {"activity":"Group Stage Matches","time":"11:00 AM"},
                    {"activity":"Lunch Break","time":"01:00 PM"},
                    {"activity":"Qualifier Matches","time":"02:00 PM"},
                    {"activity":"Streaming Session","time":"05:00 PM"},
                    {"activity":"Day 1 Closing","time":"08:00 PM"}
                    ],

                    "day_2":[

                    {"activity":"Quarter Finals","time":"10:00 AM"},
                    {"activity":"Semi Finals","time":"01:00 PM"},
                    {"activity":"Grand Finals","time":"04:00 PM"},
                    {"activity":"Prize Distribution","time":"07:00 PM"},
                    {"activity":"Champion Ceremony","time":"08:00 PM"}
                    ]
                }

        # =====================
        # CONFERENCE
        # =====================

        elif "conference" in event_type:

            return {
                    "day_1":[
                    {"activity":"Registration Desk Opening","time":"08:00 AM"},
                    {"activity":"Welcome Session","time":"09:00 AM"},
                    {"activity":"Opening Keynote","time":"09:30 AM"},
                    {"activity":"Industry Speaker Session","time":"11:00 AM"},
                    {"activity":"Lunch Break","time":"01:00 PM"},
                    {"activity":"Panel Discussion","time":"02:00 PM"},
                    {"activity":"Networking Session","time":"04:00 PM"},
                    {"activity":"Corporate Dinner","time":"07:00 PM"}
                ],

                "day_2":[

                    {"activity":"Workshops Begin","time":"09:00 AM"},
                    {"activity":"Innovation Showcase","time":"11:00 AM"},
                    {"activity":"Startup Pitch Session","time":"01:00 PM"},
                    {"activity":"Investor Connect","time":"03:00 PM"},
                    {"activity":"Closing Keynote","time":"05:00 PM"},
                    {"activity":"Awards Ceremony","time":"06:00 PM"}
                    ]
               }

        elif "hackathon" in event_type:

            return {
                "day_1":[

                    {"activity":"Venue Setup","time":"07:00 AM"},
                    {"activity":"Participant Registration","time":"08:00 AM"},
                    {"activity":"Team Formation","time":"09:00 AM"},
                    {"activity":"Hackathon Launch","time":"10:00 AM"},
                    {"activity":"Problem Statement Release","time":"10:30 AM"},
                    {"activity":"Mentor Introduction","time":"11:00 AM"},

                    {"activity":"Coding Sprint Begins","time":"11:30 AM"},
                    {"activity":"Lunch Break","time":"01:00 PM"},
                    {"activity":"Mentor Review Session","time":"02:30 PM"},
                    {"activity":"Progress Evaluation","time":"04:00 PM"},
                    {"activity":"Dinner Arrangements","time":"06:00 PM"},
                    {"activity":"Overnight Development","time":"09:00 PM"},
                    {"activity":"Accommodation Arrangements","time":"10:00 PM"}
                ],

                "day_2":[

                    {"activity":"Breakfast","time":"08:00 AM"},
                    {"activity":"Final Development","time":"09:00 AM"},
                    {"activity":"Project Submission","time":"01:00 PM"},
                    {"activity":"Demo Session","time":"02:30 PM"},
                    {"activity":"Jury Evaluation","time":"04:00 PM"},
                    {"activity":"Winner Announcement","time":"05:00 PM"},
                    {"activity":"Closing Ceremony","time":"06:00 PM"}
                ]
            }

        # =====================
        # FASHION SHOW
        # =====================

        elif "fashion" in event_type:

            return {
                "day_1":[
                {"activity":"Model Registration","time":"01:00 PM"},
                {"activity":"Makeup Session","time":"03:00 PM"},
                {"activity":"Runway Rehearsal","time":"05:00 PM"},
                {"activity":"VIP Reception","time":"07:00 PM"},
                {"activity":"Designer Preview Show","time":"08:00 PM"}
            ],

              "day_2":[

                {"activity":"Media Interaction","time":"02:00 PM"},
                {"activity":"Designer Showcase","time":"04:00 PM"},
                {"activity":"Fashion Show Launch","time":"06:00 PM"},
                {"activity":"Grand Runway Event","time":"08:00 PM"},
                {"activity":"Awards Ceremony","time":"10:00 PM"}
                ]
            }

        # =====================
        # WEDDING
        # =====================

        elif "wedding" in event_type:

            return {
                "day_1":[
                    {"activity":"Venue Decoration","time":"08:00 AM"},
                    {"activity":"Family Gathering","time":"10:00 AM"},
                    {"activity":"Pre-Wedding Rituals","time":"01:00 PM"},
                    {"activity":"Mehendi Ceremony","time":"05:00 PM"},
                    {"activity":"Sangeet Night","time":"08:00 PM"}
                ],

                "day_2":[

                    {"activity":"Guest Arrival","time":"09:00 AM"},
                    {"activity":"Wedding Ceremony","time":"11:00 AM"},
                    {"activity":"Blessing Ceremony","time":"01:00 PM"},
                    {"activity":"Lunch Service","time":"02:00 PM"},
                    {"activity":"Reception","time":"06:00 PM"},
                    {"activity":"Event Closing","time":"09:00 PM"}
                ]
            }

        # =====================
        # DEFAULT
        # =====================

        else:

            return {
                "event":[
                    {"activity":"Day 1 Opening","time":"09:00 AM"},
                    {"activity":"Main Activities","time":"11:00 AM"},
                    {"activity":"Networking","time":"03:00 PM"},
                    {"activity":"Day 2 Main Event","time":"10:00 AM"},
                    {"activity":"Awards","time":"03:00 PM"},
                    {"activity":"Closing Ceremony","time":"05:00 PM"}
                ]
            }

   # =====================
    # 3 DAYS
    # =====================

    elif "3 days" in duration:

        # =====================
        # MUSIC FESTIVAL
        # =====================

        if "music" in event_type or "festival" in event_type:

            return {
                "day_1":[
                    {"activity":"Day 1 Gate Opening","time":"05:00 PM"},
                    {"activity":"Opening Artists","time":"06:00 PM"},
                    {"activity":"Main Stage Performance","time":"09:00 PM"}
                ],
                "day_2":[

                    {"activity":"Day 2 Gate Opening","time":"05:00 PM"},
                    {"activity":"DJ Festival","time":"07:00 PM"},
                    {"activity":"Headliner Concert","time":"10:00 PM"}
                ],

                "day_3":[

                    {"activity":"Day 3 Gate Opening","time":"05:00 PM"},
                    {"activity":"Special Guest Performance","time":"08:00 PM"},
                    {"activity":"Grand Finale Concert","time":"10:00 PM"},
                    {"activity":"Festival Closing","time":"11:30 PM"}
                ]
            }

        # =====================
        # GAMING TOURNAMENT
        # =====================

        elif "gaming" in event_type or "tournament" in event_type:

            return {
                "day_1":[
                    {"activity":"Player Registration","time":"10:00 AM"},
                    {"activity":"Group Stage Matches","time":"11:00 AM"},
                    {"activity":"Streaming Launch","time":"02:00 PM"}
                ],

                "day_2":[

                    {"activity":"Qualifier Matches","time":"10:00 AM"},
                    {"activity":"Quarter Finals","time":"02:00 PM"},
                    {"activity":"Community Events","time":"06:00 PM"}

                ],

                "day_3":[

                    {"activity":"Semi Finals","time":"11:00 AM"},
                    {"activity":"Grand Finals","time":"04:00 PM"},
                    {"activity":"Prize Distribution","time":"07:00 PM"},
                    {"activity":"Champion Ceremony","time":"08:00 PM"}
                ]
            }

        # =====================
        # CONFERENCE
        # =====================

        elif "conference" in event_type:

            return {
                "day_1":[
                    {"activity":"Registration","time":"08:00 AM"},
                    {"activity":"Opening Keynote","time":"09:00 AM"},
                    {"activity":"Industry Sessions","time":"11:00 AM"}
                ],

                "day_2":[

                    {"activity":"Technical Workshops","time":"09:00 AM"},
                    {"activity":"Panel Discussions","time":"01:00 PM"},
                    {"activity":"Networking Dinner","time":"06:00 PM"}
                ],

                "day_3":[

                    {"activity":"Startup Showcase","time":"09:00 AM"},
                    {"activity":"Investor Connect","time":"12:00 PM"},
                    {"activity":"Closing Keynote","time":"03:00 PM"},
                    {"activity":"Awards Ceremony","time":"05:00 PM"}
                ]
            }

        # =====================
        # HACKATHON
        # =====================

        elif "hackathon" in event_type:

            return {
                "day_1":[
                    {"activity":"Registration","time":"09:00 AM"},
                    {"activity":"Problem Statement Release","time":"10:00 AM"},
                    {"activity":"Team Formation","time":"11:00 AM"},
                    {"activity":"Coding Sprint Begins","time":"12:00 PM"}
                ],

                "day_2":[

                    {"activity":"Development Sprint","time":"09:00 AM"},
                    {"activity":"Mentor Reviews","time":"02:00 PM"},
                    {"activity":"Prototype Testing","time":"07:00 PM"}
                ],

                "day_3":[

                    {"activity":"Project Submission","time":"10:00 AM"},
                    {"activity":"Demo Presentations","time":"01:00 PM"},
                    {"activity":"Jury Evaluation","time":"03:00 PM"},
                    {"activity":"Winner Announcement","time":"05:00 PM"}
                ]
            }

        # =====================
        # FASHION SHOW
        # =====================

        elif "fashion" in event_type:

            return {
                "day_1":[
                    {"activity":"Model Check-in","time":"02:00 PM"},
                    {"activity":"Makeup Sessions","time":"04:00 PM"},
                    {"activity":"Runway Rehearsal","time":"07:00 PM"}
                ],

                "day_2":[

                    {"activity":"Media Showcase","time":"03:00 PM"},
                    {"activity":"Designer Preview","time":"06:00 PM"},
                    {"activity":"VIP Fashion Night","time":"08:00 PM"}
                ],

                "day_3":[
        

                    {"activity":"Grand Fashion Show","time":"06:00 PM"},
                    {"activity":"Designer Awards","time":"09:00 PM"},
                    {"activity":"Press Conference","time":"10:00 PM"}
                ]
            }

        # =====================
        # WEDDING
        # =====================

        elif "wedding" in event_type:

            return {
                "day_1":[
                    {"activity":"Venue Decoration","time":"09:00 AM"},
                    {"activity":"Family Gathering","time":"12:00 PM"},
                    {"activity":"Mehendi Ceremony","time":"05:00 PM"},
                    {"activity":"Sangeet Night","time":"08:00 PM"}

                ],

                "day_2":[

                    {"activity":"Haldi Ceremony","time":"10:00 AM"},
                    {"activity":"Guest Welcome","time":"01:00 PM"},
                    {"activity":"Pre-Wedding Celebration","time":"07:00 PM"}
                ],

                "day_3":[

                    {"activity":"Wedding Ceremony","time":"11:00 AM"},
                    {"activity":"Blessing Ceremony","time":"01:00 PM"},
                    {"activity":"Reception","time":"06:00 PM"},
                    {"activity":"Event Closing","time":"10:00 PM"}
                ]
            }

        # =====================
        # DEFAULT
        # =====================

        else:

            return {
                "event":[
                    {"activity":"Day 1 Opening","time":"09:00 AM"},
                    {"activity":"Main Activities","time":"11:00 AM"},
                    {"activity":"Networking","time":"04:00 PM"},

                    {"activity":"Day 2 Workshops","time":"10:00 AM"},
                    {"activity":"Team Sessions","time":"02:00 PM"},

                    {"activity":"Day 3 Final Event","time":"10:00 AM"},
                    {"activity":"Awards Ceremony","time":"03:00 PM"},
                    {"activity":"Closing Ceremony","time":"05:00 PM"}
                ]
            }
        
    return {
        "event": [
            {
                "activity": "Guest Arrival",
                "time": "09:00 AM"
            },
            {
                "activity": "Main Event",
                "time": "10:00 AM"
            },
            {
                "activity": "Closing Ceremony",
                "time": "11:00 AM"
            }
        ]
    }


def timeline_agent(data):

    if "execution_flow" not in data:

        data["execution_flow"] = []

    data["execution_flow"].append(
        "timeline_agent"
    )

    classification = data.get(
        "classification",
        {}
    )

    event_type = data.get(
        "event_type",
        ""
    )

    event_duration = data.get(
        "event_duration",
        "4 Hours"
    )

    requirements = data.get(
     "requirements",
         ""
    )
    guests = int(
        data.get(
            "guests",
            100
        )
    )

    # =========================
    # EVENT SCALE
    # =========================

    event_scale = "small"

    if guests >= 1500:

        event_scale = "mega"

    elif guests >= 700:

        event_scale = "large"

    elif guests >= 250:

        event_scale = "medium"

    # =========================
    # SMART TIMELINE
    # =========================

    smart_timeline = build_duration_based_timeline(

        event_type,

        event_duration,

        requirements
    )

    print("EVENT TYPE:", event_type)
    print("SMART TIMELINE:", smart_timeline)
    
    data["timeline"] = smart_timeline

    # =========================
    # TOOL DATA
    # =========================

    tool_data = generate_timeline_plan(
        event_type
    )

    # =========================
    # PROMPT
    # =========================

    prompt = PromptTemplate(

        input_variables=[

            "event_type",
            "date",
            "classification",
            "tool_data",
            "smart_timeline",
            "event_scale",
            "event_duration",
            "requirements"
        ],

        template="""
You are an advanced AI event timeline planner.

Return ONLY valid JSON.
Do NOT return explanations.
Do NOT use markdown.

Event Type: {event_type}

Event Duration: {event_duration}

Requirements:
{requirements}

Date: {date}

Event Scale: {event_scale}

Classification:
{classification}

Timeline Tool:
{tool_data}

Smart Timeline:
{smart_timeline}

Improve the timeline intelligently.

Add:
- Maintain chronological order
- Keep all activities realistic
- Improve execution flow
- Add operational coordination where useful
- Add logistics and attendee management activities
- Avoid duplicate tasks
- Avoid generic activities
- Keep timings practical
- Return only valid JSON
- Respect event duration
- Only add Reception when appropriate for the event type.
- Do not add Farewell Ceremony unless requested
- Do not add Dinner unless requested
- Keep timeline inside duration

IMPORTANT:

For Music Festivals:
- Audience gates should open after 4 PM
- Main performances should happen in evening/night
- Headliner performances should occur after sunset
- Do not schedule audience activities before noon

STRICT RULES:

- If duration is 2 Hours, total timeline span must not exceed 120 minutes
- If duration is 4 Hours, total timeline span must not exceed 240 minutes
- If duration is Half Day, keep activities within 6 hours
- If duration is Full Day, keep activities within 12 hours
- If duration is 2 Days, distribute activities across Day 1 and Day 2
- If duration is 3 Days, distribute activities across Day 1, Day 2 and Day 3

DO NOT create activities outside the allowed duration.

Return format:

{{
  "event": []
}}
"""
    )

    try:

        result = run_agent_prompt(

            prompt,

            {

                "event_type":
                    event_type,

                "event_duration":
                    event_duration,

                "requirements":
                     requirements,

                "date":
                    data.get(
                        "event_date"
                    ),

                "classification":
                    str(classification),

                "tool_data":
                    str(tool_data),

                "smart_timeline":
                    str(smart_timeline),

                "event_scale":
                    event_scale
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


        if not isinstance(parsed, dict):
            parsed = smart_timeline

        if len(parsed.keys()) == 0:
             parsed = smart_timeline


        data["timeline"] = parsed

    except Exception as e:

        data["timeline"] = smart_timeline

        data["timeline"]["error"] = str(e)

    print("\n========== FINAL TIMELINE ==========")
    print(json.dumps(data["timeline"], indent=2))
    print("====================================\n")

    total_activities = 0

    for value in data["timeline"].values():

        if isinstance(value, list):

            total_activities += len(value)

    print(
        "FINAL TIMELINE ACTIVITIES:",
        total_activities
    )

    return data

