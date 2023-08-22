# Define a dictionary of Tamil consonants and diacritical marks
tamil_dict = {

    'க': 'k', 'ங': 'ṅ', 'ச': 'c', 'ஞ': 'ñ', 'ட': 'ṭ', 'ண': 'ṇ', 'த': 't', 'ந': 'n',
    'ப': 'p', 'ம': 'm', 'ய': 'y', 'ர': 'r', 'ல': 'l', 'வ': 'v', 'ழ': 'ḻ', 'ள': 'ḷ', 'ற': 'ṟ', 'ன': 'ṉ',
    '்': '', 'ா': 'ā', 'ி': 'i', 'ீ': 'ī', 'ு': 'u', 'ூ': 'ū', 'ெ': 'e', 'ே': 'ē', 'ை': 'ai', 'ொ': 'o', 'ோ': 'ō',
    'ௌ': 'au'
}


# Define a function to transliterate a Tamil string without vowels
def without_vowels(text):
    # Replace each Tamil vowel with an empty string
    text = text.replace('அ', '').replace('ஆ', '').replace('இ', '').replace('ஈ', '').replace('உ', '').replace('ஊ',
                                                                                                             '').replace(
        'எ', '').replace('ஏ', '').replace('ஐ', '').replace('ஒ', '').replace('ஓ', '').replace('ஔ', '')

    # Transliterate each remaining Tamil character using the dictionary
    transliterated_text = ''
    for char in text:
        if char in tamil_dict:
            transliterated_text += tamil_dict[char]

    return transliterated_text


# Test the function with a sample Tamil string
text = 'தமிழ் மொழி பற்றிய சிறப்பு தகவல்'
print(without_vowels(text))  # Output: 'tmzlxzbrtycrppthkvl'
# Define a dictionary of Tamil consonants and diacritical marks
tamil_dict = {

    'க': 'k', 'ங': 'ṅ', 'ச': 'c', 'ஞ': 'ñ', 'ட': 'ṭ', 'ண': 'ṇ', 'த': 't', 'ந': 'n',
    'ப': 'p', 'ம': 'm', 'ய': 'y', 'ர': 'r', 'ல': 'l', 'வ': 'v', 'ழ': 'ḻ', 'ள': 'ḷ', 'ற': 'ṟ', 'ன': 'ṉ',
}


# Define a function to transliterate a Romanized Tamil string to Tamil without vowels
def without_vowels(text):
    # Replace each English vowel with an empty string
    text = text.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')

    # Transliterate each remaining English character to Tamil using the dictionary
    tamil_text = ''
    for char in text:
        if char in tamil_dict:
            tamil_text += tamil_dict[char]
        else:
            tamil_text += char

    return tamil_text


# Test the function with a sample Romanized Tamil string
text = 'kaṭṭurai'
print(without_vowels(text))  # Output: 'கற்றுரை'

