# Lab 5 Reflection

The repository README refers to four reflection questions in the separate lab handout, but their exact wording is not included in the repository. These draft responses cover the main learning points; compare them with the handout and adjust the headings to match the instructor's exact questions.

## 1. What is static code analysis, and why is it useful?

Static code analysis checks source code without running the program. It can identify possible bugs, unsafe coding patterns, and style problems early, making software easier to review and maintain.

## 2. What are the differences between Pylint, Bandit, and Flake8?

Pylint focuses on code quality and suspicious programming practices. Bandit checks for common security risks in Python code. Flake8 checks style and formatting rules. Using all three gives a broader view than relying on just one tool.

## 3. Which issues were most important to fix, and why?

Unsafe pickle deserialization and shell command construction were important because they can introduce security vulnerabilities. The mutable default argument, invalid-priority handling, and empty-list check improve correctness and reliability. Consistent naming and documentation make the program easier to understand.

## 4. What did you learn from this lab?

I learned that code can appear to work while still containing security, reliability, and maintainability problems. Different analysis tools find different categories of issues. Warnings should be investigated and verified, and the program should be tested after changes to ensure its intended behavior remains intact.
