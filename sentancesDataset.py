import re
def combine_sentences():
    with open('rom.txt', 'r', encoding='utf-8') as f:
        roman_sentence = f.read()
    with open('tamilEx.txt', 'r', encoding='utf-8') as f:
        tamil_sentence = f.read()
    print("Number of sentences in 'rom.txt':", roman_sentence.count('.'))
    print("Number of sentences in 'tamilEx.txt':", tamil_sentence.count('.'))

    roman_sentences = re.split(r'[.!?]+\s*', roman_sentence)
    tamil_sentences = re.split(r'[.!?]+\s*', tamil_sentence)
    if len(roman_sentences) != len(tamil_sentences):
        return f"Error: number of sentences in Tamil and Romanized sentences do not match - Roman sentences: {len(roman_sentences)}, Tamil sentences: {len(tamil_sentences)}"

        # return an error message if the number of sentences in the Tamil and Romanized sentences do not match
        #return "Error: number of sentences in Tamil and Romanized sentences do not match "

    combined = []
    for i in range(len(roman_sentences)):
        roman_words = roman_sentences[i].split()
        tamil_words = tamil_sentences[i].split()
        if len(roman_words) != len(tamil_words):
            # return an error message if the number of words in the Tamil and Romanized sentences do not match
            return f"Error: number of words in Tamil and Romanized sentences do not match in sentence {i+1}"
        sentence = ''
        for j in range(len(roman_words)):
            sentence += roman_words[j] + separator + tamil_words[j] + ' '
        combined.append(sentence.strip())
    return combined

separator = '/'
combined_sentences = combine_sentences()
if "Error: number of sentences in Tamil and Romanized sentences do not match" in combined_sentences:
    print(combined_sentences)
elif "Error: number of words in Tamil and Romanized sentences do not match" in combined_sentences:
    print(combined_sentences)
else:
    with open('combined.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(combined_sentences))
    print("Sentences combined successfully and written to 'combined.txt' file.")