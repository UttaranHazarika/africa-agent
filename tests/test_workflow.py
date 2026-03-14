from app.graph.workflow import run_workflow


def test_workflow_execution():

    application = {
        "applicant_id":"T200",
        "age":40,
        "income":90000,
        "credit_score":750,
        "existing_debt":3000,
        "loan_amount":15000,
        "employment_years":10
    }

    result = run_workflow(application)

    assert "decision" in result
    assert "risk_score" in result
    assert "policy_status" in result
