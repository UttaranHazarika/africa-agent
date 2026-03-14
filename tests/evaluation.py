from app.graph.workflow import run_workflow


def test_evaluation_cases():

    test_cases = [

        {
            "input": {
                "applicant_id":"E100",
                "age":40,
                "income":90000,
                "credit_score":750,
                "existing_debt":2000,
                "loan_amount":15000,
                "employment_years":10
            },
            "expected":"approve"
        },

        {
            "input": {
                "applicant_id":"E200",
                "age":25,
                "income":30000,
                "credit_score":500,
                "existing_debt":10000,
                "loan_amount":15000,
                "employment_years":1
            },
            "expected":"reject"
        },

        {
            "input": {
                "applicant_id":"E300",
                "age":30,
                "income":50000,
                "credit_score":650,
                "existing_debt":8000,
                "loan_amount":12000,
                "employment_years":4
            },
            "expected":None
        }

    ]

    for case in test_cases:

        result = run_workflow(case["input"])

        assert "decision" in result

        if case["expected"]:
            assert result["decision"] == case["expected"]
