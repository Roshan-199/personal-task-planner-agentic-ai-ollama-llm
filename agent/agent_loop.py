from agent.planner import plan_steps
from agent.executor import execute_steps
from agent.memory import update_memory

def run_agent(state):
    """
    This function is used to plan, execute, observe, store and repeat.
    
    """

    state.plan = plan_steps(state.goal)

    for step in state.plan:
        state.current_step = step

        result = execute_steps(step)
        update_memory(result)

        state.completed_steps.append(step)
    
    state.done = True
    return state