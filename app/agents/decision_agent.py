from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.schemas import DecisionOutput
from app.config import MODEL_NAME

llm=ChatOpenAI(model=MODEL_NAME,temperature=0)

prompt=ChatPromptTemplate.from_template("""

You are a regulated credit decision agent.

Rules:
If policy_status = blocked → reject
If risk_score > 0.6 → reject
If model_confidence < 0.3 → request_info
Otherwise approve

Application:
{application}

Risk Score:
{risk_score}

Confidence:
{model_confidence}

Policy Status:
{policy_status}

Similar Cases:
{cases}

Return structured JSON.

""")

structured_llm=llm.with_structured_output(DecisionOutput)

chain=prompt|structured_llm


def decision_agent(state):

    return chain.invoke(state)
