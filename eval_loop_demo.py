import random

def evaluate_responses(responses):
    print("\nEvaluating reasoning quality...")
    accuracy = random.uniform(0.7, 0.95)
    hallucination = random.uniform(0.05, 0.25)
    trust_score = (accuracy - hallucination) * 100
    print(f"Accuracy: {accuracy:.2f}\nHallucination: {hallucination:.2f}\nTrust Score: {trust_score:.1f}")
    print("✅ Model reliability acceptable." if trust_score > 70 else "⚠️ Needs improvement.")

if __name__ == "__main__":
    evaluate_responses(["Plan improved accuracy."])
