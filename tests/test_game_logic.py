from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_hint_messages_not_backwards():
    # Test that hint messages are correct (this was the bug!)
    # When guess is too high, message should say "Go LOWER"
    outcome_high, message_high = check_guess(60, 50)
    assert outcome_high == "Too High"
    assert "LOWER" in message_high, f"Expected 'LOWER' in message, got: {message_high}"
    
    # When guess is too low, message should say "Go HIGHER"
    outcome_low, message_low = check_guess(40, 50)
    assert outcome_low == "Too Low"
    assert "HIGHER" in message_low, f"Expected 'HIGHER' in message, got: {message_low}"
