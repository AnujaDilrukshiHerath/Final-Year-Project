import TransliteratorLogic

class TrieNode():
    def __init__(self):
        self.children = {}
        self.last = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def formTrie(self, keys):
        for key in keys:
            self.insert(key)

    def insert(self, key):
        node = self.root
        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]
        node.last = True

    def suggestionsRec(self, node, word):
        if node.last:
            tam_indexes = [n for n, x in enumerate(eData) if x == word]
            for i in tam_indexes:
                y = int(i)
                if tData[y] not in lstword:
                    lstword.append(tData[y])
        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def suggestionsRecsuffix(self, node, word):
        if node.last:
            tam_indexes = [n for n, x in enumerate(eData) if x == word]
            for i in tam_indexes:
                y = int(i)
                if tData[y] not in lstword:
                    lstword.append(tData[y])
        for a, n in node.children.items():
            self.suggestionsRecsuffix(n, word + a)

    def printAutoSuggestions(self, key, para):
        lstword.clear()  # Clear the list before generating new suggestions
        lstword.append(str(TransliteratorLogic.convertText(key)))
        node = self.root
        for a in key:
            if not node.children.get(a):
                return 0
            node = node.children[a]
        if not node.children:
            return -1
        if para == 1:
            self.suggestionsRecsuffix(node, key)
            return 1
        else:
            self.suggestionsRec(node, key)
            return 1

    def testmodel(self):
        foundflag = 0
        totalflag = 0
        eval_data = list()
        f = open("Tanglish.txt", mode='r', encoding='utf-8')
        for i in f:
            eval_data.append(i)
        a = list()  # actual_list
        p = list()  # predicted_list
        for i in range(0, len(eval_data), 2):
            engnewlist = eval_data[i].strip('\n').split(" ")
            tamnewlist = eval_data[i + 1].strip('\n').split(" ")
            for j in range(len(engnewlist)):
                totalflag += 1
                try:
                    t.printAutoSuggestions(engnewlist[j], 2)
                    if tamnewlist[j] in lstword and TransliteratorLogic.convertText(tamnewlist[j]):
                        foundflag += 1
                except:
                    continue
        print("No of total words : ", totalflag)
        print("No of correct suggestions : ", foundflag)
        acc = foundflag / totalflag
        print("Accuracy :", acc)


# Code for creating trie
textFile = open("Tami.txt", mode='r', encoding='utf-8')
eData = []
tData = []

for i in textFile:
    txt = i.split("/")
    eData.append(txt[0])
    if len(txt) > 1:
        tData.append(txt[1].strip('\n'))
    else:
        tData.append('')

keys = eData
t = Trie()
t.formTrie(keys)
t.testmodel()

lstword = []

# while True:
#     txt = input("enter the word for suggestion = ")
#     if len(txt) >= 4:
#         t.printAutoSuggestions(txt, 1)
#         print(lstword)
#
#     else:
#         t.printAutoSuggestions(txt, 2)
#         print(lstword)