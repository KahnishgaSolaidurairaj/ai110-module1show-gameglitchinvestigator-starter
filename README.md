# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Purpose of the game**

Glitchy Guesser is a Streamlit number-guessing game. The app picks a secret number inside a range that depends on the chosen difficulty (Easy / Normal / Hard), and the player tries to guess it within a limited number of attempts. After each guess the game gives a "go higher / go lower" hint, updates the score, and ends when the player guesses correctly or runs out of attempts.

**Bugs I found**

1. **Out-of-range guesses were accepted** - values like -2 or 10000 got a higher/lower hint instead of being rejected as out of range.
2. **Decimals were truncated into wins** - 33.6 was silently turned into 33, so it could "win" against a secret of 33.
3. **The secret changed on submit** — on even attempts the secret was cast to a string, which broke comparisons and flipped hints.
4. **Hints were backwards** — a guess above the secret told the player to "Go HIGHER" instead of lower.
5. **The prompt ignored difficulty** — the instructions always said "between 1 and 100" even on Easy or Hard.

**Fixes I applied**

1. Added a range check in parse_guess so out-of-range guesses return a clear "Not in range" message.
2. Replaced int(float(raw)) with int(raw) so decimals are rejected as "not a whole number."
3. Removed the even-attempt str(secret) cast so the secret is always compared as an integer.
4. Corrected the swapped hint text in check_guess (above → go lower, below → go higher).
5. Made the prompt use the difficulty's actual low and high values.
6. Refactored the four logic functions into logic_utils.py, imported them into app.py, and added pytest coverage (see Test Results).

## 📸 Demo Walkthrough

A text-based run-through of a sample game on **Normal** difficulty (range 1–100, secret = 63):

1. The app loads on Normal difficulty and shows "Guess a number between 1 and 100. Attempts left: 5."
2. User enters **40** → game responds **"Too Low → 📈 Go HIGHER!"** and the score updates.
3. User enters **70** → game responds **"Too High → 📉 Go LOWER!"** and the score updates again.
4. User enters **33.6** → game rejects it with **"That is not a whole number."** (no false win).
5. User enters **150** → game rejects it with **"Not in range. Pick a number between 1 and 100."**
6. User enters **63** → game shows **"🎉 Correct!"**, fires the balloons, reveals the secret, and displays the final score.
7. The game then locks to a "you already won" state until the user clicks **New Game**, which resets the attempts and picks a fresh secret.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python -m pytest tests/ -v
============================= test session starts ==============================
platform darwin -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
rootdir: .../ai110-module1show-gameglitchinvestigator-starter
collected 8 items

tests/test_edge_cases.py::test_negative_number_is_rejected PASSED        [ 12%]
tests/test_edge_cases.py::test_decimal_is_rejected PASSED                [ 25%]
tests/test_edge_cases.py::test_extremely_large_value_is_rejected PASSED  [ 37%]
tests/test_edge_cases.py::test_boundaries_are_accepted PASSED            [ 50%]
tests/test_game_logic.py::test_winning_guess PASSED                      [ 62%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 75%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 87%]
tests/test_game_logic.py::test_hint_direction_is_not_swapped PASSED      [100%]

============================== 8 passed in 0.02s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
