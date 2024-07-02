# Regex Notes

## Table of Contents
1. [What is Regex?](#what-is-regex)
2. [Basic Syntax](#basic-syntax)
3. [Special Sequences](#special-sequences)
4. [Quantifiers](#quantifiers)
5. [Groups and Ranges](#groups-and-ranges)
6. [Anchors](#anchors)
7. [Example Patterns](#example-patterns)
8. [Using Regex in Python](#using-regex-in-python)
9. [Common Pitfalls and Tips](#common-pitfalls-and-tips)
10. [Advanced Topics](#advanced-topics)
    - [Lookaheads and Lookbehinds](#lookaheads-and-lookbehinds)
11. [Use Cases of Regular Expressions](#use-cases-of-regular-expressions)

## What is Regex?

Regular expressions (regex) are sequences of characters that define search patterns. They are used for string matching and manipulation.

## Basic Syntax

- `.`: Matches any single character except newline.
- `*`: Matches 0 or more repetitions of the preceding element.
- `+`: Matches 1 or more repetitions of the preceding element.
- `?`: Matches 0 or 1 repetition of the preceding element.
- `[]`: Matches any one of the characters inside the brackets.
- `^`: Matches the start of the string.
- `$`: Matches the end of the string.

## Special Sequences

- `\d`: Matches any digit. Equivalent to `[0-9]`.
- `\D`: Matches any non-digit character.
- `\w`: Matches any word character (alphanumeric plus underscore). Equivalent to `[a-zA-Z0-9_]`.
- `\W`: Matches any non-word character.
- `\s`: Matches any whitespace character (spaces, tabs, newlines).
- `\S`: Matches any non-whitespace character.

## Quantifiers

- `*`: 0 or more repetitions.
- `+`: 1 or more repetitions.
- `?`: 0 or 1 repetition.
- `{n}`: Exactly n repetitions.
- `{n,}`: At least n repetitions.
- `{n,m}`: Between n and m repetitions.

## Groups and Ranges

- `(abc)`: Matches the exact sequence "abc".
- `(a|b|c)`: Matches any one of "a", "b", or "c".
- `[abc]`: Matches any one of "a", "b", or "c".
- `[a-z]`: Matches any one character from "a" to "z".
- `[^abc]`: Matches any character except "a", "b", or "c".

## Anchors

- `^`: Matches the start of the string.
- `$`: Matches the end of the string.
- `\b`: Matches a word boundary.
- `\B`: Matches a non-word boundary.

## Example Patterns

- `\d{3}-\d{2}-\d{4}`: Matches a Social Security number format (e.g., 123-45-6789).
- `\b[A-Za-z]+\b`: Matches a single word.
- `\w+@\w+\.\w+`: Matches a simple email address format.

## Using Regex in Python

Python's `re` module provides support for working with regular expressions. Here are some common functions:

- `re.match()`: Checks for a match only at the beginning of the string.
- `re.search()`: Searches for a match anywhere in the string.
- `re.findall()`: Finds all matches in the string.
- `re.sub()`: Replaces matches with a specified string.

## Common Pitfalls and Tips

- **Greedy vs. Non-Greedy Matching:** Be aware of greedy (`*`, `+`) vs. non-greedy (`*?`, `+?`) quantifiers. Greedy quantifiers match as much as possible, whereas non-greedy quantifiers match as little as possible.
- **Escaping Special Characters:** Remember to escape special characters (e.g., `.`, `*`, `?`, `+`) with a backslash (`\`) when you want to match them literally.
- **Anchors and Word Boundaries:** Use `^` and `$` to match the start and end of a string, and `\b` for word boundaries. This can help to avoid partial matches.

## Advanced Topics

### Lookaheads and Lookbehinds

- **Positive Lookahead (`(?=...)`):** Asserts that what follows the current position in the string matches the given pattern.
- **Negative Lookahead (`(?!...)`):** Asserts that what follows the current position in the string does not match the given pattern.
- **Positive Lookbehind (`(?<=...)`):** Asserts that what precedes the current position in the string matches the given pattern.
- **Negative Lookbehind (`(?<!...)`):** Asserts that what precedes the current position in the string does not match the given pattern.

### Unicode Matching

Unicode Character Classes: Match characters from different languages and scripts.

### Named Groups

Named Capturing Groups: Assign names to groups for easier reference.

### Conditional Expressions

Conditional Expressions: Match different patterns based on a condition.

### Verbose Mode

Verbose Mode (re.VERBOSE): Write more readable regex by allowing comments and whitespace.

### Recursive Patterns

Recursive Patterns: Match nested structures.

### Atomic Groups

Atomic Groups ((?>...)): Prevent backtracking within a group.

### Flags and Modifiers

•	Using Flags: Modify the behavior of regex patterns.

## Use Cases of Regular Expressions

Regular expressions are extremely versatile and can be used in a variety of scenarios. Here are some common use cases:

- **Data Validation**:

	•	[Email Validation](usecases/email_validation.py): Ensure that input follows the pattern of a valid email address. 

	•	[Phone Number Validation](usecases/phone_number_validation.py): Check if a phone number follows a specific format.

- **Text Processing**:

    •	[Extracting Information](usecases/extracting_information.py): Extract specific information from a larger body of text.
    
	•	[Replacing Text](usecases/replacing_text.py): Perform substitutions in a text based on a pattern.

- **Log File Analysis**:

	•	[Parsing Logs](usecases/parsing_logs.py): Extract useful information from log files.

- **Web Scraping**:

	•	[Extracting Data from HTML](usecases/extracting_data_from_html.py): Use regex to scrape data from web pages (though libraries like BeautifulSoup are often better for this task).

- **Configuration File Parsing**:

	•	[Reading Configurations](usecases/reading_configurations.py): Extract key-value pairs from configuration files
.