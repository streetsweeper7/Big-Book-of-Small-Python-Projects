# Bagels, a deductive logic game.
# by John Banda adrielbanda4@gmail.com

import random

class BagelsGame:
    def __init__(self, num_digits: int = 3, max_guesses: int = 10):
        self.num_digits     = num_digits
        self.max_guesses    = max_guesses
        self.answer         = self._generate_answer()
        self.guess_count    = 0
        self.won            = False
    
    def _generate_answer(self) -> list[int]:
        digits = list(range(10))
        random.shuffle(digits)
        if digits[0] == 0:
            digits[0], digits[1] = digits[1], digits[0]
        return digits[:self.num_digits]

    def validate_guess(self, guess: str) -> str:

        if len(guess) != self.num_digits or not guess.isdigit():
            return f"Invalid input. Enter a {self.num_digits}-digit number." 

        self.guess_count += 1
        guess_digits     = [int(ch) for ch in guess]
        fermi   = sum(
            guess_digits[i] == self.answer[i] for i in range(self.num_digits)
        )
        pico    = sum(
            guess_digits[i] != self.answer[i] and guess_digits[i] in self.answer
            for i in range(self.num_digits)
        )
        
        if fermi == self.num_digits:
            self.won = True
            return "You got it!"
        
        if fermi == 0 and pico == 0:
            return "Bagel"
        
        return " ".join(["Fermi"] * fermi + ["Pico"] * pico)

    def is_over(self) -> bool:
        return self.won or self.guess_count >= self.max_guesses

    def get_answer(self) -> str:
        return ''.join(map(str, self.answer))

def main():
    print("Welcome to Bagels!")

    while True:
        game = BagelsGame()

        while not game.is_over():
            guess = input(f"Guess #{game.guess_count + 1}: ").strip()
            feedback = game.validate_guess(guess)
            print(feedback)
            if game.won:
                break

        if not game.won:
            print(f"Out of guesses! The correct answer was: {game.get_answer()}")
        
        again = input("Do you want to play again? (yes or no) ").strip().lower()

        if not again.startswith("y"):
            break
        
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
