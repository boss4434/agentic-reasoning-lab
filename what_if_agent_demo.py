import random, pandas as pd, matplotlib.pyplot as plt

def simulate_demand(base_demand, volatility=0.15):
    return [base_demand * (1 + random.uniform(-volatility, volatility)) for _ in range(10)]

scenarios = {
    "baseline": simulate_demand(1000),
    "promotion": simulate_demand(1200),
    "supply_disruption": simulate_demand(900)
}
df = pd.DataFrame(scenarios)
summary = df.mean().to_dict()
best = max(summary, key=summary.get)

plt.figure(figsize=(8,5))
for col in df.columns:
    plt.plot(df[col], label=col)
plt.title("What-If Simulation — Demand Projection Scenarios")
plt.xlabel("Time (weeks)")
plt.ylabel("Projected Demand")
plt.legend()
plt.show()

print(f"🏁 Recommended strategy: {best.upper()} — yields highest projected demand.")
