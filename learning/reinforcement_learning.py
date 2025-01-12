class ReinforcementLearning:
    def __init__(self):
        self.memory = {}

    def update_policy(self, state, action, reward):
        # Simplicity: Direct mapping for demo
        self.memory[state] = (action, reward)
