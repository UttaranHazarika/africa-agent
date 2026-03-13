from app.logging_config import logger

def governance_agent(trace_id,decision):

    logger.info(f"TRACE={trace_id}")
    logger.info(f"DECISION={decision}")
