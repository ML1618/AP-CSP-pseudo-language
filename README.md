# BASIC-like Interpreted Language

This language is a BASIC-like, interpreted programming language, coded in Python.

This language was originally based on the AP CSP pseudo-language. Documentation of their syntax can be found at this [PDF of the 2026 exam reference information](https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf). However, due to complications, I had to abandon that:
- The biggest issue is that the tutorial series I'm following diverges too much from the AP CSP language in a way that's difficult to fix without major rewriting after the fact. The syntax is especially different.
- In the future, I may go back and try the project again. That's a long ways off, however.

When creating this language, I followed along with this [YouTube series](https://www.youtube.com/playlist?list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD).

Progress:
- Lexer episode finished
- Parser episode finished
- Interpreter episode finished
- Power operator finished
- Variable episode finished
- Comparisons and logical operators episode finished
- IF statement video finished
- FOR and WHILE statement video finished
- Function video just started

Specific syntax:
- `^` is the power operator
- VAR [identifier] = [expr]

Issues:
- Parts of the language (such as TRUE, FALSE, etc) can have their values altered