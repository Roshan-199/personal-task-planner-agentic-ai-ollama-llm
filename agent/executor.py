from tools.basic_tools import study_tool, practice_tool

def execute_steps(step: str):
    if "practice" in step:
        return practice_tool(step)
    return study_tool(step)