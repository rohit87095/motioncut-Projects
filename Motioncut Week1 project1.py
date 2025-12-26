def get_mood_response(mood_text):
    mood_text = mood_text.lower().strip()

    moods = {
        "happy":    ("😄", "Yay! That makes me happy too!"),
        "sad":      ("😢", "Cheer up! You’ve got this."),
        "angry":    ("😠", "Take a deep breath… it will be okay."),
        "tired":    ("😴", "You should get some rest soon."),
        "excited":  ("🤩", "Wow, that sounds super exciting!"),
        "stressed": ("😓", "Remember to take short breaks and relax."),
    }

    for keyword, (emoji, message) in moods.items():
        if keyword in mood_text:
            return f"{emoji}  {message}"

    return "🤔  I’m not sure how that feels, but I’m here for you!"


def main():
    print("=== Emoji Mood Responder ===")
    print("Type 'exit' anytime to quit.\n")

    while True:
        user_input = input("How are you feeling today? ")

        if user_input.lower().strip() == "exit":
            print("👋 Bye! Take care of your mood.")
            break

        response = get_mood_response(user_input)
        print(response + "\n")


if __name__ == "__main__":
    main()