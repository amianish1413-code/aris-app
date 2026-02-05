import random

def reply(text, memory):
    text = text.lower()

    if "remember that" in text:
        fact = text.replace("remember that", "").strip()
        memory.append(fact)
        return "I will remember that."

    if "what do you remember" in text:
        if memory:
            return "I remember: " + ", ".join(memory)
        return "I remember nothing yet."

    responses = {
        "hello": ["Hello sir.", "Systems online."],
        "your name": ["I am A.R.I.S. Advanced Responsive Intelligence System."],
        "how are you": ["Running optimally."]
    }

    for key in responses:
        if key in text:
            return random.choice(responses[key])

    return "Offline mode active."
