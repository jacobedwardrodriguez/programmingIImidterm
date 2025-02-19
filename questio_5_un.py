def count_pattern_occurrences(text):
    """
    This function finds and counts all words that:
    - Start with 'un'
    - Have any number of letters in between
    - End with 'an'

    :param text: The text to search in.
    :return: The number of occurrences.
    """
    words = text.split()  # Split text into words
    count = 0  # Initialize counter

    for word in words:
        if word.startswith("un") and word.endswith("an"):
            count += 1  # Increases the count if the word matches the pattern

    return count  # Returns the total count

# Example text
text = "The unseen unbroken unhuman utilitarian union unused uncanny unplan."
print(count_pattern_occurrences(text))  # the number of matches
