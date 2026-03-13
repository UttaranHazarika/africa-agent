# AFRICA – Autonomous Financial Risk & Credit Decision Agent

AFRICA is a multi-agent AI system that evaluates loan applications by combining classical machine learning, policy-based rules, vector memory retrieval, and LLM reasoning. The goal is to demonstrate how an **agentic AI system** can make structured, explainable credit decisions while maintaining governance and auditability.

## Overview
The system processes loan applications through a sequence of agents orchestrated with **LangGraph**. Each agent performs a specific task and passes structured outputs to the next stage.

Workflow:
User Request → FastAPI API → LangGraph Workflow → Risk Agent → Policy Agent → Memory Agent → Decision Agent → Governance Logging → API Response

## Agents
Risk Scoring Agent  
Computes a credit risk probability using a classical machine learning model (Logistic Regression).

Policy & Compliance Agent  
Applies rule-based checks such as credit score thresholds, loan-to-income ratios, and minimum age requirements.

Memory Agent  
Retrieves similar historical credit cases from a **Chroma vector database** to provide contextual decision support.

Decision Reasoning Agent  
Uses an LLM to synthesize risk scores, policy outcomes, and retrieved cases to produce a structured decision and explanation.

Governance Agent  
Logs decision traces and maintains audit-ready records.

## Technology Stack
Backend: FastAPI  
Agent Framework: LangChain (>1.0) and LangGraph (>1.0)  
Vector Database: ChromaDB  
Machine Learning: Scikit-learn  
Tracing: LangSmith (optional)  
Development Environment: GitHub Codespaces  
Deployment Target: AWS ECS Fargate

## Project Structure
africa-agent  
│  
├── app  
│   ├── main.py  
│   ├── config.py  
│   ├── schemas.py  
│   ├── logging_config.py  
│   │  
│   ├── agents  
│   │   ├── risk_agent.py  
│   │   ├── policy_agent.py  
│   │   ├── memory_agent.py  
│   │   ├── decision_agent.py  
│   │   └── governance_agent.py  
│   │  
│   ├── graph  
│   │   └── workflow.py  
│   │  
│   └── services  
│       └── vector_store.py  
│  
├── tests  
│   └── evaluation.py  
│  
├── requirements.txt  
├── .env.example  
├── .gitignore  
└── README.md

## Development Environment
The project is designed for **GitHub Codespaces**, enabling a cloud-based development workflow.

Steps:
1. Create a GitHub repository.
2. Open the repository in GitHub Codespaces.
3. Install dependencies.
4. Run the FastAPI server.

## Installation
Install dependencies:

pip install -r requirements.txt

Create environment variables file:

cp .env.example .env

Add your API keys to `.env`.

## Running the Application
Start the API server:

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

Codespaces automatically exposes port 8000.

## Example API Request
Endpoint: POST /assess

Example input:

{
  "applicant_id": "A123",
  "age": 30,
  "income": 50000,
  "credit_score": 680,
  "existing_debt": 8000,
  "loan_amount": 12000,
  "employment_years": 4
}

Example response:

{
  "decision": "approve",
  "explanation": "Applicant demonstrates moderate risk with sufficient income stability.",
  "llm_confidence": 0.84
}

## Evaluation
Run test scenarios:

python tests/evaluation.py

The evaluation script sends sample loan applications through the workflow to verify agent behavior.

## Deployment
The application is designed to run as a containerized API.

Recommended deployment architecture:

Docker Container → AWS ECS Fargate → Public API Endpoint

Infrastructure can be deployed temporarily for testing and destroyed after use to minimize cost.

## Security
The repository excludes sensitive files using `.gitignore`.

Do not commit:
.env files  
API keys  
Local databases  
Log files

## Future Enhancements
Potential improvements include:

PostgreSQL decision history  
Redis caching  
Prometheus metrics  
CI/CD pipeline  
Model routing for cost optimization  
Human-in-the-loop escalation for high-risk cases

## License
This project is intended for research and educational use.
