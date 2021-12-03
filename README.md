# Password Generator

Terminal utility written in python that is used to generate passwords with random characters.

```
usage: pass-generator [-h] [-u] [-l] [-d] [-p] LENGTH

Random characters password generator.

positional arguments:
  LENGTH             The length of the password (min: 4).

optional arguments:
  -h, --help         Show this help message and exit.
  -u, --upper        Disable ascii upper letters (enabled by default)
  -l, --lower        Disable ascii lower letters (enabled by default).
  -d, --digit        Disable digit characters (enabled by default).
  -p, --punctuation  Enable punctuation symbols (disabled by default).
```