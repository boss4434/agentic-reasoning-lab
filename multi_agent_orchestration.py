import random, time

class ReasoningAgent:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def reason(self, context):
        print(f"[{self.name}] ({self.specialty}) reasoning on: {context}")
        time.sleep(0.5)
        return f"{self.name} suggests: {random.choice(['expand idea', 'refine context', 'validate fact', 'generate plan'])}"

class Orchestrator:
    def __init__(self, agents):
        self.agents = agents

    def run(self, goal):
        print(f"Goal: {goal}\n")
        context = goal
        for _ in range(2):
            for agent in self.agents:
                result = agent.reason(context)
                context += f" -> {result}"
        print("\nFinal reasoning: ", context)

if __name__ == "__main__":
    agents = [ReasoningAgent("Planner","strategy"), ReasoningAgent("Retriever","knowledge"), ReasoningAgent("Evaluator","accuracy")]
    Orchestrator(agents).run("Optimize retail supply forecast for new product launch")
