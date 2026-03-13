from pydantic import BaseModel
from typing import Literal


class LoanApplication(BaseModel):

    applicant_id: str
    age: int
    income: float
    credit_score: int
    existing_debt: float
    loan_amount: float
    employment_years: int


class DecisionOutput(BaseModel):

    decision: Literal["approve","reject","request_info"]
    explanation: str
    confidence_level: float

