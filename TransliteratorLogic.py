import re

nVowels = 12
# constants 18
# Special Character 1
# all together 247
consonants = []
consonantsUni = []

# 12
vowels = []
vowelsUni = []
vowelModifiersUni = []  # vowels done

# 6
specialConsonants = []
specialConsonantsUni = []
# 1
specialCharUni = []
specialChar = []


def initializeVar():
    vowelsUni.append("ஆ")
    vowels.append("aa")
    vowelModifiersUni.append("ா")
    vowelsUni.append("அ")
    vowels.append("a")
    vowelModifiersUni.append("")
    vowelsUni.append("அ")
    vowels.append("a")
    vowelModifiersUni.append("ா")


    vowelsUni.append("ஓ")
    vowels.append("oo")
    vowelModifiersUni.append("ோ")

    vowelsUni.append("ஒ")
    vowels.append("o")
    vowelModifiersUni.append("ொ")



    vowelsUni.append("ஏ")
    vowels.append("ee")
    vowelModifiersUni.append("ே")

    vowelsUni.append("எ")
    vowels.append("e")
    vowelModifiersUni.append("ெ")

    vowelsUni.append("ஊ")
    vowels.append("uu")
    vowelModifiersUni.append("ூ")

    vowelsUni.append("உ")
    vowels.append("u")
    vowelModifiersUni.append("ு")

    vowelsUni.append("ஈ")
    vowels.append("ii")
    vowelModifiersUni.append("ீ")
    vowelsUni.append("இ")
    vowels.append("i")
    vowelModifiersUni.append("ி")

    vowelsUni.append("அ")
    vowels.append("A")
    vowelModifiersUni.append("")

    vowelsUni.append("ஆ")
    vowels.append("a\\)")
    vowelModifiersUni.append("ா")


    vowelsUni.append("ஈ")
    vowels.append("i\\")
    vowelModifiersUni.append("ீ")
    vowelsUni.append("ஈ")
    vowels.append("II")
    vowelModifiersUni.append("ீ")

    vowelsUni.append("ஊ")
    vowels.append("u\\)")
    vowelModifiersUni.append("ூ")

    vowelsUni.append("ு")
    vowels.append("u")
    vowelModifiersUni.append("ு")


    vowelsUni.append("எ")
    vowels.append("E")
    vowelModifiersUni.append("ெ")

    vowelsUni.append("ஏ")
    vowels.append("e\\")
    vowelModifiersUni.append("ே")


    vowelsUni.append("ஒ")
    vowels.append("O")
    vowelModifiersUni.append("ொ")
    vowelsUni.append("ஓ")
    vowels.append("o\\)")
    vowelModifiersUni.append("ோ")

    vowelsUni.append("ஐ")
    vowels.append("ai)")
    vowelModifiersUni.append("ை")

    vowelsUni.append("ஔ")
    vowels.append("au")
    vowelModifiersUni.append("ௌ")

    vowelsUni.append("ஃ")
    vowels.append("ah")
    vowelModifiersUni.append("ஃ")

    vowelsUni.append("அ")
    vowels.append("A")
    vowelModifiersUni.append("ா")
    vowelsUni.append("எ")
    vowels.append("e")
    vowelModifiersUni.append("ெ")
    vowelsUni.append("உ")
    vowels.append("u")
    vowelModifiersUni.append("ு")
    vowelsUni.append("ஒ")
    vowels.append("o")
    vowelModifiersUni.append("ொ")
    vowelsUni.append("ஐ")
    vowels.append("I")
    vowelModifiersUni.append("ை")

    # consonants 18 + sanskrit 5

    consonantsUni.append("க")
    consonants.append("k")

    consonantsUni.append("க")
    consonants.append("g")

    # consonantsUni.append("க")
    # consonants.append("h")

    consonantsUni.append("ங")
    consonants.append("ng")

    consonantsUni.append("ச")
    consonants.append("c")

    consonantsUni.append("ச")
    consonants.append("ch")

    consonantsUni.append("ச")
    consonants.append("s")

    consonantsUni.append("ச")
    consonants.append("sh\\")

    consonantsUni.append("ஞ")
    consonants.append("gn")

    consonantsUni.append("ட")
    consonants.append("t")

    consonantsUni.append("ட")
    consonants.append("d")

    consonantsUni.append("ண")
    consonants.append("N")

    consonantsUni.append("த")
    consonants.append("th")

    consonantsUni.append("த")
    consonants.append("d")

    consonantsUni.append("ந")
    consonants.append("nh")

    consonantsUni.append("ன")
    consonants.append("n")

    consonantsUni.append("ப")
    consonants.append("p")

    consonantsUni.append("ப")
    consonants.append("f")

    consonantsUni.append("ப")
    consonants.append("b")

    consonantsUni.append("ப")
    consonants.append("bh")

    consonantsUni.append("ம")
    consonants.append("m")

    consonantsUni.append("ய")
    consonants.append("y")

    consonantsUni.append("ர")
    consonants.append("r")

    consonantsUni.append("ற")
    consonants.append("r")

    consonantsUni.append("ல")
    consonants.append("l")

    consonantsUni.append("ள")
    consonants.append("l")

    consonantsUni.append("ழ")
    consonants.append("zh")

    consonantsUni.append("வ")
    consonants.append("v")

    consonantsUni.append("வ")
    consonants.append("w")

    # sanskrit

    consonantsUni.append("ஜ")
    consonants.append("j")

    consonantsUni.append("ஷ")
    consonants.append("sh")

    consonantsUni.append("ஸ")
    consonants.append("s")

    consonantsUni.append("ஹ")
    consonants.append("h")

    consonantsUni.append("ஶ")
    consonants.append("sh")

    consonantsUni.append("க்ஷ")
    consonants.append("ks")

    # SpecialConsonants
    specialConsonantsUni.append("ஂ")
    specialConsonants.append("am")

    specialConsonantsUni.append("ஃ")
    specialConsonants.append("aq")

    specialConsonantsUni.append("ௐ")
    specialConsonants.append("om")

    specialConsonantsUni.append("ௗ")
    specialConsonants.append("au")

    specialConsonantsUni.append("◌்")
    specialConsonants.append("")

    specialConsonantsUni.append("ஂ")
    specialConsonants.append("\\n")

    # specialConsonantsUni.append("ஃ")
    # specialConsonants.append("\\h")

    specialConsonantsUni.append("ங்")
    specialConsonants.append("\\N")

    specialConsonantsUni.append("ண்")
    specialConsonants.append("\\R")

    specialConsonantsUni.append("ஸ்ரீ")
    specialConsonants.append("\\S")

    specialConsonantsUni.append("ஜ்ஞ")
    specialConsonants.append("\\J")

    specialConsonantsUni.append("க்ஷ")
    specialConsonants.append("\\K")

    specialConsonantsUni.append("ஸ")
    specialConsonants.append("\\s")

    specialConsonantsUni.append("ஹ")
    specialConsonants.append("\\h")

    specialConsonantsUni.append("ர்" + "\u200D")
    specialConsonants.append("R")
    specialConsonantsUni.append("ர்" + "\u200D")
    specialConsonants.append("\\r")

    # special character Aytham
    specialConsonantsUni.append("ஃ")
    specialConsonants.append("\\aa")

    # Special Character
    specialCharUni.append("ஸ்ரீ")
    specialChar.append("sri")


initializeVar()


def convertText(text):
    s = ""
    r = ""
    v = ""

    # special characters
    # for i in range(len(specialConsonants)):
    #     text = text.replace(specialConsonants[i], specialConsonantsUni[i])

    for i in range(len(specialChar)):
        text = text.replace(specialChar[i], specialCharUni[i])

        # consonents + special Chars
    for i in range(len(specialCharUni)):
        for j in range(len(consonants)):
            s = consonants[j] + specialChar[i]
            v = consonantsUni[j] + vowelModifiersUni[0] + specialCharUni[i]  # add default vowel
            r = s.replace(s + "/G", "")
            text = text.replace(r, v)
        # consonants + special characters
        # for i in range(len(specialCharUni)):
        #     for j in range(len(consonants)):
        #         s = consonants[j] + specialCharUni[i]
        #         v = consonantsUni[j] + specialCharUni[i]
        #         r = s.replace(s+"/G", "")
        #         text = text.replace(r, v)

        # consonants + Rakaransha + vowel modifiers
        for j in range(len(consonants)):
            for i in range(len(vowels)):
                s = consonants[j] + "r" + vowels[i]
                v = consonantsUni[j] + "்ரு" + vowelModifiersUni[i]
                r = s.replace(s + "/G", "")
                text = text.replace(r, v)
            s = consonants[j] + "r"
            v = consonantsUni[j] + "்ரு"
            r = s.replace(s + "/G", "")
            text = text.replace(r, v)

    # consonants + vowel modifiers
    for i in range(len(consonants)):
        for j in range(nVowels):
            s = consonants[i] + vowels[j]
            v = consonantsUni[i] + vowelModifiersUni[j]
            r = s.replace(s + "/G", "")
            text = text.replace(r, v)

    # consonents + HAL
    for i in range(len(consonants)):
        r = consonants[i].replace("/G", "")
        text = text.replace(r, consonantsUni[i] + "்")

    vowels
    for i in range(len(vowels)):
        r = vowels[i].replace(vowels[i] + "/G", "")
        text = text.replace(r, vowelsUni[i])
    return text

# OLD ONE
# def convertText(text):
#      s=""
#      r=""
#      v=""
#      # text = document.txtBox.box1.value;
#      # special consonents
#      for i in range(len(specialConsonants)):
#          text = text.replace(specialConsonants[i], specialConsonantsUni[i])
#  # consonents + special Chars
#      for i in range(len(specialCharUni)):
#          for j in range(len(consonants)):
#              s = consonants[j] + specialChar[i]
#              v = consonantsUni[j] + specialCharUni[i]
#              # r = new RegExp(s, "g")
#              r = s.replace(s+"/G", "")
#              text = text.replace(r, v)
#
#  # consonants + Rakaransha + vowel modifiers
#      for j in range(len(consonants)):
#          for i in range(len(vowels)):
#              s = consonants[j] + "r" + vowels[i]
#              v = consonantsUni[j] + "්‍ර" + vowelModifiersUni[i]
#              # r = new RegExp(s, "g")
#              r = s.replace(s+"/G", "")
#              text = text.replace(r, v)
#          s = consonants[j] + "r"
#          v = consonantsUni[j] + "්‍ර"
#          # r = new RegExp(s, "g")
#          r = s.replace(s+"/G", "")
#          text = text.replace(r, v)
#  # consonents + vowel modifiers
#      for i in range(len(consonants)):
#          for j in range(nVowels):
#              s = consonants[i] + vowels[j]
#              v = consonantsUni[i] + vowelModifiersUni[j]
#              # r = new RegExp(s, "g")
#              r = s.replace(s+"/G", "")
#              text = text.replace(r, v)
#
#  # consonents + HAL
#      for i in range(len(consonants)):
#          r = consonants[i].replace(consonants[i]+"/G", "")
#          text = text.replace(r, consonantsUni[i] + "◌ீ")
#  # vowels
#      for i in range(len(vowels)):
#          # r = new RegExp(vowels[i], "g")
#          r = vowels[i].replace(vowels[i]+"/G", "")
#          text = text.replace(r, vowelsUni[i])
#
#          return text
