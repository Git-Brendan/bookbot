def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    unique_chars = {}
    for char in text.lower():
        if char in unique_chars:
            unique_chars[char] += 1
        else:
            unique_chars[char] = 1

    return unique_chars

def sorted_char_count(unique_chars):
    return dict(sorted(unique_chars.items(), key=lambda item: item[1], reverse=True))
