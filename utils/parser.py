def parse_steps(llm_response: str):
    """
    Extract the numebered from the LLM response
    """
    steps = []
    for line in llm_response.split("\n"):
        line = line.strip()
        if line and line[0].isdigit():
            steps.append(line.split(".", 1)[1].strip())
        
    return steps