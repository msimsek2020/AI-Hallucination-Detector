"""
AI Hallucination Detector

Author: Dr. Mustafa Simsek
"""

reference_facts = {
    "Capital of Texas": "Austin",
    "Largest planet": "Jupiter"
}


def detect_hallucination(question, response):
    expected = reference_facts.get(question)

    if expected is None:
        return "Unknown"

    if response.strip().lower() == expected.lower():
        return "Accurate"

    return "Potential Hallucination"


if __name__ == "__main__":

    result = detect_hallucination(
        "Capital of Texas",
        "Dallas"
    )

    print(result)
