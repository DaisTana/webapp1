def split_into_words(input_string):
    """
    Splits the input string into a list of words.

    Args:
        input_string (str): The string to be split.

    Returns:
        list: A list of words in the input string.
    """
    return input_string.split()

def main():
  words = split_into_words("This is a test string")
  print(words)

if __name__ == "__main__":
    main()
