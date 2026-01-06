from llm.llm_client import call_llm
from utils.parser import parse_steps

def plan_steps(goal: str):
    """
    This function is used to generate the step-by-step plan.
    """

    prompt = f"""
    You are an AI Planning Agent.

    Break the following goal into clear, actionable steps.
    Return only a numbered list.

    Goal: {goal}
    """

    llm_response = call_llm(prompt)
    return parse_steps(llm_response)