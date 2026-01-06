class AgentState:
    """
    This class represents the internal state of the agent.
    Think of this as the agent's 'brain memory'.
    """
    def __init__(self, goal: str):
        self.goal = goal
        self.plan = []
        self.current_step = None
        self.completed_steps = []
        self.memory = []
        self.done = False