from app.services.vector_store import retrieve_cases

def memory_agent(application):

    query=str(application)

    return retrieve_cases(query)
