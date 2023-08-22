import pickle
import nltk
nltk.download('punkt')
import TransliteratorLogic
from nltk import PerceptronTagger
from nltk.corpus import TaggedCorpusReader
from nltk.tag import str2tuple, tuple2str
from nltk.corpus import *
from itertools import product
from sklearn.metrics import classification_report
from nltk.translate.bleu_score import corpus_bleu
from sklearn.metrics import precision_score, recall_score, f1_score


y_true = [1, 1, 2, 3, 3, 3]
y_pred = [1, 2, 2, 3, 3, 1]

# compute the precision score


uni_tagger = open("filename.pkl", "rb")

utagger = pickle.load(uni_tagger)

file = open("Tami.txt", "r", encoding='utf-8')
train_text = file.read()
print(train_text)

testData = []
trainData = []
fTrn = open("Tami.txt",
            mode='r', encoding='utf-8')
fTst = open("tanglishTrain.txt",
            mode='r', encoding='utf-8')

for i in fTrn.readlines():
    trainData.append([str2tuple(t) for t in i.split()])
print(trainData)
for i in fTst.readlines():
    testData.append([str2tuple(t) for t in i.split()])

def ngramTranslater(train_sents, n, defaultTag='NNN'):
    t0 = nltk.DefaultTagger(defaultTag)
    if (n <= 0):
        return t0
    elif (n == 1):
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        return t1
    elif (n == 2):
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        t2 = nltk.BigramTagger(train_sents, backoff=t1)
        return t2
    else:
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        t2 = nltk.BigramTagger(train_sents, backoff=t1)
        t3 = nltk.TrigramTagger(train_sents, backoff=t2)
        print(t3)
        return t3

tra =ngramTranslater(trainData,1)
print("Traning Done")
print(tra.evaluate(testData))


#The writeTag() function takes a TSV file containing romanized Tamil and Tamil text, reads it line by line, splits each line into two separate lists
# (one for the romanized Tamil and one for the Tamil text), and then writes the lists to a new TSV file in the format of "romanized/Tamil" separated by a space.
def writeTag():
    write = open("ta.romanized.split.tsv",
                 mode='w', encoding='utf-8')
    read = open("ta.romanized.split.tsv",
                mode='r', encoding='utf-8')
    for i in read:
        tanglish = i.split()
        tamil = next(read).split()
        for n in range(len(tanglish)):
            write.write(tanglish[n] + "/" + tamil[n] + " ")
        write.write("\n")

#The translatorsave() function first calls the ngramTranslater() function with the appropriate arguments to create a trigram tagger from the trainData and testData lists.
# Then, it evaluates the accuracy of the tagger on the test data and prints the result. It saves the trained trigram tagger to a pickle file named "trigramTamil.pickle".
def translatorsave():
    translator = ngramTranslater(trainData, 3, 'NNN')
    print('Trigram Translator Accuracy : ' + str(translator.evaluate(testData)))
    save_translator = open("trigramTamil.pickle", "wb")
    pickle.dump(translator, save_translator)
    save_translator.close()
    #The last line of the code opens the saved pickle file "trigramTamil.pickle" and loads the trained trigram tagger object into the translator variable.
    print("pickle file updated")

#This code loads a trained trigram language model from a saved pickle file named "trigramTamil.pickle".
# The loaded model is then used in the function "triGramTranslate" to translate a given input sentence from Tamil romanized script to Tamil script.
translatorsave()
translateorPic = open("trigramTamil.pickle", "rb")
translator = pickle.load(translateorPic)

# def triGramTranslate(sentence):
#       sentence_romanized=sentence.split(" ")
#       translation = ""
#       translated = translator.tag(nltk.word_tokenize(sentence.lower()))
#       print(translated)
#       i=-1
#       for word, trans in translated:
#           i+=1
#           if trans in ('NNN'):
#             translation = translation + str(TransliteratorLogic.convertText(str(sentence_romanized[i])) + " ")
#           else:
#               translation = translation + str(trans + " ")
#       return translation

def triGramTranslate(sentence):
    sentence_romanized=sentence.split(" ")
    translation = ""
    translated = translator.tag(nltk.word_tokenize(sentence.lower()))
    print(translated)
    i=-1
    for word, trans in translated:
        i+=1
        if i >= len(sentence_romanized):
            break
        if trans in ('NNN'):
            translation = translation + str(TransliteratorLogic.convertText(str(sentence_romanized[i])) + " ")
        else:
            translation = translation + str(trans + " ")
    return translation

# def triGramTranslate(sentance):
#     sentence_romanized = sentance.split()
#     translation = ""
#     translated = translator.tag(nltk.word_tokenize(sentance.lower()))
#     print(translated)
#     for i in range(len(sentence_romanized)):
#         print("i=", i)
#         print("len(sentence_romanized)=", len(sentence_romanized))
#         print("sentence_romanized=", sentence_romanized)
#         translation = translation + str(TransliteratorLogic.convertText(str(sentence_romanized[i])) + " ")
#     return translation


def onlytriGramTranslate(sentence):
    translation = ""
    translated = translator.tag(nltk.word_tokenize(sentence.lower()))
    print(translated)
    for word, trans in translated:
        translation = translation + str(trans + " ")
    return translation

def uniTagger():
    tagger = ngramTranslater(trainData, 1, 'NNN')


def translate(sentence):
    translated = []
    tokened = nltk.word_tokenize(sentence)

    for word in tokened:
        matched = getMatch(word)
        translated.append(matched)
    print(translated)
    unigramtag(translated)


def getMatch(testWord):
    possiblities = []
    splitted = nltk.word_tokenize(train_text)
    for word in splitted:
        pureWord, tanglishWord = word.split("/")

        if (testWord == pureWord):
            if (tanglishWord in possiblities):
                continue
            else:
                possiblities.append(tanglishWord)
    if (len(possiblities) == 0):
        possiblities.append("--")
    return possiblities


def unigramtag(sentence):
    for word in sentence:
        print(utagger.tag(word))


def tagAndTranslate(translatedList):
    sentenceList = list(product(*translatedList))


def testing_model():
    eval_data = []
    with open("Tanglish.txt", mode='r', encoding='utf-8') as f:
        eval_data = f.readlines()

    actual_list_word = []
    predicted_list_word = []
    actual_list_char = []
    predicted_list_char = []

    for i in range(0, len(eval_data), 2):
        # Word-level accuracy
        actual_word = eval_data[i + 1].strip().split()
        predicted_word = triGramTranslate(eval_data[i]).strip().split()
        actual_list_word.append([actual_word])
        predicted_list_word.append(predicted_word)

        # Character-level accuracy
        actual_char = list(eval_data[i + 1].strip())
        predicted_char = list(triGramTranslate(eval_data[i].strip()))
        actual_list_char.append([actual_char])
        predicted_list_char.append(predicted_char)

        print('src=[%s], target=[%s], predicted=[%s]' % (eval_data[i].strip(),
                                                         eval_data[i + 1].strip(),
                                                         triGramTranslate(eval_data[i]).strip()))

    # Calculate word-level BLEU score
    bleu_score_word = corpus_bleu(actual_list_word, predicted_list_word)

    # Calculate character-level BLEU score
    bleu_score_char = corpus_bleu(actual_list_char, predicted_list_char,
                                  weights=(1, 0, 0, 0))

    print('Word-level BLEU: %f' % bleu_score_word)
    print('Character-level BLEU: %f' % bleu_score_char)
testing_model()

#Generating the N gram model and saving the into a pkl file
translatorsave()


def translatorAcuracy():
    read = open("Tanglish.txt",
                mode='r', encoding='utf-8')
    Nwronng = 0
    Nright = 0
    N = 0
    for i in read:
        tanlish = onlytriGramTranslate(i).split()
        tamil = next(read).split()
        N = N + len(tanlish)
        for n in range(len(tanlish)):
            if (tanlish[n] == tamil[n]):
                Nright = Nright + 1
            else:
                Nwronng = Nwronng + 1

    print(N, Nwronng, Nright, Nright / N)

precision = precision_score(y_true, y_pred, average='weighted')

# compute the f1 score
f1 = f1_score(y_true, y_pred, average='weighted')

# print the results
print('Precision:', precision)
print('F1 Score:', f1)

def confusionmat():
    tamil = []
    romanized = []
    read = open("Tanglish.txt", mode='r', encoding='utf-8')
    for i in read:
        roman_text = triGramTranslate(i.strip())
        tamil_text = next(read).strip()
        roman_words = roman_text.split()
        tamil_words = tamil_text.split()
        for n in range(len(roman_words)):
            tamil.append(tamil_words[n])
            romanized.append(roman_words[n])
    print(classification_report(tamil, romanized, zero_division=0))

confusionmat()

# while True:
#      input1 =input("Enter a sentence")
#      print(triGramTranslate(input1))