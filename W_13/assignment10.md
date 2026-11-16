# COMP 170 Assignment 10 - Playlist Manager

## Overview

In this assignment, you will practice working with **lists, searching algorithms, deleting elements while traversing, mutability, tuples, dictionaries, and files**.

You are given a playlist represented by a list of song titles:

```python
playlist = ["Jazz", "Pop", "Rock", "Pop", "Blues", "Pop", "Classical"]
```

Write the following functions to manage the playlist.

---

## Part 1 — Search for a Song (5 pts)

Write `find_song(playlist, song)` that searches for a song and returns its **first index**, or `-1` if the song is not found.

**Example:**

```python
print(find_song(playlist, "Rock"))  # 2
print(find_song(playlist, "Rap"))   # -1
```

**Constraint:** Use a loop. Do not use `index()`.

---

## Part 2 — Remove All Occurrences of a Song (5 pts)

Write `remove_song(playlist, song)` that removes **all occurrences** of the given song from the original playlist.

**Example:**

```python
remove_song(playlist, "Pop")
print(playlist)
# ["Jazz", "Rock", "Blues", "Classical"]
```

**Constraints:**

- Modify the original list without creating a new one.
- Do not use `filter()` or list comprehensions.

---

## Part 3 — Working with Tuples (6 pts)

### Question 1 — Playlist Summary

Write `playlist_summary(playlist)` that returns a tuple containing:

- The number of songs in the playlist.
- The first song (or `None` if the playlist is empty).
- The last song (or `None` if the playlist is empty).

**Example:**

```python
summary = playlist_summary(playlist)
print(summary)
# (4, "Jazz", "Classical")
```

### Question 2 — String Representation

Write `format_summary(summary)` that takes the tuple returned by `playlist_summary()` and returns a string describing the playlist.

**Example:**

```python
print(format_summary(summary))
# "This playlist contains 4 songs, starts with Jazz, and ends with Classical."
```

For an empty playlist, return:

```python
"This playlist is empty."
```

**Hint:** You can access the elements of a tuple using either **indexing** or **unpacking**.

- **Indexing:** Access individual elements using their positions, such as `summary[0]`, `summary[1]`, and `summary[2]`.
- **Unpacking:** Assign the elements of a tuple to separate variables in a single statement.

For example:

```python
count, first, last = summary

print(count)  # 4
print(first)  # Jazz
print(last)   # Classical
```

---

## Part 4 — Counting Songs with Dictionaries (6 pts)

Write `count_songs(playlist)` that creates and returns a dictionary containing the number of occurrences of each song in the playlist.

Each dictionary entry should have:

- **Key:** The song name in uppercase.
- **Value:** The number of times the song appears in the playlist.

**Case-insensitive counting:** Song names should be treated as case-insensitive. Convert each song name to uppercase before using it as a dictionary key. Do not modify the song name in the original playlist.

**Example:**

```python
playlist = ["Jazz", "Pop", "JAZZ", "pop", "Rock", "jazz"]

counts = count_songs(playlist)
print(counts)

# {"JAZZ": 3, "POP": 2, "ROCK": 1}
```

**Hint:**

As you traverse the playlist, check whether each song already exists in the dictionary.

You can use the `get()` method:

```python
mydict.get("JAZZ")
```

This returns the value associated with `"JAZZ"` if it exists, or `None` if it does not.

Alternatively, you can use the `in` operator to check whether a key exists in the dictionary.

If the song is already in the dictionary, you can increase its count by one:

```python
mydict["JAZZ"] += 1
```

Otherwise, add the song to the dictionary with an initial count of `1`.

**Constraint:** Use a loop to traverse the playlist and build the dictionary. Do not use `count()`.

---

## Part 5 — Working with Files (6 pts)

### Question 1 — Save Song Counts to a File

Write `save_playlist(counts, filename)` that takes the dictionary created in Part 4 and writes its contents to a text file.

Each line of the file should contain the **song name and its number of repetitions**, separated by a comma.

**Example:**

```python
counts = {"JAZZ": 3, "POP": 2, "ROCK": 1}

save_playlist(counts, "playlist.txt")
```

The file `playlist.txt` should contain:

```text
JAZZ,3
POP,2
ROCK,1
```

**Requirements:**

- Use a loop to traverse the dictionary.
- Write one song per line.
- The function should create the file if it does not exist and overwrite its contents if it already exists.

### Question 2 — Load a Playlist from a File 

Write `load_playlist(filename)` that reads a file in the format described above and **creates and returns a list of song names**.

Each song should appear in the list as many times as indicated by its count in the file.

**Example:**

Given the following contents of `playlist.txt`:

```text
JAZZ,3
POP,2
ROCK,1
```

Calling:

```python
playlist = load_playlist("playlist.txt")
print(playlist)
```

Should produce:

```python
["JAZZ", "JAZZ", "JAZZ", "POP", "POP", "ROCK"]
```

**Hints:**

- Read the file line by line.
- Use `strip()` to remove the newline character.
- Use `split(",")` to separate the song name from its count.
- Convert the count to an integer using `int()`.
- Use a loop to add each song to the list the required number of times.

**Assumption:** You can assume the file exists and follows the correct format, with a positive integer count on each line.

---

## Part 6 — Understanding Mutability (2 pts)

Consider the following code:

```python
playlist = ["Jazz", "Pop", "Rock", "Pop"]
other_playlist = playlist

remove_song(playlist, "Pop")

print(playlist)
print(other_playlist)
```

**Question:** What will each `print()` statement display? Explain why `other_playlist` is affected even though we never directly modified it.

---

## General Requirements

- Include a **docstring** for every function.
- Use loops to traverse lists and dictionaries where required.
- Do not use `break`, `continue`, or `while True`.
- Do not use built-in methods that directly perform the required task when prohibited.
- Test your functions with different inputs, including empty lists, repeated elements, and elements that are not found.
- Your functions should work for different playlists, not just the examples provided.
