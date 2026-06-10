# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. When I first started the game, it showed attempts left 7 (there should be 8 attempts to start with as mentioned in the game instructions), although when I start a new game, it correctly shows, attempts left = 8.
  Same for other levels, the attemt number to start with is 1 less.

  2. Yes, the hints are backwards, when I need to go lower, it says ho higher, and when I need to go higher, the hint is go lower.

  3. New game button doesn't work once you win the game.

  4. In game setting, easy has a range from 1 - 20, but the game still has a range from 1 - 100, mismatch in instructions and the actual game.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Difficulty level hard| attempts left: 5| attempts left: 4
| 60 | hint: go higher| hint: go lower|
| New game (after winning the game) | should start a new game | doesn't start a new game| You already won. Start a new game to play again.
| Difficulty: hard| Guess a number between 1 and 50 | Guess a number between 1 and 100

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  claude code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The issue: The logic is inverted:

When guess > secret (your guess is too high), it should say "Go LOWER" but it says "Go HIGHER"
When guess < secret (your guess is too low), it should say "Go HIGHER" but it says "Go LOWER"
The fix: Swap the messages
  
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I did not encounter a wrong suggestion from the AI in either of my fixes.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I first asked the AI assistant to generate a pytest case as per the instructions and ran it in the terminal, when that worked, I run the app and tried it in the browser to verify that the issue was fixed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  for my 1st fix: I simply run the the app and in the game in the browser, the attempts left was correct to 8 (for normal), on playing the game, I entered all the incorrect numbers to ensure the correct number of attempts were allowed.
  for my 2nd fix: again in the browser, on entering the incorrect number, I was getting the correct hint from the game.

- Did AI help you design or understand any tests? How?
yes, AI helped me design the pytest case I could run in the terminal and instructed me on how to un it too.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
