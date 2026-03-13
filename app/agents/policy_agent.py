def policy_agent(app):

    if app["loan_amount"] > app["income"]*2:
        return "blocked"

    if app["credit_score"] < 550:
        return "blocked"

    if app["age"] < 18:
        return "blocked"

    return "allowed"
