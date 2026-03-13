import numpy as np
from sklearn.linear_model import LogisticRegression


class RiskScoringAgent:

    def __init__(self):

        X=np.array([
            [25,40000,650,10000,5000,2],
            [45,120000,750,5000,20000,10],
            [30,30000,600,15000,10000,3],
            [50,90000,800,2000,15000,15]
        ])

        y=np.array([1,0,1,0])

        self.model=LogisticRegression()
        self.model.fit(X,y)

    def run(self,app):

        features=np.array([[
            app["age"],
            app["income"],
            app["credit_score"],
            app["existing_debt"],
            app["loan_amount"],
            app["employment_years"]
        ]])

        risk=self.model.predict_proba(features)[0][1]
        confidence=abs(risk-0.5)*2

        return risk,confidence


risk_agent=RiskScoringAgent()
