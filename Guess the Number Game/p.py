import random
import time

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLORS = True
except Exception:
    COLORS = False
    class _NoColor:
        RESET_ALL = ""

    class _NoFore:
        CYAN = MAGENTA = YELLOW = GREEN = BLUE = RED = ""

    Fore = _NoFore()
    Style = _NoColor()

def color(text, c):
    if COLORS:
        return c + text + Style.RESET_ALL
    return text

def loading(text, t=0.5):
    print(text, end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(t)
    print()

def get_feedback(diff):
    compliments = [
        "Nice try! You're learning fast 😄",
        "Good guess! Keep going 🔥",
        "You're getting warmer 🔥🔥",
        "You're close! Trust your instincts 💡",
        "Smart move! Keep it up! 🚀",
        "Great energy! Let’s win this 💪",
    ]
    return random.choice(compliments)


def guess_game():
    print(color("\n🎮 WELCOME TO GUESS THE NUMBER —  🎮", Fore.CYAN))
    print(color("Boosted with rewards, emotions & engagement psychology!\n", Fore.MAGENTA))

    print(color("Select Difficulty Level:", Fore.YELLOW))
    print("1) Easy (1–20)\n2) Medium (1–100)\n3) Hard (1–500)\n4) Impossible (1–1000)")

    while True:
        try:
            level = int(input("\nChoose 1/2/3/4: "))
            if level in [1, 2, 3, 4]:
                break
            else:
                print("Choose a valid option.")
        except:
            print("Enter a number.")

    ranges = {1: 20, 2: 100, 3: 500, 4: 1000}
    max_num = ranges[level]

    loading(color("\nPreparing your challenge", Fore.GREEN), 0.3)

    number = random.randint(1, max_num)
    attempts = 0

    print(color(f"\nI’m thinking of a number between 1 and {max_num}.", Fore.BLUE))
    print(color("Can you guess it? Let’s see how sharp your brain is! 🧠⚡", Fore.MAGENTA))

    while True:
        try:
            guess = int(input(color("\n👉 Your guess: ", Fore.YELLOW)))
            attempts += 1

            if guess < 1 or guess > max_num:
                print(color(f"⚠ Guess must be between 1 and {max_num}.", Fore.RED))
                continue

            print(color(get_feedback(level), Fore.CYAN))

            if guess < number:
                print(color("⬆ Too low!", Fore.RED))
            elif guess > number:
                print(color("⬇ Too high!", Fore.RED))
            else:
                print(color("\n🥳🎉 YOU GUESSED IT! 🎉🥳", Fore.GREEN))
                print(color(f"✔ Number was: {number}", Fore.BLUE))
                print(color(f"✔ Attempts: {attempts}\n", Fore.YELLOW))

                print(color("🏆 ACHIEVEMENTS UNLOCKED:", Fore.MAGENTA))
                if attempts == 1:
                    print(color("⭐ Lucky Genius! (Guessed in 1 try!)", Fore.GREEN))
                if attempts <= 5:
                    print(color("⭐ Sharp Shooter! (Under 5 attempts)", Fore.CYAN))
                if attempts > 15:
                    print(color("⭐ Persistence Master! (Never gave up!)", Fore.YELLOW))

                break

        except ValueError:
            print(color("❌ Please enter a valid number.", Fore.RED))

    again = input(color("\n🔁 Play again? (y/n): ", Fore.MAGENTA)).lower()
    if again == "y":
        guess_game()
    else:
        print(color("\n👋 Thanks for playing! You were awesome!", Fore.CYAN))



guess_game()
