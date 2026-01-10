import random

color_psychology = {
    "happy": {
        "color": "Yellow",
        "meaning": "Optimism and energy",
        "outfits": [
            "a yellow t-shirt with blue jeans",
            "a light yellow shirt with white trousers"
        ]
    },
    "calm": {
        "color": "Blue",
        "meaning": "Calmness and trust",
        "outfits": [
            "a blue shirt with grey pants",
            "a pastel blue kurta with white pajama"
        ]
    },
    "confident": {
        "color": "Red",
        "meaning": "Confidence and passion",
        "outfits": [
            "a red shirt with black jeans",
            "a maroon blazer with dark trousers"
        ]
    },
    "energetic": {
        "color": "Yellow",
        "meaning": "Energy and enthusiasm",
        "outfits": [
            "a bright yellow hoodie with joggers",
            "a neon t-shirt with denim jeans"
        ]
    },
    "stressed": {
        "color": "Green",
        "meaning": "Balance and freshness",
        "outfits": [
            "a green t-shirt with beige pants",
            "an olive shirt with light jeans"
        ]
    }
}

event_styles = {
    "interview": "formal",
    "date": "stylish",
    "party": "trendy",
    "casual": "comfortable"
}

mood = input("Enter your mood: ").lower()
event = input("Enter event type: ").lower()

if mood in color_psychology:
    data = color_psychology[mood]
    outfit = random.choice(data["outfits"])
    style = event_styles.get(event, "smart")
    print(f"You are feeling {mood}.")
    print(f"Recommended Color: {data['color']} ({data['meaning']})")
    print(f"Suggested Outfit: Try wearing {outfit} for a {style} look.")
else:
    print("Sorry, mood not recognized. Try again.")