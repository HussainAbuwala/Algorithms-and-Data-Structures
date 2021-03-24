from TrieNode import TrieNode
class MyTrie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self,key):

        trav = self.root

        for item in key:
            if trav.array[ord(item)] == None:
                newTrieNode = TrieNode()
                trav.array[ord(item)] = newTrieNode
                trav = newTrieNode
            else:
                trav = trav.array[ord(item)]

        trav.string = key

    def search(self,key):

        trav = self.root

        for item in key:
            if trav.array[ord(item)] == None:
                return False
            else:
                trav = trav.array[ord(item)]

        if trav.string == key:
            return True
        return False

    def printAllWords(self):

        trav = self.root
        self.aux_printAllWords(trav)



    def aux_printAllWords(self,trav):


        if trav.string!= '':
            print(trav.string)

        for i in range(len(trav.array)):
            if trav.array[i] == None:
                continue
            else:
                x = trav.array[i]
                self.aux_printAllWords(x)

    def delete_word(self,key):

        trav = self.root
        self._aux_delete_word(trav,key,0)


    def _aux_delete_word(self,trav,key,index):

            if index == len(key):
                trav.string = ''
                return self.check_if_any_descendant(trav)

            else:
                x = trav.array[ord(key[index])]
                check = self._aux_delete_word(x,key,index + 1)
                if check == False:
                    trav.array[ord(key[index])] = None

                return self.check_if_any_descendant(trav)

    def check_if_any_descendant(self,trav):

        check = False
        for i in range(len(trav.array)):
            if trav.array[i] != None:
                check = True
                break

        return check








'''trie = MyTrie()
trie.insert('dad')
trie.insert('dads')
trie.insert('dadss')
trie.printAllWords()
trie.delete_word('dad')
trie.printAllWords()
trie.delete_word('dads')
trie.printAllWords()
print(trie.search('dad'))
print(trie.search('dads'))
print(trie.search('dadss'))
trie.printAllWords()'''
