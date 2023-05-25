def get_content(file):
    with open(file, encoding="UTF-8") as fopen:
        content = fopen.readlines()

    return content


def main():
    file = get_content("pan_tadeusz.txt")
    file = set(file)

    biggest_word_len = 0
    biggest_word = ""

    for line in file:
        words = line.split()
        for word in words:
            leng = len(word)
            #print(word, leng)
            if leng > biggest_word_len:
                biggest_word_len = leng
                biggest_word = word

    print(f"Biggest word: {biggest_word} -> długość {biggest_word_len}")


main()
