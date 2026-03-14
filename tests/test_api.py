from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_assess_endpoint():

    payload = {
        "applicant_id":"T100",
        "age":30,
        "income":50000,
        "credit_score":680,
        "existing_debt":8000,
        "loan_amount":10000,
        "employment_years":5
    }

    response = client.post("/assess", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "decision" in data
    assert "explanation" in data
