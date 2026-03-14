from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import LoanApplication
from app.graph.workflow import run_workflow

app = FastAPI(title="AFRICA Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/assess")
def assess_credit(application: LoanApplication):

    return run_workflow(application.model_dump())


