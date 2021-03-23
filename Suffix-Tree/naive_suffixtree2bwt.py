'''
        NAME: HUSSAIN SADIQ ABUWALA
        STUDENT-ID: 27502333

'''
'''

Algortihm divided into three cases

Case - 1: - str[j...i] ends at an internal node or a root node. Lets name the node as 'X'

    1 (a). - If str[i + 1] is a child of 'X'.
              
                    APPLY RULE - 3
    
    1 (b). - Else:  APPLY RULE - 2
             
             - Create a new leaf node with suffix index = 'i + 1'
             - Create a new leaf edge connecting node 'X' and new leaf node where the edge has the following attributes
                
                - edge.start_index = i + 1
                - edge.end_index = i + 1

Case - 2: - str[j...i] ends between an edge 'Y'
    
    2 (a). - if str[i + 1] == str[edge.start_index + d]
                    
                    APPLY RULE - 3
    
    2 (b). - Else:  APPLY RULE - 2
            
            - Create a new internal node
            - Create a new leaf edge
            - Create a new leaf node


Case - 3: - str[j...i] ends at an leaf node 'X'
    
    3 (a). Update leaf edge end index = i + 1

'''

class suffixNode:

    def __init__(self,suffixNo = None):
        self.children = [None] * 256
        self.suffix_id = suffixNo

class suffixEdge:

    def __init__(self,sIndex,eIndex,rNode):

        self.start_index = sIndex
        self.end_index = eIndex
        self.receiving_Node = rNode


class suffixTree:

    def __init__(self,string):
        self.root = suffixNode()
        self.string = string
        self.build_tree()
        #self.test()


    def build_tree(self):

        for phases_i_plus_one in range(0,len(self.string)):

            jth_suffix_extension = 0

            while (jth_suffix_extension <= phases_i_plus_one):

                phase_i = phases_i_plus_one - 1

                #n_o_e_t_t - number of elements left still to travel for the path str[j..i] in the phase i+1

                node,edge,n_o_e_t_t = self.traverse(self.root,phase_i - jth_suffix_extension + 1, jth_suffix_extension)

                # we have reached our destination // CASE - 1 OR CASE - 3 POSSIBLE - FROM ABOVE
                if(n_o_e_t_t == 0):

                    current_node = node
                    current_node_incoming_edge = edge

                    #CASE - 3 - APPLY RULE - 1
                    if(self.is_leaf(current_node)):
                        current_node_incoming_edge.end_index = phases_i_plus_one

                    #CASE - 1
                    else:

                        # 1 (a). - If str[i + 1] is a child of 'X': APPLY RULE - 3
                        if(current_node.children[ord(self.string[phases_i_plus_one])] != None):
                            break

                        #1 (b). - Else:  APPLY RULE - 2
                        else:
                            self.attach_leaf(current_node,phases_i_plus_one,phases_i_plus_one,jth_suffix_extension)

                # we will end in between an edge
                # CASE - 2 - FROM ABOVE
                else:
                    current_node = node
                    current_node_outgoing_edge = edge

                    #character x on the edge with which str[i+1] is compared
                    character, character_index = self.get_character_at_distance_from_edge(current_node_outgoing_edge,n_o_e_t_t)

                    # 2(a). - if str[i + 1] == str[edge.start_index + d]: APPLY RULE - 3
                    if(self.string[phases_i_plus_one] == character):
                        break

                    # 2(b). - Else:  APPLY RULE - 2
                    else:
                        self.split_edge(current_node_outgoing_edge,character_index,phases_i_plus_one,phases_i_plus_one,jth_suffix_extension)



                jth_suffix_extension += 1


    def split_edge(self,edge,character_index,l_e_s,l_e_e,l_s_id):

        save_end = edge.end_index
        edge.end_index = character_index - 1
        new_intermediate_node = suffixNode(None)
        self.attach_leaf(new_intermediate_node,l_e_s,l_e_e,l_s_id)
        new_edge = suffixEdge(character_index,save_end,edge.receiving_Node)
        new_intermediate_node.children[ord(self.string[character_index])] = new_edge
        edge.receiving_Node = new_intermediate_node

    def attach_leaf(self,current_node,leaf_edge_start_index,leaf_edge_end_index,leaf_suffix_id):
        leaf_node = suffixNode(leaf_suffix_id)
        leaf_edge = suffixEdge(leaf_edge_start_index,leaf_edge_end_index,leaf_node)
        current_node.children[ord(self.string[leaf_edge_start_index])] = leaf_edge


    def traverse(self,current_node,n_o_e_t_t,start_index,current_node_incoming_edge=None):

        #we need to travel furthur down the tree from the current node
        if(n_o_e_t_t > 0):

            current_node_outgoing_edge = current_node.children[ord(self.string[start_index])]
            edge_length = self.get_edge_length(current_node_outgoing_edge)
            if(n_o_e_t_t >= edge_length):
                return self.traverse(current_node_outgoing_edge.receiving_Node,
                                     n_o_e_t_t - edge_length,
                                     start_index + edge_length,
                                     current_node_outgoing_edge)

            #we will end in between an edge // CASE - 2 - FROM ABOVE
            else:
                return (current_node,current_node_outgoing_edge,n_o_e_t_t)

        #we have reached our destination // CASE - 1 OR CASE - 3 POSSIBLE - FROM ABOVE
        else:
            return (current_node,current_node_incoming_edge,n_o_e_t_t)

    def is_leaf(self,Node):

        if(Node.suffix_id != None):
            return True
        return False

    def get_character_at_distance_from_edge(self,edge,distance):

        character_index = edge.start_index + distance
        character = self.string[character_index]
        return (character,character_index)

    def get_edge_length(self,edge):

        return edge.end_index - edge.start_index + 1





def dfs(trav,suffixArray):

    if (trav.suffix_id == None):
        for i in range(256):
            edge = trav.children[i]
            if(edge != None):
                dfs(edge.receiving_Node,suffixArray)

    else:

        suffixArray.append(trav.suffix_id)

def computeBWT(suffixArray,string):

    bwt_string = ''

    for item in suffixArray:
        if (item - 1 < 0):
            bwt_string = bwt_string + '$'
        else:
            bwt_string = bwt_string + string[item - 1]

    return bwt_string


def main(textFile):

    text_file = open(textFile, 'r')
    text = ""
    text += text_file.read()
    text+="$"

    myTree = suffixTree(text)

    sArray = []
    dfs(myTree.root, sArray)

    out = computeBWT(sArray, text)
    file = open('output_bwt.txt', 'w')

    file.write(out)



if __name__ == '__main__':
    #string = "An_algorithm_such_as_this_must_be_beheld_to_be_believed--Donald_Ervin_Knuth$"
    #string = "abbabc$"
    main(input("Please enter File Name: "))


