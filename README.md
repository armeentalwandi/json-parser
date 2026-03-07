# JSON Parser

This project is a simple JSON parser written in Python, built from scratch without using Python's built-in `json` module. The goal was to learn how parsing works under the hood by implementing both a lexer (tokenizer) and a parser that follows the JSON grammar.

## What it does

- Reads and validates JSON files, including:
  - Objects and arrays
  - Strings, numbers (including decimals and exponents), booleans, and null
  - Nested structures
  - Whitespace and basic escape sequences in strings
- Gives clear error messages for invalid JSON
- Includes a test runner to check your parser against a suite of test files for each step of the project

## How to use it

To check if a JSON file is valid:

```bash
python main.py path/to/file.json
```

To run tests for a specific step or all steps:

```bash
python test_runner.py 2      # Run tests for step 2
python test_runner.py all    # Run all step tests
```

## Project files

- `main.py` — Command-line entry point
- `lexer.py` — Turns JSON text into tokens
- `parser.py` — Checks if the token sequence matches JSON grammar
- `token.py` — Defines token types and the Token class
- `tests/` — Test JSON files for each step
- `test_runner.py` — Script to run all tests and show results

## What you learn by doing this

- How to break down text into tokens (lexical analysis)
- How to write a recursive descent parser that follows a formal grammar
- How to handle errors and edge cases in input
- How to write code that is modular and easy to test
- How to follow a published standard (ECMA-404 for JSON)
- How to automate testing for your own code

## Why it matters

Building a parser from scratch gives you a real understanding of how data formats and programming languages are processed. You get hands-on experience with concepts like tokenization, parsing, error handling, and test automation—skills that are useful for everything from writing interpreters to building robust data pipelines.

---
