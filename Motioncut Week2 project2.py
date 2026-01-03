import random

history = []

def style_one(n1, n2):
    return n1[:len(n1)//2] + n2[len(n2)//2:]

def style_two(n1, n2):
    return n1[:3] + n2[:3]

def style_three(n1, n2):
    chars = list(n1 + n2)
    random.shuffle(chars)
    return "".join(chars[:6])

def style_four(n1, n2):
    return (n2 + n1)[::-1]

def generate_nicknames(name1, name2):
    styles = [
        style_one(name1, name2),
        style_two(name1, name2),
        style_three(name1, name2),
        style_four(name1, name2)
    ]
    return styles

def main():
    while True:
        name1 = input("Enter first name: ").strip()
        name2 = input("Enter second name: ").strip()

        nicknames = generate_nicknames(name1, name2)

        print("\nGenerated Nicknames:")
        for n in nicknames:
            print(n)
            history.append(n)

        choice = input("\nGenerate again? (yes/no): ").lower()
        if choice != "yes":
            break

    if history:
        print("\nNickname History:")
        for h in history:
            print(h)

    print("\nProgram ended.")

if __name__ == "__main__":
    main()