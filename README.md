# AP-CSP-pseudo-language

A programming language based on the AP CSP pseudo-language. Documentation of their syntax can be found at this [PDF of the 2026 exam reference information](https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf).

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

Deviations from AP CSP language:
 - `←` as the assignment operator is too annoying to use (you have to copy/paste it and it's not muscle memory), so I use `=` instead.
 - I use power operators because (a) the tutorial I'm following uses them and it'd be too hard/annoying to work around that, and (b) power operators can be useful
 - Declare variables with VAR (AP CSP doesn't use VAR)
    - The video used VAR and I felt it would be too hard/annoying to cut it

Specific syntax:
 - `^` is the power operator
 - VAR [identifier] = [expr]

Issues:
 - Arrows (carets) under errors don't extend the whole way through, like they do in the video
 - Parts of the language (such as TRUE, FALSE, etc) can have their values altered

To-Do:
 - Make the IF statement part match the video for now, but later change it to match the AP CSP language
 - Make the FOR/WHILE statement part match the video for now, but later change it to match the AP CSP language