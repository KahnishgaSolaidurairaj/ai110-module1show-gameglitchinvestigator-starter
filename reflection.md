# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|   -2  | Hint: Not in Range| Hint: "Go LOWER!" based on the secret it should have said to go higher or out of range | None                   |
| 10000 | Hint: Not in Range| Hint: "Go HIGHER!" based on the secret it should have said to go lower or out of range| None                   |
|  33.6 | Incorrect, Hint to use whole numbers | "You won! The secret was 33" but the decimal value and 33 is not the same| None      |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI tool I used was Claude directly connected with my VSCode. I used it as a debugging partner where I described the wrong behavior I saw in the game, and it helped me locate the exact lines causing each bug and explain why they broke.

One AI suggestion that was correct was the fix for the decimal bug. The AI noticed that parse_guess used int(float(raw)), which silently truncated 33.6 down to 33, and it suggested switching to int(raw) so non-whole numbers get rejected instead. I verified this by running the function on test inputs: 33.6 and abc now return "That is not a whole number," while 33 still works as a valid guess.

One AI suggestion that was misleading came after we removed a str() cast that had been flipping the hints. The AI claimed the game "now correctly says Go HIGHER" for guess 20 against secret 87, but when I actually read the test output it still said "Go LOWER!" which is wrong, since 20 is below 87. I verified this by playing the game and checking the printed result myself, and it turned out the real bug was that the hint messages in check_guess were swapped. This taught me not to trust the AI's summary of a result without reading the output myself.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed when the actual output matched the expected behavior from my bug log, not just when the AI said it was fixed. For each fix I re-ran the specific input that had broken before and confirmed it now did the right thing. For example, after fixing check_guess I tested guess 20 against secret 87 and saw it return "Go HIGHER!", then tested 90 against 87 and got "Go LOWER!", which showed the hints finally pointed the right direction. AI helped me by suggesting small test inputs to run for each bug and explaining what each result meant, which made it faster to tell a real fix from a fake one.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would tell a friend that Streamlit re-runs the entire script from top to bottom every time you interact with the page, like clicking a button or typing a guess. Because of that, any normal variable gets reset on every interaction, so you can't rely on it to remember anything. Session state is the fix since it's a special storage box that survives those reruns, which is why the secret number, score, and attempts all live in st.session_state. Understanding this helped me see why bugs like the attempt counter or the secret number had to be handled through session state instead of regular variables.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is reproducing a bug with a specific input before and after a fix, so I always have proof that something actually changed. Next time I would ask the AI to show me the real test output instead of trusting its summary, since it once told me a hint was correct when it clearly wasn't. This project changed how I think about AI-generated code by showing me that it can look polished and confident while still being wrong, so I now treat it as a fast first draft that I always have to verify myself.
