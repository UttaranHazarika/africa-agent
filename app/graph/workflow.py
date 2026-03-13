import uuid
from typing import TypedDict, Optional, List

from langgraph.graph import StateGraph, END

from app.agents.risk_agent import risk_agent
from app.agents.policy_agent import policy_agent
from app.agents.memory_agent import memory_agent
from app.agents.decision_agent import decision_agent
from app.agents.governance_agent import governance_agent


# -------- STATE DEFINITION --------

class State(TypedDict, total=False):

    trace_id: str
    application: dict

    risk_score: float
    model_confidence: float

    policy_status: str

    cases: List[str]

    decision: str
    explanation: str
    llm_confidence: float


# -------- AGENT NODES --------

def risk_node(state: State):

    risk, conf = risk_agent.run(state["application"])

    return {
        "risk_score": risk,
        "model_confidence": conf
    }


def policy_node(state: State):

    status = policy_agent(state["application"])

    return {
        "policy_status": status
    }


def memory_node(state: State):

    cases = memory_agent(state["application"])

    return {
        "cases": cases
    }


def decision_node(state: State):

    result = decision_agent(state)

    return {
        "decision": result.decision,
        "explanation": result.explanation,
        "llm_confidence": result.confidence_level
    }


def governance_node(state: State):

    governance_agent(state["trace_id"], state["decision"])

    return {}


# -------- GRAPH CONSTRUCTION --------

builder = StateGraph(State)

builder.add_node("risk", risk_node)
builder.add_node("policy", policy_node)
builder.add_node("memory", memory_node)
builder.add_node("decision", decision_node)
builder.add_node("governance", governance_node)

builder.set_entry_point("risk")

builder.add_edge("risk", "policy")
builder.add_edge("policy", "memory")
builder.add_edge("memory", "decision")
builder.add_edge("decision", "governance")
builder.add_edge("governance", END)

graph = builder.compile()


# -------- WORKFLOW ENTRY --------

def run_workflow(application: dict):

    state = {
        "trace_id": str(uuid.uuid4()),
        "application": application
    }

    result = graph.invoke(state)

    return result

