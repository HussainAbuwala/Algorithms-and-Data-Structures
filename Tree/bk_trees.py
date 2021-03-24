from edit_distance_dp import minimumEditDistance

class BK_node:
    def __init__(self,key):
        self.array = [None] * 26
        self.word = key


class BK_trees:

    def __init__(self,tolerance = 1):
        self.root = None
        self.count = 0
        self.tolerance = tolerance

    def __len__(self):
        return self.count

    def insertWord(self,word):

        if self.root == None:
            self.root = BK_node(word)
            return

        trav = self.root
        while True:
            edit_distance = minimumEditDistance(trav.word,word)
            if trav.array[edit_distance] == None:
                new_Node = BK_node(word)
                trav.array[edit_distance] = (edit_distance,new_Node)
                self.count+=1
                return
            else:
                trav = trav.array[edit_distance][1]

    def predict_correct_words(self,mispelled):

        trav = self.root

        self._aux_predict_words(trav,mispelled)

    def _aux_predict_words(self,trav,mispl):

        edit_distance = minimumEditDistance(trav.word,mispl)
        if edit_distance <= self.tolerance:
            print(trav.word)
        min = edit_distance - self.tolerance
        max = edit_distance + self.tolerance

        if min <= 0:
            min = 1

        for i in range(min,max + 1):
            if trav.array[i] != None:
                self._aux_predict_words(trav.array[i][1],mispl)

def parseWords():

    f = open('english_words','r')

    words = f.readlines()

    for i,item in enumerate(words):
        words[i] = item.strip('\n')

    return words

def main():

    words = parseWords()
    bk_tree = build_bk(words)


    while True:
        bk_tree.predict_correct_words(input(':'))
        print()

def build_bk(words):

    bk_tree = BK_trees()

    for item in words:
        bk_tree.insertWord(item)

    return bk_tree

if __name__ == '__main__':
    '''bk = BK_trees()
    bk.insertWord('book')
    bk.insertWord('books')
    bk.insertWord('cake')
    bk.insertWord('boo')
    bk.insertWord('cape')
    bk.insertWord('boon')
    bk.insertWord('cook')
    bk.insertWord('cart')
    
    bk.predict_correct_words('cooo')'''
    main()











