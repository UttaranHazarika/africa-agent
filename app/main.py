from fastapi import FastAPI
from app.schemas import LoanApplication
from app.graph.workflow import run_workflow

app=FastAPI(title="AFRICA Agent API")


@app.post("/assess")
def assess_credit(application:LoanApplication):

    return run_workflow(application.dict())
