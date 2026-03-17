from app.agents.risk_agent import risk_agent
from app.agents.policy_agent import policy_agent


def test_risk_agent():

    app = {
        "age":35,
        "income":60000,
        "credit_score":700,
        "existing_debt":5000,
        "loan_amount":15000,
        "employment_years":5
    }

    risk, confidence = risk_agent.run(app)

    assert 0 <= risk <= 1
    assert 0 <= confidence <= 1


def test_policy_agent_allowed():

    app = {
        "age":30,
        "income":60000,
        "credit_score":700,
        "existing_debt":5000,
        "loan_amount":10000,
        "employment_years":5
    }

    result = policy_agent(app)

    assert result == "allowed"


def test_policy_agent_blocked():

    app = {
        "age":17,
        "income":60000,
        "credit_score":700,
        "existing_debt":5000,
        "loan_amount":10000,
        "employment_years":5
    }

    result = policy_agent(app)

    assert result == "blocked"

