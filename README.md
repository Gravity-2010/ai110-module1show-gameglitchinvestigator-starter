# 🎮 Game Glitch Investigator

### Debugging a Streamlit Number-Guessing Game

> **Coursework / Learning Project**
>
> This repository contains my implementation of the **CodePath AI110 Game Glitch Investigator exercise**, focused on debugging AI-generated code, understanding Streamlit session state, refactoring business logic, and validating fixes with automated tests.

The starter application was intentionally broken. The goal was to identify the defects, understand why they occurred, repair them, and verify the resulting behavior rather than accepting AI-generated code at face value.

---

## 🐛 Bugs Investigated

The original game contained several issues:

* The number of remaining attempts started incorrectly.
* Higher/lower hints were reversed.
* The secret number was not handled consistently across Streamlit reruns.
* Difficulty-specific number ranges were not applied consistently.
* Starting a new game did not correctly reset all game state.
* Game logic was embedded directly in the Streamlit interface instead of being separated into testable functions.

---

## ✅ Final Behavior

The corrected application supports three difficulty levels:

| Difficulty | Range | Attempts |
| ---------- | ----: | -------: |
| Easy       |  1–20 |        6 |
| Normal     | 1–100 |        8 |
| Hard       |  1–50 |        5 |

Players can:

* Select a difficulty
* Enter guesses
* Receive higher/lower hints
* Track remaining attempts
* View attempt history
* Earn a score for winning
* Start a fresh game at any time

---

## 🧠 Streamlit Session State

One of the primary bugs involved Streamlit's execution model.

Streamlit reruns the Python script from top to bottom whenever the user interacts with a widget.

Without session state, values such as:

```text
secret number
attempt count
game status
score
guess history
```

would be recreated or lost during those reruns.

The corrected implementation stores persistent game information in:

```python
st.session_state
```

so the game can maintain its state between interactions.

---

## 🏗️ Refactoring

The final version separates user-interface behavior from reusable game logic.

```text
Streamlit UI
    │
    ▼
app.py
    │
    ▼
logic_utils.py
    │
    ├── difficulty ranges
    ├── input parsing
    ├── guess comparison
    └── score calculation
```

This allows core behavior to be tested without starting Streamlit.

---

## 🔍 Game Logic

### Correct Guess

```text
guess == secret
      ↓
     Win
```

### Guess Too High

```text
guess > secret
      ↓
   Too High
      ↓
   Go LOWER
```

### Guess Too Low

```text
guess < secret
      ↓
    Too Low
      ↓
   Go HIGHER
```

---

## 🧪 Testing

The project includes automated tests for:

* Difficulty ranges
* Valid input parsing
* Empty input
* Invalid/non-numeric input
* Correct guesses
* Too-high guesses
* Too-low guesses
* Correct hint direction
* Score calculation

Run:

```bash
python -m pytest
```

Automated tests are supplemented with manual testing through the Streamlit interface.

---

## ▶️ Running the Application

### 1. Clone the repository

```bash
git clone https://github.com/Gravity-2010/ai110-module1show-gameglitchinvestigator-starter.git
cd ai110-module1show-gameglitchinvestigator-starter
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

### 5. Run tests

```bash
python -m pytest
```

---

## 📁 Project Structure

```text
ai110-module1show-gameglitchinvestigator-starter/
│
├── tests/
│   └── test_game_logic.py
│
├── app.py
├── logic_utils.py
├── reflection.md
├── ai_interactions.md
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies

`Python` · `Streamlit` · `Pytest`

---

## 🎯 What I Learned

This exercise reinforced several software-engineering practices:

* Reproduce a bug before changing the code.
* Understand the underlying cause rather than patching symptoms.
* Separate business logic from UI code.
* Use automated tests to verify deterministic behavior.
* Supplement automated tests with manual integration testing.
* Treat AI-generated code as a suggestion that still requires verification.
* Understand framework-specific behavior such as Streamlit reruns and session state.

---

## 🙏 Attribution

This repository is based on the **CodePath AI110 Game Glitch Investigator starter exercise**.

It is preserved as a record of my debugging, testing, refactoring, and AI-assisted development practice.

---

## 📌 Repository Status

**Archived coursework / learning project**

This repository is not actively maintained as a standalone production application.
