from collections import Counter

EMOTION_KEYWORDS = {
    "joy": [
        "happy", "joy", "glad", "excited", "pleased", "delighted",
        "cheerful", "smile", "laugh", "awesome", "great", "fantastic"
    ],
    "sadness": [
        "sad", "unhappy", "depressed", "down", "cry", "upset",
        "miserable", "lonely", "heartbroken", "tears"
    ],
    "anger": [
        "angry", "mad", "furious", "irritated", "annoyed", "rage",
        "hate", "frustrated"
    ],
    "fear": [
        "afraid", "scared", "fear", "terrified", "nervous",
        "anxious", "worried"
    ],
    "surprise": [
        "surprised", "shocked", "amazed", "astonished", "wow"
    ],
    "disgust": [
        "disgusted", "gross", "nasty", "revolting"
    ]
}

EMOTION_EMOJIS = {
    "joy": "😊",
    "sadness": "😢",
    "anger": "😠",
    "fear": "😨",
    "surprise": "😮",
    "disgust": "🤢"
}


def build_reverse_dictionary(emotion_keywords):
    word_to_emotion = {}
    for emotion, words in emotion_keywords.items():
        for w in words:
            word_to_emotion[w] = emotion
    return word_to_emotion


WORD_TO_EMOTION = build_reverse_dictionary(EMOTION_KEYWORDS)


def preprocess(text):
    text = text.lower()
    tokens = text.split()
    cleaned = []
    for t in tokens:
        cleaned.append(t.strip(".,!?;:\"'()[]{}"))
    return [w for w in cleaned if w]


def detect_emotion(text):
    tokens = preprocess(text)
    emotion_hits = []

    for token in tokens:
        if token in WORD_TO_EMOTION:
            emotion_hits.append(WORD_TO_EMOTION[token])

    if not emotion_hits:
        return None, Counter()

    counts = Counter(emotion_hits)
    dominant_emotion = counts.most_common(1)[0][0]
    return dominant_emotion, counts


def format_result(emotion, counts):
    if emotion is None:
        return "No emotion keywords detected. Try a more expressive sentence."

    emoji = EMOTION_EMOJIS.get(emotion, "")
    lines = [f"Detected Emotion: {emotion.capitalize()} {emoji}", "Details:"]
    for e, c in counts.most_common():
        lines.append(f"  - {e.capitalize()}: {c}")
    return "\n".join(lines)


def main():
    print("=== Emotion Detector from Text ===")
    print('Type a sentence (or "exit" to quit).\n')

    while True:
        user_input = input("Your text: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        emotion, counts = detect_emotion(user_input)
        result = format_result(emotion, counts)
        print(result)
        print("-" * 40)


if __name__ == "__main__":
    main()