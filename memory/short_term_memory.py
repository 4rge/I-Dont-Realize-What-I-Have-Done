class ShortTermMemory:
    def __init__(self):
        self.memory = []

    def store(self, item):
        if len(self.memory) >= 10:  # Limit memory size (e.g., last 10 interactions)
            self.memory.pop(0)
        self.memory.append(item)

    def retrieve(self):
        return self.memory
