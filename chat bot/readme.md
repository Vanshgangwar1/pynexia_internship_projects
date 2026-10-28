# Rule-Based Chatbot in Python

A lightweight, pattern-matching chatbot built with Python. The application preprocesses user input, evaluates intent patterns using Regular Expressions (Regex), and provides coherent, conditional responses via a terminal interface[cite: 2].

---

## 📌 Features

- **Input Preprocessing**: Strips leading/trailing spaces, normalizes text to lowercase, and removes punctuation for clean string comparison[cite: 2].
- **Intent Pattern Matching**: Uses Python's `re` module to evaluate keyword triggers and Regex rules[cite: 2].
- **Conditional Responses**: Selects contextually relevant answers using predefined rule mappings[cite: 2].
- **Graceful Fallbacks**: Handles unrecognized commands or empty inputs cleanly without crashing.
- **Interactive CLI**: Maintained conversational session loop with safe exit triggers (`exit`, `bye`, `quit`)[cite: 2].

---

## 📁 Project Structure