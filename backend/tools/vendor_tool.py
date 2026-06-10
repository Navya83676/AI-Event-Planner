def get_vendor_recommendations(
    event_type="",
    guests=0,
    budget=0
):

    event_type = str(
        event_type
    ).lower()

    if guests <= 100:
        vendor_count = 6

    elif guests <= 500:
        vendor_count = 10

    else:
         vendor_count = 12

    # =========================
    # WEDDING
    # =========================

    if (
        "wedding" in event_type
        or
        "marriage" in event_type
    ):

        vendors = [

            {
                "id": "wedding-vendor-1",
                "name": "Royal Caterers",
                "category": "Catering",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                "id": "wedding-vendor-2",
                "name": "Elite Decor Studio",
                "category": "Decoration",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "wedding-vendor-3",
                "name": "Grand Palace Venues",
                "category": "Venue",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                "id": "wedding-vendor-4",
                "name": "Wedding Lens Pro",
                "category": "Photography",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "wedding-vendor-5",
                "name": "Secure Events India",
                "category": "Security",
                "rating": 4.7,
                "status": "Confirmed"
            },

            {
                "id": "wedding-vendor-6",
                "name": "Dream Wedding Planners",
                "category": "Planning",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                 "id": "wedding-vendor-7",
                 "name": "Luxury Bridal Makeup",
                "category": "Makeup",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                 "id": "wedding-vendor-8",
                 "name": "Live Music Orchestra",
                 "category": "Entertainment",
                 "rating": 4.7,
                 "status": "Confirmed"
            },
            {
                "id": "wedding-vendor-9",
                "name": "Premium Florists",
                "category": "Floral Design",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                "id": "wedding-vendor-10",
                "name": "Luxury Transport",
                "category": "Transportation",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "wedding-vendor-11",
                "name": "Wedding Video Studio",
                "category": "Videography",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                "id": "wedding-vendor-12",
                "name": "LED Event Lighting",
                "category": "Lighting",
                "rating": 4.8,
                "status": "Confirmed"
            }

        ]
        return vendors[:vendor_count]
    
    # =========================
    # CORPORATE / CONFERENCE / AI SUMMIT
    # =========================

    elif (
        "conference" in event_type
        or "corporate" in event_type
        or "business" in event_type
        or "startup" in event_type
        or "ai summit" in event_type
        or "summit" in event_type
    ):

        # AI SUMMIT
        if (
            "ai summit" in event_type
            or "summit" in event_type
        ):

            vendors = [

                {
                    "id": "ai-vendor-1",
                    "name": "AI Conference Center",
                    "category": "Venue",
                    "rating": 4.9,
                    "status": "Confirmed"
                },

                {
                    "id": "ai-vendor-2",
                    "name": "AV Tech Systems",
                    "category": "Audio Visual",
                    "rating": 4.8,
                    "status": "Confirmed"
                },

                {
                    "id": "ai-vendor-3",
                    "name": "Corporate Catering Hub",
                    "category": "Catering",
                    "rating": 4.7,
                    "status": "Confirmed"
                },

                {
                    "id": "ai-vendor-4",
                    "name": "Event Registration Pro",
                    "category": "Registration",
                    "rating": 4.8,
                    "status": "Confirmed"
                },

                {
                    "id": "ai-vendor-5",
                    "name": "Media Coverage Team",
                    "category": "Photography",
                    "rating": 4.7,
                    "status": "Confirmed"
                },

                {
                    "id": "ai-vendor-6",
                    "name": "Tech Expo Booths",
                    "category": "Exhibition",
                    "rating": 4.9,
                    "status": "Confirmed"
                },

                {
                    "id": "ai-vendor-7",
                    "name": "Cloud Infrastructure Pro",
                    "category": "Cloud Services",
                    "rating": 4.8,
                    "status": "Confirmed"
                },

                {
                    "id": "ai-vendor-8",
                    "name": "AI Speaker Management",
                    "category": "Speaker Coordination",
                    "rating": 4.9,
                    "status": "Confirmed"
                },

                                {
                    "id": "ai-vendor-9",
                    "name": "Cyber Security Experts",
                    "category": "Security",
                    "rating": 4.8,
                    "status": "Confirmed"
                },

                {
                    "id": "ai-vendor-10",
                    "name": "Innovation Stage Design",
                    "category": "Stage Design",
                    "rating": 4.9,
                    "status": "Confirmed"
                },

                {
                    "id": "ai-vendor-11",
                    "name": "VIP Guest Management",
                    "category": "VIP Services",
                    "rating": 4.8,
                    "status": "Confirmed"
                },

                {
                    "id": "ai-vendor-12",
                    "name": "AI Networking Lounge",
                    "category": "Networking",
                    "rating": 4.9,
                    "status": "Confirmed"
                }

            ]

            return vendors[:vendor_count]

        else:

            vendors = [

                {
                    "id": "corporate-vendor-1",
                    "name": "Business Event Solutions",
                    "category": "Management",
                    "rating": 4.8,
                    "status": "Confirmed"
                },

                {
                    "id": "corporate-vendor-2",
                    "name": "AV Tech Systems",
                    "category": "Audio Visual",
                    "rating": 4.9,
                    "status": "Confirmed"
                },

                {
                    "id": "corporate-vendor-3",
                    "name": "Corporate Catering Hub",
                    "category": "Catering",
                    "rating": 4.7,
                    "status": "Confirmed"
                },

                {
                    "id": "corporate-vendor-4",
                    "name": "Conference Media Crew",
                    "category": "Photography",
                    "rating": 4.6,
                    "status": "Confirmed"
                },

                {
                    "id": "corporate-vendor-5",
                    "name": "Stage Vision Pro",
                    "category": "Stage Setup",
                    "rating": 4.8,
                    "status": "Confirmed"
                },

                {
                    "id": "corporate-vendor-6",
                    "name": "Networking Lounge Experts",
                    "category": "Networking",
                    "rating": 4.8,
                    "status": "Confirmed"
                },

                {
                    "id": "corporate-vendor-7",
                    "name": "Corporate Security Group",
                    "category": "Security",
                    "rating": 4.7,
                    "status": "Confirmed"
                },

                {
                    "id": "corporate-vendor-8",
                    "name": "Smart Registration Systems",
                    "category": "Registration",
                    "rating": 4.9,
                    "status": "Confirmed"
                },

                                {
                    "id": "corporate-vendor-9",
                    "name": "VIP Executive Services",
                    "category": "VIP Management",
                    "rating": 4.8,
                    "status": "Confirmed"
                },

                {
                    "id": "corporate-vendor-10",
                    "name": "Corporate Branding Studio",
                    "category": "Branding",
                    "rating": 4.8,
                    "status": "Confirmed"
                },

                {
                    "id": "corporate-vendor-11",
                    "name": "Business Lounge Experts",
                    "category": "Hospitality",
                    "rating": 4.9,
                    "status": "Confirmed"
                },

                {
                    "id": "corporate-vendor-12",
                    "name": "Live Event Streaming Pro",
                    "category": "Broadcasting",
                    "rating": 4.8,
                    "status": "Confirmed"
                }

            ]

            return vendors[:vendor_count]

    # =========================
    # HACKATHON
    # =========================
    elif (
        "hackathon" in event_type
    ):

             vendors =  [

            {
                "id": "hack-vendor-1",
                "name": "Tech Setup Solutions",
                "category": "Technical Support",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                 "id": "hack-vendor-2",
                 "name": "FoodHub Catering",
                 "category": "Catering",
                "rating": 4.8,
                "status": "Confirmed"
           },

            {
                "id": "hack-vendor-3",
                "name": "SecureGuard Services",
                "category": "Security",
                "rating": 4.7,
                "status": "Confirmed"
            },

            {
                 "id": "hack-vendor-4",
                "name": "Registration Experts",
                 "category": "Registration",
                 "rating": 4.8,
                 "status": "Confirmed"
             },

            {
                "id": "hack-vendor-5",
                "name": "Tech Rental Systems",
                "category": "Equipment",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                "id": "hack-vendor-6",
                "name": "Cloud Infrastructure Pro",
                "category": "Cloud Services",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                 "id": "hack-vendor-7",
                "name": "Internet Backbone Solutions",
                "category": "Networking",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                "id": "hack-vendor-8",
                 "name": "Live Coding Arena",
                "category": "Stage Setup",
                "rating": 4.8,
                "status": "Confirmed"
            },

                        {
                "id": "hack-vendor-9",
                "name": "AI Mentor Network",
                "category": "Mentorship",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                "id": "hack-vendor-10",
                "name": "DevOps Cloud Labs",
                "category": "DevOps Support",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "hack-vendor-11",
                "name": "Hackathon Media Team",
                "category": "Photography",
                "rating": 4.7,
                "status": "Confirmed"
            },

            {
                "id": "hack-vendor-12",
                "name": "Innovation Awards Hub",
                "category": "Awards & Prizes",
                "rating": 4.8,
                "status": "Confirmed"
            }
        ]
             return vendors[:vendor_count]


    # =========================
    # MUSIC FESTIVAL
    # =========================
    elif (
         "music" in event_type
            or
        "festival" in event_type
    ):

     vendors = [

        {
            "id": "music-vendor-1",
            "name": "SoundWave Systems",
            "category": "Audio",
            "rating": 4.9,
            "status": "Confirmed"
        },

        {
            "id": "music-vendor-2",
            "name": "Stage Masters",
            "category": "Stage Setup",
            "rating": 4.8,
            "status": "Confirmed"
        },

        {
            "id": "music-vendor-3",
            "name": "LightFX Pro",
            "category": "Lighting",
            "rating": 4.8,
            "status": "Confirmed"
        },

        {
            "id": "music-vendor-4",
            "name": "Food Festival Catering",
            "category": "Catering",
            "rating": 4.7,
            "status": "Confirmed"
        },

        {
            "id": "music-vendor-5",
            "name": "Event Security Force",
            "category": "Security",
            "rating": 4.8,
            "status": "Confirmed"
        },

        {
             "id": "music-vendor-6",
            "name": "Artist Management Hub",
            "category": "Artists",
            "rating": 4.8,
            "status": "Confirmed"
        },

        {
              "id": "music-vendor-7",
             "name": "Festival Broadcast Media",
            "category": "Live Streaming",
            "rating": 4.9,
            "status": "Confirmed"
        },

        {
             "id": "music-vendor-8",
             "name": "Crowd Control Experts",
             "category": "Operations",
             "rating": 4.7,
             "status": "Confirmed"
        },
                {
            "id": "music-vendor-9",
            "name": "VIP Lounge Services",
            "category": "VIP Management",
            "rating": 4.8,
            "status": "Confirmed"
        },

        {
            "id": "music-vendor-10",
            "name": "Ticketing Solutions Pro",
            "category": "Ticketing",
            "rating": 4.9,
            "status": "Confirmed"
        },

        {
            "id": "music-vendor-11",
            "name": "Festival Medical Support",
            "category": "Medical Services",
            "rating": 4.8,
            "status": "Confirmed"
        },

        {
            "id": "music-vendor-12",
            "name": "Drone Vision Productions",
            "category": "Videography",
            "rating": 4.9,
            "status": "Confirmed"
        }

    ]
     return vendors[:vendor_count]

    # =========================
    # GAMING
    # =========================

    elif (
        "gaming" in event_type
        or
        "tournament" in event_type
    ):

         vendors = [

            {
                "id": "gaming-vendor-1",
                "name": "ArenaX Gaming",
                "category": "Gaming Setup",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                "id": "gaming-vendor-2",
                "name": "HyperStream",
                "category": "Live Streaming",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "gaming-vendor-3",
                "name": "RGB Stage Works",
                "category": "Lighting",
                "rating": 4.7,
                "status": "Confirmed"
            },

            {
                "id": "gaming-vendor-4",
                "name": "ProSecure Events",
                "category": "Security",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "gaming-vendor-5",
                "name": "Esports Arena Systems",
                "category": "Venue",
                "rating": 4.7,
                "status": "Confirmed"
            },

            {
                "id": "gaming-vendor-6",
                "name": "Tournament Management Pro",
                "category": "Operations",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                 "id": "gaming-vendor-7",
                "name": "UltraNet Fiber",
                "category": "Internet",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                 "id": "gaming-vendor-8",
                "name": "Caster Studios",
                "category": "Broadcasting",
                "rating": 4.8,
                "status": "Confirmed"
            },

                        {
                "id": "gaming-vendor-9",
                "name": "Gaming Hardware Hub",
                "category": "Hardware",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                "id": "gaming-vendor-10",
                "name": "Esports Medical Support",
                "category": "Medical Services",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "gaming-vendor-11",
                "name": "VIP Player Lounge",
                "category": "VIP Management",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "gaming-vendor-12",
                "name": "Tournament Prize Solutions",
                "category": "Awards & Prizes",
                "rating": 4.9,
                "status": "Confirmed"
            }

        ]
         return vendors[:vendor_count]

    # =========================
    # FASHION
    # =========================

    elif (
            "fashion" in event_type
                or
            "runway" in event_type
    ):

          vendors = [

            {
                "id": "fashion-vendor-1",
                "name": "Runway Masters",
                "category": "Stage Design",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                "id": "fashion-vendor-2",
                "name": "Elite Glam Studio",
                "category": "Makeup",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "fashion-vendor-3",
                "name": "Flash Vogue Media",
                "category": "Photography",
                "rating": 4.7,
                "status": "Confirmed"
            },

            {
                "id": "fashion-vendor-4",
                "name": "Luxury Lights",
                "category": "Lighting",
                "rating": 4.8,
                "status": "Confirmed"
            },
            {
                "id": "fashion-vendor-5",
                "name": "VIP Event Security",
                "category": "Security",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "fashion-vendor-6",
                "name": "Elite Model Agency",
                "category": "Models",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                 "id": "fashion-vendor-7",
                "name": "Luxury Runway Productions",
                "category": "Production",
                "rating": 4.8,
                 "status": "Confirmed"
            },

            {
                 "id": "fashion-vendor-8",
                 "name": "Fashion PR Network",
                 "category": "Media",
                 "rating": 4.7,
                "status": "Confirmed"
            },

                        {
                "id": "fashion-vendor-9",
                "name": "Designer Showcase Agency",
                "category": "Designer Management",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                "id": "fashion-vendor-10",
                "name": "VIP Guest Relations",
                "category": "VIP Management",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "fashion-vendor-11",
                "name": "Luxury Backstage Services",
                "category": "Backstage Operations",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "fashion-vendor-12",
                "name": "Fashion Awards Studio",
                "category": "Event Management",
                "rating": 4.9,
                "status": "Confirmed"
            }
        ]
          return vendors[:vendor_count]

    # =========================
    # DEFAULT
    # =========================

    vendors = [

            {
                "id": "default-vendor-1",
                "name": "General Event Management",
                "category": "Management",
                "rating": 4.7,
                "status": "Confirmed"
            },

            {
                "id": "default-vendor-2",
                "name": "Premium Catering Services",
                "category": "Catering",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "default-vendor-3",
                "name": "Event Decor Studio",
                "category": "Decoration",
                "rating": 4.7,
                "status": "Confirmed"
            },

            {
                "id": "default-vendor-4",
                "name": "Event Photography Team",
                "category": "Photography",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "default-vendor-5",
                "name": "Venue Support Services",
                "category": "Venue",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "default-vendor-6",
                "name": "Stage Setup Experts",
                "category": "Stage Setup",
                "rating": 4.7,
                "status": "Confirmed"
            },

            {
                "id": "default-vendor-7",
                "name": "Event Security Group",
                "category": "Security",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "default-vendor-8",
                "name": "Lighting Solutions",
                "category": "Lighting",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "default-vendor-9",
                "name": "Sound Systems Pro",
                "category": "Audio",
                "rating": 4.9,
                "status": "Confirmed"
            },

            {
                "id": "default-vendor-10",
                "name": "VIP Guest Services",
                "category": "VIP Management",
                "rating": 4.8,
                "status": "Confirmed"
            },

            {
                "id": "default-vendor-11",
                "name": "Transportation Services",
                "category": "Transportation",
                "rating": 4.7,
                "status": "Confirmed"
            },

            {
                "id": "default-vendor-12",
                "name": "Event Operations Team",
                "category": "Operations",
                "rating": 4.8,
                "status": "Confirmed"
            }
   ]

    return vendors[:vendor_count]