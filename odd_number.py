import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
print(random_numbers)


#filtering out odd and doubles evens
processed_numbers = [num * 2 for num in random_numbers if num % 2 == 0]

# Print the original and processed lists
print("Original list:", random_numbers)
print("Processed list:", processed_numbers)


def is_valid_url(url):
    """
    Checks if the given string is a valid URL.
    A valid URL must start with 'http://' or 'https://'
    and contain at least one '.' after the scheme.

    :param url: The string to check
    :return: True if valid, False if not
    """
    if len(url) < 8:
        return False  # is minimum length for a valid URL

    if not (url.startswith("http://") or url.startswith("https://")):
        return False  # it must start with a valid scheme

    if "." not in url:
        return False  # Must contain at least one dot

    return True


# Examples
print(is_valid_url("https://example.com"))  # True
print(is_valid_url("http://google.com"))  # True
print(is_valid_url("www.example.com"))  # False
print(is_valid_url("example"))  # False




