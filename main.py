from agent.state import AgentState
from agent.agent_loop import run_agent

if __name__ == "__main__":
    goal = "Prepare for Pyspark interview in 7 days"
    
    state = AgentState(goal)
    final_state = run_agent(state)

    print("\n Plan")
    for step in state.plan:
        print("-",step)
    
    print("\n Memory")
    for mem in state.memory:
        print("-", mem)