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

## License
This project is intended for research and educational use.
