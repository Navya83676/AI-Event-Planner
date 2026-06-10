from tools.vendor_tool import (
    get_vendor_recommendations
)


def vendor_agent(state):

    print(
        "\n===== VENDOR AGENT ====="
    )

    # =========================
    # EXECUTION FLOW
    # =========================

    if "execution_flow" not in state:

        state["execution_flow"] = []

    state["execution_flow"].append(
        "vendor_agent"
    )

    # =========================
    # EVENT DATA
    # =========================

    event_type = str(
        state.get(
            "event_type",
            ""
        )
    )

    event_name = str(
        state.get(
            "event_name",
            ""
        )
    )

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
    # GET VENDORS
    # =========================


    print("Event Type:", event_type)
    print("Event Name:", event_name)
    print("Combined:", f"{event_type} {event_name}")
    
    vendors = (
        get_vendor_recommendations(
            event_type=f"{event_type} {event_name}",
            guests=guests,
            budget=budget
        )
    )

    # =========================
    # SAVE TO STATE
    # =========================

    state["vendors"] = vendors

    print(
        f"Generated {len(vendors)} vendor recommendations"
    )
    print(
    "Vendor Agent Executed"
    )

    return state