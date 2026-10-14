import string


def sanitize_string(text: str) -> str:
    """Convert text to lowercase and remove spaces and punctuation."""
    text = text.lower()
    cleaned = ""

    for char in text:
        if char not in string.punctuation and not char.isspace():
            cleaned += char

    return cleaned


def is_palindrome(text: str) -> bool:
    """Return True if the cleaned text is a palindrome."""
    cleaned = sanitize_string(text)
    return cleaned == cleaned[::-1]


def count_characters(text: str) -> dict:
    """Count how many times each character appears."""
    cleaned = sanitize_string(text)
    counts = {}

    for char in cleaned:
        counts[char] = counts.get(char, 0) + 1

    return counts


if __name__ == "__main__":
    sentence = input("Enter a word or sentence: ")

    cleaned = sanitize_string(sentence)

    print("Cleaned text:", cleaned)
    print("Is palindrome:", is_palindrome(sentence))
    print("Character counts:", count_characters(sentence))