def generate_security_plan(
    guests,
    event_type=""
):

    guests = int(guests)

    event_type = str(
        event_type
    ).lower()

    # =========================
    # BASE SECURITY LEVEL
    # =========================

    if guests >= 3000:

        security_level = "Critical"
        guards = 80

    elif guests >= 1500:

        security_level = "High"
        guards = 45

    elif guests >= 500:

        security_level = "Medium"
        guards = 20

    else:

        security_level = "Basic"
        guards = 8

    # =========================
    # EVENT INTELLIGENCE
    # =========================

    if (

        "gaming" in event_type or
        "festival" in event_type or
        "concert" in event_type or
        "music" in event_type

    ):

        guards += 20

    elif (

        "fashion" in event_type or
        "runway" in event_type or
        "launch" in event_type or
        "product" in event_type

    ):

        guards += 10

    elif (

        "hackathon" in event_type or
        "conference" in event_type or
        "expo" in event_type or
        "corporate" in event_type

    ):

        guards += 5

    # =========================
    # RETURN PLAN
    # =========================

    return {

        "security_level":
            security_level,

        "guards_required":
            guards,

        "emergency_services":
            "Ambulance and Fire Safety",

        "crowd_management":
            "Dedicated Entry and Exit Control",

        "surveillance":
            "CCTV Monitoring",

        "entry_control":
            "QR Verification System",

        "risk_alert":
            "Standard Risk Monitoring"
    }