## 1.1 Functions only, two customers

Use these functions:

```python
def deposit(balance: float, amount: float) -> float:
    """Return the balance after depositing amount."""
    return balance + amount

def withdraw(balance: float, amount: float) -> float:
    """Return the balance after withdrawing amount."""
    return balance - amount
```

Ada starts with `100.0` and Bo starts with `20.0`. Make Ada deposit `50.0`, Bo deposit `15.0`, and Ada withdraw `30.0`. Print both balances.

**Expected output**

```text
Ada 120.0
Bo 35.0
```

1. List every variable you created. Which ones belong together?
2. Write one incorrect line that runs without an error but mixes up the customers.
3. Explain why having no explicit connection between a customer, their balance, and the functions is a problem.

## 1.2 Procedural or object-oriented?

Classify each line as procedural style or object style. For object style, identify the object and method.

```python
# a
total = add_item(total, 4.99)
# b
cart.add_item("pen", 4.99)
# c
words = text.split()
# d
temps.append(72)
# e
area = rectangle_area(width, height)
# f
count = len(names)
```

For line f, explain your classification. Why might Python's designers have made `len` a function instead of a method?

## 1.3 Spot the missing link

```python
player1_name = "Ana"
player1_score = 0
player2_name = "Ben"
player2_score = 0

def add_points(score: int, points: int) -> int:
    """Return score increased by points."""
    return score + points

player2_score = add_points(player1_score, 10)
```

1. What is wrong with the last line? Why doesn't Python complain?
2. Name a class that could hold a player's name and score together.
3. List its two attributes and at least two methods.

## 2.1 Model it

For each item, list two attributes and two method names:

- A library book
- A thermostat
- A playlist
- An object of your choice

## 2.2 Build a Thermostat

Write class `Thermostat`. Its `__init__` takes `location: str` and `temperature: float = 68.0` and stores both as attributes.

**Test script**

```python
kitchen = Thermostat("Kitchen")
office = Thermostat("Office", 72.5)
print(kitchen.location, kitchen.temperature)
print(office.location, office.temperature)
```

**Expected output**

```text
Kitchen 68.0
Office 72.5
```

## 2.3 Predict the output

Using `Thermostat` from 2.2, predict the output before running the code. Explain any differences from your prediction.

```python
a = Thermostat("Lab")
b = a
b.temperature = 75.0
c = Thermostat("Lab")
print(a.temperature, b.temperature, c.temperature)
print(a is b, a is c)
```

How many `Thermostat` objects exist? Explain.

## 2.4 Find the bugs

Find and fix the two bugs. First predict what happens when this program runs.

```python
class Student:
    """A student with a name and a GPA."""

    def __init__(name: str, gpa: float = 0.0) -> None:
        """Create a student."""
        self.name = name
        gpa = gpa

s = Student("Kim", 3.5)
print(s.gpa)
```

**Expected output after the fix**

```text
3.5
```

## 2.5 A class and its client

1. Put only your `Thermostat` class in `thermostat.py`. Run the file. What does it print?
2. Write `thermostat_main.py` in the same folder. Use `from thermostat import *`. In `main()`, create three thermostats, including one with the default temperature, and print each location and temperature. Call `main()`.
3. Explain the difference between the two files in one sentence.

## 3.1 Statement and interest

Extend the slides' `BankAccount` class (`__init__`, `deposit`, and `withdraw`):

- Store a transaction history as a list of strings. Record deposits, withdrawals, and interest using the format shown below.
- Add `apply_interest(self, rate: float) -> None`. Calculate interest as `round(balance * rate, 2)`, add it to the balance, and record it.
- Add `statement(self) -> str`. Use a string accumulator to return the report shown below.

**Test script**

```python
acct = BankAccount("Ada", 100.0)
acct.deposit(50.0)
acct.withdraw(30.0)
acct.apply_interest(0.05)
print(acct.statement())
```

**Expected output**

```text
Statement for Ada
  deposit 50.0
  withdraw 30.0
  interest 6.0
Balance: $126.0
```

**Extra:** Add `count_withdrawals(self) -> int`. It returns `1` for this test.

## 3.2 Give the Thermostat behavior

Add these methods to `Thermostat` from 2.2:

| Method | Required behavior |
| --- | --- |
| `get_temperature(self) -> float` | Return the current temperature. |
| `raise_temp(self, degrees: float) -> None` | Increase the temperature. Raise `ValueError` if `degrees <= 0`. |
| `lower_temp(self, degrees: float) -> None` | Decrease the temperature. Raise `ValueError` if `degrees <= 0`. |
| `is_cold(self) -> bool` | Return whether the temperature is below `65.0`. |
| `__str__(self) -> str` | Return text such as `Kitchen: 68.0F`. |

**Essential hint:** Validate an argument before changing the object's attributes.

**Test script**

```python
kitchen = Thermostat("Kitchen")
office = Thermostat("Office", 72.5)
kitchen.lower_temp(5.0)
office.raise_temp(1.5)
print(kitchen)
print(office)
print(kitchen.is_cold(), office.is_cold())
print(office.get_temperature())
```

**Expected output**

```text
Kitchen: 63.0F
Office: 74.0F
True False
74.0
```

## 3.3 Accessor or mutator?

Classify each `BankAccount` method as an accessor or mutator:

- `get_balance()`
- `deposit(amount)`
- `can_afford(amount)`
- `transfer(other, amount)`
- `apply_interest(rate)`
- `statement()`
- `count_withdrawals()`
- `__str__()`

Why might a class design keep `deposit` from also returning the new balance?

## 3.4 Trace one account

For each line, state whether it raises an error and give the balance afterward. Use the slides' `BankAccount`, where withdrawing more than the balance raises `ValueError`.

For this trace, continue to the next line after recording an error.

```python
acct = BankAccount("Cy", 50.0)
acct.deposit(25.0)
acct.withdraw(80.0)
acct.withdraw(75.0)
acct.deposit(10.0)
acct.get_balance()
```

Which method call returns the balance? Which calls change the object?

## 3.5 A tally counter

Write class `TallyCounter`:

- `__init__(self, limit: int = 9999)` stores the limit and starts the count at `0`.
- `click(self) -> None` adds `1`. If already at the limit, raise `ValueError("limit reached")` without changing the count.
- `get_count(self) -> int` returns the count.
- `reset(self) -> None` resets the count to `0`.

**Test script**

```python
door = TallyCounter(3)
door.click()
door.click()
door.click()
print(door.get_count())
door.reset()
print(door.get_count())
door.click()
print(door.get_count())
```

**Expected output**

```text
3
0
1
```

Then call `door.click()` three more times. The first two calls succeed; the third raises `ValueError: limit reached`, leaving the count at `3`.

## 4.1 Outside or inside?

A `Playlist` class provides `add_song(title)`, `count() -> int`, and `shuffle()`. Classify each item as part of its outside view (interface) or an inside detail (implementation):

1. The method name `add_song` and its parameter `title`.
2. The attribute `self.songs` is a list of strings.
3. The docstring of `count`: "Return the number of songs."
4. `count()` returns an `int`.
5. The loop inside `shuffle` that swaps songs.
6. The name of the variable storing a random index in `shuffle`.
7. Calling `shuffle()` changes the order of the songs.

## 4.2 Use a class you cannot see

Use this interface:

| Call | Behavior |
| --- | --- |
| `Die(sides: int = 6)` | Create a die with the given number of sides. |
| `roll(self) -> int` | Return a random face from `1` through `sides`. |
| `get_last_roll(self) -> int` | Return the most recent face, or `0` before the first roll. |

1. Without implementing `Die`, write `dice_main.py`. Create two six-sided dice, roll each 20 times, count matching pairs, and print a line such as `Doubles: 3 out of 20`.
2. Implement the interface in `die.py`. Use `random.randint(1, sides)`.
3. Run the client. Did you need to change it after implementing the class? Explain.

## 4.3 Same outside, different inside

Rewrite `Thermostat` from 3.2 to store temperature only in `self.celsius`. Keep the location attribute and the same public method names, parameters, and behavior. The constructor and methods must still accept or return Fahrenheit where applicable.

- Convert using `c = (f - 32) * 5 / 9` and `f = c * 9 / 5 + 32`.
- A change of `d` degrees Fahrenheit equals `d * 5 / 9` degrees Celsius.
- `get_temperature()` returns Fahrenheit rounded to one decimal place.
- Do not store a Fahrenheit attribute.

Run the unchanged test script from 3.2; its output must remain identical.

What happens if a client uses `print(office.temperature)` instead of `get_temperature()`? What does this show about accessing attributes directly?

## 4.4 Explain abstraction

1. Define abstraction and give an everyday example other than a music player.
2. List three Python features you have used without knowing their internal implementation.
3. Three teammates are writing a `Library` class, a `Member` class, and a client program. What must they agree on first? Which details can each implement independently?

## T1 Rectangle

Write class `Rectangle`:

- `__init__(self, width: float, height: float)` raises `ValueError` if either side is not positive.
- `area() -> float`, `perimeter() -> float`, and `is_square() -> bool` return the corresponding results.
- `scale(self, factor: float) -> None` multiplies both sides by `factor`. Raise `ValueError` if it is not positive.
- `__str__()` returns text such as `Rectangle 3.0 x 4.0`.

**Test script**

```python
r = Rectangle(3.0, 4.0)
print(r)
print(r.area(), r.perimeter(), r.is_square())
r.scale(2.0)
print(r, r.area())
sq = Rectangle(5.0, 5.0)
print(sq.is_square())
```

**Expected output**

```text
Rectangle 3.0 x 4.0
12.0 14.0 False
Rectangle 6.0 x 8.0 48.0
True
```

## T2 Book progress

Write class `Book`:

- `__init__(self, title: str, author: str, pages: int)` starts the current page at `0`.
- `read(self, count: int) -> None` advances by `count` pages without passing the last page. Raise `ValueError` if `count` is not positive.
- `progress(self) -> float` returns the percentage read, rounded to one decimal place.
- `is_finished(self) -> bool` reports whether the last page has been reached.
- `__str__()` uses the format below.

**Test script**

```python
bk = Book("Clean Loops", "R. Ortiz", 200)
bk.read(50)
print(bk)
print(bk.progress())
bk.read(500)
print(bk.is_finished(), bk.progress())
```

**Expected output**

```text
Clean Loops by R. Ortiz (page 50 of 200)
25.0
True 100.0
```

## T3 Point

Write class `Point`:

- `__init__(self, x: int = 0, y: int = 0)` stores the coordinates.
- `translate(self, dx: int, dy: int) -> None` moves the point.
- `distance_from_origin(self) -> float` and `distance(self, other: "Point") -> float` calculate distances using `math.sqrt`.
- `__str__()` returns text such as `(3, 4)`.

**Test script**

```python
p1 = Point(3, 4)
p2 = Point()
print(p1, p2)
print(p1.distance_from_origin())
p2.translate(6, 8)
print(p2, p1.distance(p2))
p3 = Point(y=2, x=1)
print(p3)
```

**Expected output**

```text
(3, 4) (0, 0)
5.0
(6, 8) 5.0
(1, 2)
```

## T4 Temperature log

Write class `TempLog` with `__init__(self, city: str)` and an empty list of temperatures. Use loops for calculations; do not use `sum` or `max`.

- `add(self, temp: float) -> None` stores a temperature.
- `count(self) -> int` returns the number of entries.
- `average(self) -> float` returns the average rounded to one decimal place.
- `highest(self) -> float` returns the highest temperature.
- `average()` and `highest()` raise `ValueError` for an empty log.
- `count_above(self, limit: float) -> int` counts temperatures strictly above `limit`.

**Test script**

```python
log = TempLog("Chicago")
for t in [68, 72, 75, 61, 80]:
    log.add(t)
print(log.count(), log.average(), log.highest(), log.count_above(70))
```

**Expected output**

```text
5 71.2 80 3
```

## T5 Coin jar

Write class `CoinJar`:

- `__init__(self)` starts with `0` cents. Store the amount as an integer number of cents.
- `add_coins(self, quarters: int = 0, dimes: int = 0, nickels: int = 0, pennies: int = 0) -> None` adds the coins. Raise `ValueError` if any count is negative.
- `total(self) -> float` returns the amount in dollars.
- `empty(self) -> None` resets the amount to `0`.
- `__str__()` returns text such as `Jar: $1.72`.

**Test script**

```python
jar = CoinJar()
jar.add_coins(quarters=5, pennies=7)
jar.add_coins(dimes=3, nickels=2)
print(jar.total())
print(jar)
jar.empty()
print(jar.total())
```

**Expected output**

```text
1.72
Jar: $1.72
0.0
```

Why is storing cents as an `int` safer than storing dollars as a `float`?

## T6 Sentence statistics

Write class `Sentence`:

- `__init__(self, text: str)` stores the text.
- `word_count(self) -> int` returns the number of words.
- `longest_word(self) -> str` returns the longest word, choosing the first if tied.
- `average_word_length(self) -> float` returns the average length rounded to two decimal places. Raise `ValueError` if there are no words.

**Test script**

```python
s = Sentence("Objects bundle state and behavior together")
print(s.word_count(), s.longest_word(), s.average_word_length())
```

**Expected output**

```text
6 behavior 6.17
```

Also check that `Sentence(" ").average_word_length()` raises `ValueError`.

## T7 Two players

Write class `Player`:

- `__init__(self, name: str)` starts the score at `0`.
- `add_points(self, points: int) -> None` raises `ValueError` for negative points; otherwise it adds the points.
- `get_score(self) -> int` returns the score.
- `beats(self, other: "Player") -> bool` returns whether this player's score is strictly higher.
- `__str__()` returns text such as `Ana: 12`.

**Test script — complete the last part**

```python
ana = Player("Ana")
ben = Player("Ben")
ana_points = [5, 2, 5]
ben_points = [3, 6, 2]
for i in range(len(ana_points)):
    ana.add_points(ana_points[i])
    ben.add_points(ben_points[i])
print(ana)
print(ben)
# Print "Winner: <name>" or "Tie" using beats().
```

**Expected output**

```text
Ana: 12
Ben: 11
Winner: Ana
```

## T8 Debug the rectangle

Predict what this program does, then find and fix its four bugs.

```python
class Rectangle:
    """A rectangle with a width and a height."""

    def __init__(self, width: float, height: float) -> None:
        """Create a rectangle."""
        self.width = width
        height = height

    def area() -> float:
        """Return the area."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Return the perimeter."""
        print(2 * (self.width + self.height))

r = Rectangle(3, 4)
print(r.area)
print(r.perimeter() + 1)
```

**Expected output after the fix**

```text
12
15
```

## C1 A bank with many accounts

Extend `BankAccount` from 3.1 with `transfer(self, other, amount)` and `__str__()` using the format `Ada: $60.0`. Write class `Bank`, which stores a list of `BankAccount` objects.

| Method | Required behavior |
| --- | --- |
| `__init__(self, name: str)` | Store the bank name and an empty account list. |
| `open_account(self, owner: str, balance: float = 0.0) -> BankAccount` | Create, store, and return an account. Reject duplicate owners with `ValueError`. |
| `find(self, owner: str) -> BankAccount` | Return the account or raise `ValueError("no account for " + owner)`. |
| `transfer(self, from_owner: str, to_owner: str, amount: float) -> None` | Use `BankAccount.transfer` to move money. A failed transfer must change neither account. |
| `month_end(self, rate: float) -> None` | Apply interest to every account. |
| `total_deposits(self) -> float` | Return the sum of all balances. |
| `richest(self) -> BankAccount` | Return the account with the highest balance; choose the first if tied. |
| `report(self) -> str` | Return the report shown below. |

**Test script**

```python
bank = Bank("Lakeshore Bank")
bank.open_account("Ada", 100.0)
bank.open_account("Bo", 20.0)
bank.open_account("Cy")
bank.transfer("Ada", "Cy", 40.0)
bank.find("Bo").deposit(30.0)
bank.month_end(0.10)
print(bank.report())
print(bank.richest().owner)
```

**Expected output**

```text
Lakeshore Bank: 3 accounts
  Ada: $66.0
  Bo: $55.0
  Cy: $44.0
Total: $165.0
Ada
```

Also test these calls separately:

| Call | Expected error |
| --- | --- |
| `bank.open_account("Ada")` | `ValueError: Ada already has an account` |
| `bank.transfer("Bo", "Zed", 5.0)` | `ValueError: no account for Zed` |
| `bank.transfer("Bo", "Ada", 500.0)` | `ValueError: insufficient funds`; both balances remain unchanged. |

## C2 Gradebook

Write `Student` and `Course`. A `Course` stores a list of `Student` objects.

| Student method | Required behavior |
| --- | --- |
| `__init__(self, name: str)` | Store the name and an empty score list. |
| `add_score(self, score: float) -> None` | Store the score. If outside 0–100, raise `ValueError("score must be between 0 and 100")`. |
| `average(self) -> float` | Return the average rounded to one decimal place, or `0.0` if there are no scores. |
| `letter_grade(self) -> str` | Use the rounded average: A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, otherwise F. |
| `__str__(self) -> str` | Return text such as `Kim: 91.7 (A)`. |

| Course method | Required behavior |
| --- | --- |
| `__init__(self, name: str)` | Store the name and an empty student list. |
| `add_student(self, name: str) -> Student` | Create, store, and return a student. Raise `ValueError` for duplicate names. |
| `find(self, name: str) -> Student` | Return the student or raise `ValueError`. |
| `class_average(self) -> float` | Return the average of the students' averages, rounded to one decimal place. |
| `top_student(self) -> Student` | Return the student with the highest average; choose the first if tied. |
| `honor_roll(self) -> list` | Return names of students with an A, in enrollment order. |
| `report(self) -> str` | Return the report shown below. |

**Test script**

```python
course = Course("COMP 170")
kim = course.add_student("Kim")
lee = course.add_student("Lee")
ana = course.add_student("Ana")
for score in [95, 88, 92]:
    kim.add_score(score)
for score in [72, 85, 79]:
    lee.add_score(score)
for score in [90, 91, 89]:
    ana.add_score(score)
print(course.report())
print(course.honor_roll())
print(course.top_student().name)
```

**Expected output**

```text
COMP 170: 3 students
  Kim: 91.7 (A)
  Lee: 78.7 (C)
  Ana: 90.0 (A)
Class average: 86.8
['Kim', 'Ana']
Kim
```

## C3 Fractions

Write class `Fraction`. Store fractions in lowest terms with a positive denominator; for example, `Fraction(6, -8)` becomes `-3/4`. Use `math.gcd` to reduce fractions.

| Method | Required behavior |
| --- | --- |
| `__init__(self, numerator: int, denominator: int = 1)` | Reduce and normalize the sign. For a zero denominator, raise `ValueError("denominator cannot be 0")`. |
| `get_numerator(self) -> int` | Return the numerator. |
| `get_denominator(self) -> int` | Return the denominator. |
| `add`, `subtract`, `multiply`, `divide` | Each takes another `Fraction` and returns a new `Fraction`, leaving both operands unchanged. Division by a zero fraction raises `ValueError("cannot divide by zero")`. |
| `to_float(self) -> float` | Return the decimal value. |
| `equals(self, other: "Fraction") -> bool` | Return whether both fractions have the same value. |
| `__str__(self) -> str` | Return text such as `3/4`, or `2` if the denominator is 1. |

**Test script**

```python
a = Fraction(1, 2)
b = Fraction(3, 4)
c = Fraction(6, -8)
print(a, b, c)
print(a.add(b))
print(b.subtract(b))
print(a.multiply(c))
print(a.divide(b))
print(b.equals(Fraction(9, 12)))
print(c.to_float())
print(a)
```

**Expected output**

```text
1/2 3/4 -3/4
5/4
0
-3/8
2/3
True
-0.75
1/2
```

Why is returning a new object a useful design for fraction arithmetic?

## C4 Library

Write three cooperating classes:

- `Book(title: str, author: str)` starts not checked out. Its `__str__()` returns text such as `Clean Loops by R. Ortiz`, adding ` (checked out)` when appropriate.
- `Member(name: str, limit: int = 3)` stores a list of borrowed `Book` objects. Implement `can_borrow(self) -> bool` and `__str__()` using the format `Sam: 2 of 2 books`.
- `Library()` stores a list of `Book` objects and provides the methods below.

| Library method | Required behavior |
| --- | --- |
| `add_book(self, title: str, author: str) -> Book` | Create, store, and return a book. |
| `find_book(self, title: str) -> Book` | Return the book or raise `ValueError("no book titled " + title)`. |
| `check_out(self, member: Member, title: str) -> None` | Lend the book and update the member's borrowed list. Raise `ValueError` if already checked out or if the member has reached the borrowing limit. |
| `return_book(self, member: Member, title: str) -> None` | Return the book and update the member's borrowed list. Raise `ValueError` if the member does not have it. |
| `available_titles(self) -> list` | Return available titles in the order the books were added. |
| `report(self) -> str` | Return the report shown below. |

Use error messages such as `Clean Loops is already checked out` and `Sam has reached the limit of 2 books`.

**Test script**

```python
lib = Library()
lib.add_book("Clean Loops", "R. Ortiz")
lib.add_book("Objects First", "M. Chen")
lib.add_book("Shell Basics", "T. Okafor")
sam = Member("Sam", 2)
lib.check_out(sam, "Clean Loops")
lib.check_out(sam, "Shell Basics")
print(lib.available_titles())
print(sam)
print(lib.report())
lib.return_book(sam, "Clean Loops")
print(lib.available_titles())
lib.check_out(sam, "Objects First")
lib.check_out(sam, "Clean Loops")
```

**Expected output**

```text
['Objects First']
Sam: 2 of 2 books
Library: 3 books, 1 available
  Clean Loops by R. Ortiz (checked out)
  Objects First by M. Chen
  Shell Basics by T. Okafor (checked out)
['Clean Loops', 'Objects First']
Traceback (most recent call last):
  ...
ValueError: Sam has reached the limit of 2 books
```
