tData = []  # tamil data tuple
eData = []  # english data tuple

lstword = []
final = []

import pickle
import TransliteratorLogic


def clearlstword():
    global lstword
    lstword = []


def translate(txt):
    global lstword
    lstword.clear()
    if len(txt)==0:
        return lstword
    else:
        l=t.printAutoSuggestions(txt.strip(), 2)
    #if len(txt) >= 5:
       # t.printAutoSuggestions(txt, 1)
    #else:
       # t.printAutoSuggestions(txt, 2)
    #print(lstword)
        return l


class TrieNode():
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False


class Trie():

    def __init__(self):

        # Initialising the trie structure.
        self.root = TrieNode()

    def formTrie(self, keys):

        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key in keys:
            self.insert(key)  # inserting one key to the trie.

    def insert(self, key):

        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        node = self.root

        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

    def suggestionsRec(self, node, word):

        # Method to recursively traverse the trie
        # and return a whole word.
        lstword=[]
        txt=str(TransliteratorLogic.convertText(word))
        print(txt)
        lstword.append(txt)
        if node.last:
            sin_indexes = [n for n, x in enumerate(eData) if x == word]
            for i in sin_indexes:
                y = int(i)
                if tData[y] not in lstword:
                    print(tData[y])
                    lstword.append(tData[y])
        return lstword
                    
    def suggestionsRecsuffix(self, node, word):

        # Method to recursively traverse the trie
        # and return a whole word.
        if node.last:
            sin_indexes = [n for n, x in enumerate(eData) if x == word]
            for i in sin_indexes:
                y = int(i)
                if tData[y] not in lstword:
                    # print(sData[y])
                    lstword.append(tData[y])

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key, para):

        # adding text using rule
        # lstword.append(str(TranslaterLogic.convertText(key)))

        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.

        node = self.root

        for a in key:
            # no string in the Trie has this prefix
            if not node.children.get(a):
                return 0
            node = node.children[a]

        # If prefix is present as a word, but
        # there is no subtree below the last
        # matching node.
        if not node.children:
            return -1
        if para == 1:
            lst=self.suggestionsRecsuffix(node, key)
            return lst
        else:
            lst=self.suggestionsRec(node, key)
            return lst

    def testmodel(self):
        foundflag = 0
        totalflag = 0
        eval_data = list()
        f = open("tanglishSuggestion.txt",
                 mode='r', encoding='utf-8')
        for i in f:
            eval_data.append(i)
        a = list()  # actual_list
        p = list()  # predicted_list
        for i in range(0, len(eval_data), 2):
            engnewlist = eval_data[i].strip('\n').split(" ")
            print(engnewlist)
            sinnewlist = eval_data[i + 1].strip('\n').split(" ")
            print(sinnewlist)
            for j in range(len(engnewlist)):
                totalflag += 1
                try:
                    t.printAutoSuggestions(engnewlist[j], 2)
                    if (sinnewlist[j] in lstword):
                        foundflag += 1
                except:
                    continue

        print("No of total words : ", totalflag)
        print("No of correct suggestions : ", foundflag)
        acc = foundflag / totalflag
        print("Accuracy :", acc)


# Code for creating trie

textFile = open("Tami.txt",
                mode='r', encoding='utf-8')
for i in textFile:
    txt = i.split("/")
    eData.append(txt[0])
    tData.append(txt[0].strip('\n'))

keys = eData
# keys to form the trie structure.
# creating trie object
t = Trie()

# creating the trie structure with the
# given set of strings.
t.formTrie(keys)
print("Trie generated .")

#t.testmodel()
