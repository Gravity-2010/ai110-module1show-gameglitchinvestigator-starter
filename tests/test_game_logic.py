from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_valid_guess():
    ok, guess, error = parse_guess("42")

    assert ok is True
    assert guess == 42
    assert error is None


def test_empty_guess():
    ok, guess, error = parse_guess("")

    assert ok is False
    assert guess is None
    assert error == "Enter a guess."


def test_non_numeric_guess():
    ok, guess, error = parse_guess("hello")

    assert ok is False
    assert guess is None
    assert error == "Enter a whole number."


def test_winning_guess():
    outcome, message = check_guess(50, 50)

    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    outcome, message = check_guess(60, 50)

    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)

    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_first_attempt_win_score():
    assert update_score(0, "Win", 1) == 100


def test_later_win_scores_less():
    assert update_score(0, "Win", 5) == 60


def test_incorrect_guess_does_not_change_score():
    assert update_score(50, "Too High", 2) == 50
