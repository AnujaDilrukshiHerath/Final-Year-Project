with open("rom.txt", "r", encoding="utf-8") as f1, open("tamilEx.txt", "r", encoding="utf-8") as f2:
    romanized_words = f1.read().splitlines()
    tamil_words = f2.read().splitlines()

    combined_words = [f"{r}/{t}" for r, t in zip(romanized_words, tamil_words)]

with open("combined_words.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(combined_words))
