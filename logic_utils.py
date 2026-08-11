"""Pure game-logic helpers for Game Glitch Investigator."""


DIFFICULTY_RANGES = {
    "Easy": (1, 20),
    "Normal": (1, 100),
    "Hard": (1, 50),
}


def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Return the inclusive guessing range for a difficulty level."""
    return DIFFICULTY_RANGES.get(difficulty, (1, 100))


def parse_guess(raw: str):
    """
    Parse user input into an integer guess.

    Returns:
        tuple[bool, int | None, str | None]:
        (success, parsed_guess, error_message)
    """
    if raw is None or not raw.strip():
        return False, None, "Enter a guess."

    try:
        value = int(raw.strip())
    except ValueError:
        return False, None, "Enter a whole number."

    return True, value, None


def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """Compare a guess with the secret number."""
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


def update_score(
    current_score: int,
    outcome: str,
    attempt_number: int,
) -> int:
    """
    Award points when the player wins.

    Earlier wins receive more points.
    """
    if outcome != "Win":
        return current_score

    points = max(
        10,
        100 - (attempt_number - 1) * 10,
    )

    return current_score + points
