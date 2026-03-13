import uuid
from langgraph.graph import StateGraph,END

from app.agents.risk_agent import risk_agent
from app.agents.policy_agent import policy_agent
from app.agents.memory_agent import memory_agent
from app.agents.decision_agent import decision_agent
from app.agents.governance_agent import governance_agent


class State(dict):
    pass


def risk_node(state):

    risk,conf=risk_agent.run(state["application"])

    return {"risk_score":risk,"model_confidence":conf}


def policy_node(state):

    status=policy_agent(state["application"])

    return {"policy_status":status}


def memory_node(state):

    return {"cases":memory_agent(state["application"])}


def decision_node(state):

    result=decision_agent(state)

    return {
        "decision":result.decision,
        "explanation":result.explanation,
        "llm_confidence":result.confidence_level
    }


def governance_node(state):

    governance_agent(state["trace_id"],state["decision"])

    return {}


builder=StateGraph(State)

builder.add_node("risk",risk_node)
builder.add_node("policy",policy_node)
builder.add_node("memory",memory_node)
builder.add_node("decision",decision_node)
builder.add_node("governance",governance_node)

builder.set_entry_point("risk")

builder.add_edge("risk","policy")
builder.add_edge("policy","memory")
builder.add_edge("memory","decision")
builder.add_edge("decision","governance")
builder.add_edge("governance",END)

graph=builder.compile()


def run_workflow(application):

    state={
        "trace_id":str(uuid.uuid4()),
        "application":application
    }

    return graph.invoke(state)
