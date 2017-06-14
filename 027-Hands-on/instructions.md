# Guess the number game
There is a game where one person thinks of a number, and another person tries to guess the number.
The guesser has a certain number of guesses,
and the person thinking of a number has to tell the guesser if their guess is too high or too low after each guess.

Create a program which will do this for a user. The code below will get the random number. Just place it at the top of the file.
```python
import random
number = random.randint(1, 100)
```
If the user does not enter a number, skip that guess without giving them any hints.

Here is an example of how the flow should go.

> I have thought of a number between 1 and 100. Please attempt to guess it.

> Enter a guess (6 guesses left)

> `50`

> Your number is too low

> Enter a guess (5 guesses left)

> `75`

> Your number is too high

> Enter a guess (4 guesses left)

> `65`

> Your guess is too high

> Enter a guess (3 guesses left)

> `55a`

> That is not a number

> Enter a guess (2 guesses left)

> `55`

> Your guess is too low

> Enter a guess (1 guess left)

> `60`

> Your guess is too low

> You were unable to guess the number.

> The correct answer was 62
