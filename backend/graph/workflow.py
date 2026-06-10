from langgraph.graph import StateGraph, END

from agents.supervisor_agent import supervisor_agent
from agents.event_classifier_agent import event_classifier_agent
from agents.vendor_agent import vendor_agent
from agents.venue_agent import venue_agent
from agents.food_agent import food_agent
from agents.budget_agent import budget_agent
from agents.decoration_agent import decoration_agent
from agents.timeline_agent import timeline_agent
from agents.security_agent import security_agent
from agents.entertainment_agent import entertainment_agent


# =========================
# EXECUTION TRACKER
# =========================

def update_execution_state(
    state,
    agent_name
):

    if "agent_flow" not in state:

        state["agent_flow"] = []

    state["agent_flow"].append(
        agent_name
    )

    return state


# =========================
# SECURITY ROUTER
# =========================

def route_security(state):

    update_execution_state(
        state,
        "security_router"
    )

    shared_memory = state.get(
        "shared_memory",
        {}
    )

    if shared_memory.get(
        "needs_security",
        False
    ):

        return "security"

    if shared_memory.get(
        "needs_entertainment",
        False
    ):

        return "entertainment"

    return "timeline"


# =========================
# ENTERTAINMENT ROUTER
# =========================

def route_entertainment(state):

    update_execution_state(
        state,
        "entertainment_router"
    )

    shared_memory = state.get(
        "shared_memory",
        {}
    )

    needs_entertainment = shared_memory.get(
        "needs_entertainment",
        False
    )

    if needs_entertainment:

        return "entertainment"

    return "timeline"


# =========================
# WORKFLOW BUILDER
# =========================

def build_workflow():

    workflow = StateGraph(dict)

    # =========================
    # NODES
    # =========================

    workflow.add_node(
        "supervisor",
        supervisor_agent
    )

    workflow.add_node(
        "classifier",
        event_classifier_agent
    )
    workflow.add_node(
        "vendor",
        vendor_agent
    )

    workflow.add_node(
        "venue",
        venue_agent
    )

    workflow.add_node(
        "food",
        food_agent
    )

    workflow.add_node(
        "budget",
        budget_agent
    )

    workflow.add_node(
        "decoration",
        decoration_agent
    )

    workflow.add_node(
        "security",
        security_agent
    )

    workflow.add_node(
        "entertainment",
        entertainment_agent
    )

    workflow.add_node(
        "timeline",
        timeline_agent
    )

    # =========================
    # ENTRY
    # =========================

    workflow.set_entry_point(
        "supervisor"
    )

    # =========================
    # MAIN FLOW
    # =========================

    workflow.add_edge(
        "supervisor",
        "classifier"
    )

    workflow.add_edge(
        "classifier",
        "vendor"
    )

    workflow.add_edge(
        "vendor",
        "venue"
    )

    workflow.add_edge(
        "venue",
        "food"
    )

    workflow.add_edge(
        "food",
        "budget"
    )

    workflow.add_edge(
        "budget",
        "decoration"
    )

    # =========================
    # SECURITY ROUTING
    # =========================

    workflow.add_conditional_edges(

        "decoration",

        route_security,

        {

            "security":
                "security",

            "entertainment":
                "entertainment",

            "timeline":
                "timeline"
        }
    )

    # =========================
    # ENTERTAINMENT ROUTING
    # =========================

    workflow.add_conditional_edges(

        "security",

        route_entertainment,

        {

            "entertainment":
                "entertainment",

            "timeline":
                "timeline"
        }
    )

    # =========================
    # FINAL FLOW
    # =========================

    workflow.add_edge(
        "entertainment",
        "timeline"
    )

    workflow.add_edge(
        "timeline",
        END
    )

    workflow = workflow.compile()

    print(
        "Dynamic LangGraph workflow initialized"
    )

    return workflow