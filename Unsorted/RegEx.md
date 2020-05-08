    Copyright(c) 2020-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+

# Regular Expressions (RegEx)

<center>

| Expression | Meaning |
|   :---:   |  :---:  |
| `.` | Any character (except newline) |
| `\d`, `\D` | Digit (0-9), !Digit |
| `\w`, `\W`| Word (a-z, A-Z, 0-9, _), !Word|
| `\s`, `\S` | Whitespace (space, tab, newline), !Whitespace |
| `\b`, `\B` | WordBoundary, !WordBoundary |
| `^`, `$` | Beginning/End of String |
| `[]`,`[^]`,`()`,`{n}`,`{m,n}` | CharacterSet, !CharacterSet, WordGroup, n-Values, Values between m & n times |

</center>

- Quantifier

<center>

| Expression | Meaning | Example | Description |
|   :---:   |  :---:  |  :---:  |  :---:  |
| `*`,`+` | >=0, >=1 | `\d*`,`\d+` | `0 or more digits`, `1 or more digits` |
| `?` | 0 or 1 | `\d?`| `0 or 1 digit` |
| `{n}` | Exact value (=n) | | |
| `{start, stop}` | Range of values (min, max) | | |

</center>

### Examples
- Phone Numbers <br>
    +91-95774-21050 <br>
    +91-94273-18798 <br>
    +91-81340-14187 <br>
    ```
    \d\d.\d\d\d\d\d.\d\d\d\d\d
    \+\d\d[-]\d\d\d\d\d[-]\d\d\d\d\d
    \+\d{2}-?\d{5}-?\d{5}
    ```
    +91-95774-21050 to 9577421050
    ```
    (\+\d{2})-?(\d{5})-?(\d{5})
    $2$3
    ```
- Character from the alphabet. `[a-zA-Z]`
- Anything except characters of the alphabet. `[^a-zA-Z]`
- HTTP URLs. `https?://(www\.)?\w+\.\w+`
- Rhyming words (cat, mat, bat, rat). `at\b`
- [ ] Rhyming words (cat, mat, bat, rat, rattatat). <br>

``` py
#!/usr/bin/env python3
import re


text = '''
abc1234!
'''
pattern = re.compile(r'(\bDoe\b)')
matches = pattern.finditer(text)
for match in matches:
    print(match)
```

```
1. Get Source & Destination directories from header.
\b(Source|Dest)\s+:\s(.+)
\b(?P<type>Source|Dest)\s+:\s(?P<dir>.+)

2. Get Error message.
# timestamp
(\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2}:\d{2})
(\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2}:\d{2})
\d{4}(/\d{2}){2}\s+(\d{2}:?){3}
# error
\bERROR\s+(.+)

3. Get metrics table
\b(Dir|File|Byte|Time)s\s+:(\s+[\d:]+){1,}
```

## To-Do

- [ ] Curate a table of expressions with examples.
- [ ] Python: Use RegEx.
- [ ] Python: Implement RegEx in code.
