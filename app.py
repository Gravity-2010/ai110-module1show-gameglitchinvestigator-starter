import random

import streamlit as st

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


ATTEMPT_LIMITS = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}


st.set_page_config(
    page_title="Game Glitch Investigator",
    page_icon="🎮",
)

st.title("🎮 Game Glitch Investigator")
st.caption(
    "A debugging exercise exploring Streamlit session state, "
    "game logic, refactoring, and testing."
)


# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

low, high = get_range_for_difficulty(difficulty)
attempt_limit = ATTEMPT_LIMITS[difficulty]

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(
    f"Attempts allowed: {attempt_limit}"
)


# ---------------------------------------------------------------------------
# Game-state helpers
# ---------------------------------------------------------------------------

def reset_game() -> None:
    """Reset all state required for a fresh game."""
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []

    st.session_state.game_id = (
        st.session_state.get("game_id", 0) + 1
    )


if (
    "difficulty" not in st.session_state
    or st.session_state.difficulty != difficulty
):
    st.session_state.difficulty = difficulty
    reset_game()

elif "secret" not in st.session_state:
    reset_game()


# ---------------------------------------------------------------------------
# Game information
# ---------------------------------------------------------------------------

st.subheader("Make a Guess")

attempts_left = (
    attempt_limit - st.session_state.attempts
)

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempts_left}"
)


# ---------------------------------------------------------------------------
# Controls
# ---------------------------------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    new_game = st.button("New Game 🔁")

with col2:
    show_hint = st.checkbox(
        "Show hints",
        value=True,
    )


if new_game:
    reset_game()
    st.rerun()


# ---------------------------------------------------------------------------
# Game status
# ---------------------------------------------------------------------------

if st.session_state.status == "won":
    st.success(
        "You already won! Start a new game to play again."
    )

elif st.session_state.status == "lost":
    st.error(
        "Game over. Start a new game to try again."
    )


# ---------------------------------------------------------------------------
# Input
# ---------------------------------------------------------------------------

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{st.session_state.game_id}",
)

submit = st.button(
    "Submit Guess 🚀",
    disabled=st.session_state.status != "playing",
)


# ---------------------------------------------------------------------------
# Guess handling
# ---------------------------------------------------------------------------

if submit:
    ok, guess, error = parse_guess(raw_guess)

    if not ok:
        st.error(error)

    elif guess < low or guess > high:
        st.error(
            f"Enter a number between {low} and {high}."
        )

    else:
        st.session_state.attempts += 1

        outcome, message = check_guess(
            guess,
            st.session_state.secret,
        )

        st.session_state.history.append(
            {
                "attempt": st.session_state.attempts,
                "guess": guess,
                "result": outcome,
            }
        )

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.session_state.status = "won"

            st.balloons()

            st.success(
                f"You won in "
                f"{st.session_state.attempts} attempts! "
                f"Score: {st.session_state.score}"
            )

        else:
            if show_hint:
                st.warning(message)

            if (
                st.session_state.attempts
                >= attempt_limit
            ):
                st.session_state.status = "lost"

                st.error(
                    f"Out of attempts! "
                    f"The secret number was "
                    f"{st.session_state.secret}."
                )


# ---------------------------------------------------------------------------
# History
# ---------------------------------------------------------------------------

if st.session_state.history:
    st.divider()
    st.subheader("Attempt History")

    st.dataframe(
        st.session_state.history,
        use_container_width=True,
        hide_index=True,
    )


# ---------------------------------------------------------------------------
# Debug information
# ---------------------------------------------------------------------------

with st.expander("Developer Debug Info"):
    st.write(
        "Secret:",
        st.session_state.secret,
    )

    st.write(
        "Attempts:",
        st.session_state.attempts,
    )

    st.write(
        "Score:",
        st.session_state.score,
    )

    st.write(
        "Difficulty:",
        difficulty,
    )
