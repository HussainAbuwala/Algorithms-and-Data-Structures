import argparse

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

global_END = 0



class suffixNode:

    '''

    description:        - new suffix node is created
    param: suffixNo     - suffix id of the node
    param: par          - parent of the node
    param: sLink        - suffix link of the node
    param: iE           - incoming edge into the node
    return:             - node

    '''
    def __init__(self, suffixNo=None,par=None,sLink=None,iE=None):
        self.children = [None] * 256
        self.suffix_id = suffixNo
        self.parent = par
        self.suffix_link = sLink
        self.incoming_edge = iE


class suffixEdge:

    '''

    description:      - new suffix edge is created
    param: sIndex     - start index of the edge in the string
    param: eIndex     - end index of the edge in the string
    param: rNode      - node which have this edge as its incoming edge
    return:           - edge

    '''
    def __init__(self, sIndex, eIndex, rNode):
        self.start_index = sIndex
        self.end_index = eIndex
        self.receiving_Node = rNode

    '''

    description:      - this function is automatically called by python whenever an attribute value needs to be accessed. This especially useful to exploit the 
                      - property that at each phase, all leaf edges will be extended by one character which will be str[phase_i_plus_one]. So there is no need to
                      - traverse down to the leaf. Only the end index needs to point to phase_i_plus_one. So whenever the end index of the leaf node is accessed, the global_END
                      - value is returned which points to phase_i_plus_one.
                      
    param: name       - the name of the attribute whose value needs to be accessed
    return (a):       - global_END is returned if end_index of a leaf edge is accessed
    return (b):       - else whatever is the attribute value, that is returned.

    '''
    def __getattribute__(self, name):

        if name == 'end_index':
            if(self.receiving_Node.suffix_id != None):
                return global_END

        return object.__getattribute__(self, name)



class suffixTree:
    def __init__(self, string):

        self.root = suffixNode()
        self.string = string.strip()
        self.build_tree()

    def build_tree(self):

        global global_END
        last_j = - 1

        for phases_i_plus_one in range(0, len(self.string)):

            j_plus_one_extension_start_node = self.root
            j_plus_one_extension_start_index = last_j + 1
            last_intermediate_node_created = None

            global_END = phases_i_plus_one
            jth_suffix_extension = last_j + 1

            while (jth_suffix_extension <= phases_i_plus_one):

                phase_i = phases_i_plus_one - 1

                # n_o_e_t_t - number of elements left still to travel for the path str[j..i] in the phase i+1

                node, edge, n_o_e_t_t = self.traverse(j_plus_one_extension_start_node,
                                                      phase_i - j_plus_one_extension_start_index + 1,
                                                      j_plus_one_extension_start_index,
                                                      j_plus_one_extension_start_node.incoming_edge)

                j_plus_one_extension_start_node, j_plus_one_extension_start_index = self.get_next_starting_node_and_index_for_j_plus_one_extension(
                                                                                                                                                    node,
                                                                                                                                                    edge,
                                                                                                                                                    n_o_e_t_t,
                                                                                                                                                    jth_suffix_extension,
                                                                                                                                                    phase_i)

                # we have reached our destination // CASE - 1 OR CASE - 3 POSSIBLE - FROM ABOVE
                if (n_o_e_t_t == 0):

                    current_node = node

                    # CASE - 1
                    # connect previous intermediate node to the intermediate node that already exists (SUFFIX LINK CREATED)
                    if (last_intermediate_node_created != None):
                        last_intermediate_node_created.suffix_link = current_node
                        last_intermediate_node_created = None

                    # 1 (a). - If str[i + 1] is a child of 'X': APPLY RULE - 3
                    if (current_node.children[ord(self.string[phases_i_plus_one])] != None):
                        last_j = jth_suffix_extension - 1
                        break

                    # 1 (b). - Else:  APPLY RULE - 2
                    else:
                        self.attach_leaf(current_node, phases_i_plus_one, phases_i_plus_one, jth_suffix_extension)



                # we will end in between an edge
                # CASE - 2 - FROM ABOVE
                else:
                    current_node = node
                    current_node_outgoing_edge = edge

                    # character x on the edge with which str[i+1] is compared
                    character, character_index = self.get_character_at_distance_from_edge(current_node_outgoing_edge,
                                                                                          n_o_e_t_t)

                    # 2(a). - if str[i + 1] == str[edge.start_index + d]: APPLY RULE - 3
                    if (self.string[phases_i_plus_one] == character):
                        last_j = jth_suffix_extension - 1
                        break

                    # 2(b). - Else:  APPLY RULE - 2
                    else:
                        self.split_edge(current_node,current_node_outgoing_edge, character_index, phases_i_plus_one,
                                        phases_i_plus_one, jth_suffix_extension)

                        #connect previous intermediate node to the newly created intermediate node (SUFFIX LINK CREATED)
                        if(last_intermediate_node_created != None):
                            last_intermediate_node_created.suffix_link = current_node_outgoing_edge.receiving_Node

                        #make newly created intermediate node ready to get its suffix link in the next extension
                        last_intermediate_node_created = current_node_outgoing_edge.receiving_Node


                jth_suffix_extension += 1

            if (jth_suffix_extension > phases_i_plus_one):
                last_j = phases_i_plus_one


    '''
    
    description:            - splits the edge from the mismatch point and a new intermediate is created at the mismatch point with a leaf hanging from the new intermediate node 
    param: current_node     - node from which the edge is coming out
    param: edge             - outgoing edge from the current_node
    param: chracter_index   - index of the mismatch character on the edge
    param: l_e_s            - start index of the leaf edge
    param: l_e_e            - end index of the leaf edge
    param: l_s_id           - suffix id of the leaf node
    return:                 - None
    time_complexity:        - O(1) in best case and worst case
    
    '''
    def split_edge(self,current_node,edge, character_index, l_e_s, l_e_e, l_s_id):

        save_end = edge.end_index
        edge.end_index = character_index - 1
        new_intermediate_node = suffixNode(None,current_node,self.root,edge)   #parent set and suffix link to root
        self.attach_leaf(new_intermediate_node, l_e_s, l_e_e, l_s_id)
        new_edge = suffixEdge(character_index, save_end, edge.receiving_Node)
        new_intermediate_node.children[ord(self.string[character_index])] = new_edge

        edge.receiving_Node.parent = new_intermediate_node      #set the parent of old receving node to the new intermediate node before it gets replaced
        edge.receiving_Node.incoming_edge = new_edge
        edge.receiving_Node = new_intermediate_node

    '''

    description:                    - attaches a leaf node and a leaf edge to an intermediate node or a root node
    param: current_node             - node from which leaf edge will come out
    param: leaf_edge_start_index    - outgoing edge from the current_node
    param: leaf_edge_end_index      - index of the mismatch character on the edge
    param: leaf_suffix_id           - start index of the leaf edge
    return:                         - None
    time_complexity:                - O(1) in best case and worst case

    '''

    def attach_leaf(self, current_node, leaf_edge_start_index, leaf_edge_end_index, leaf_suffix_id):
        leaf_node = suffixNode(leaf_suffix_id,current_node)     #parent set
        leaf_edge = suffixEdge(leaf_edge_start_index, leaf_edge_end_index, leaf_node)
        leaf_node.incoming_edge = leaf_edge
        current_node.children[ord(self.string[leaf_edge_start_index])] = leaf_edge

    '''

    description:                        - traversal is performed from the given start_index in the string using the SKIP COUNT TRICK
    param: current_node                 - node from which the traversal starts
    param: n_o_e_t_t                    - number of elements left to travel
    param: start_index                  - index in the string from which the traversal starts
    param: current_node_incoming_edge   - incoming edge of the current_node
    return (a):                         - if the traversal will end between an edge, then (current_node, current_node_outgoing_edge, n_o_e_t_t) is returned
    return (b):                         - if the traversal will end at an node, then (current_node, current_node_incoming_edge, n_o_e_t_t) is returned

    '''

    def traverse(self, current_node, n_o_e_t_t, start_index, current_node_incoming_edge=None):

        # we need to travel furthur down the tree from the current node
        if (n_o_e_t_t > 0):

            current_node_outgoing_edge = current_node.children[ord(self.string[start_index])]
            edge_length = self.get_edge_length(current_node_outgoing_edge)
            if (n_o_e_t_t >= edge_length):
                return self.traverse(current_node_outgoing_edge.receiving_Node,
                                     n_o_e_t_t - edge_length,
                                     start_index + edge_length,
                                     current_node_outgoing_edge)

            # we will end in between an edge // CASE - 2 - FROM ABOVE
            else:
                return (current_node, current_node_outgoing_edge, n_o_e_t_t)

        # we have reached our destination // CASE - 1 OR CASE - 3 POSSIBLE - FROM ABOVE
        else:
            return (current_node, current_node_incoming_edge, n_o_e_t_t)

    '''

    description:        - checks if a node is a leaf or not
    param: Node         - node to check whether it is a leaf or not
    return (a):         - TRUE is returned if the node is a leaf.
    return (b):         - FALSE is returned if the node is not a leaf.

    '''
    def is_leaf(self, Node):

        if (Node.suffix_id != None):
            return True
        return False

    '''

    description:        - gets the character at some point in the edge
    param: edge         - edge from which the character is needed
    return:             - (character, character_index) is returned.


    '''
    def get_character_at_distance_from_edge(self, edge, distance):

        character_index = edge.start_index + distance
        character = self.string[character_index]
        return (character, character_index)

    '''

    description:        - gets the length of the edge
    param: edge         - edge of which the length is needed
    return:             - length of the edge

    '''

    def get_edge_length(self, edge):

        return edge.end_index - edge.start_index + 1

    '''

    description:        - checks if a node is a root or not
    param: node         - node to check whether it is a root or not
    return (a):         - TRUE is returned if the node is a root.
    return (b):         - FALSE is returned if the node is not a root.

    '''
    def is_root(self,node):

        if(node.parent == None):
            return True
        return False

    '''

    description:            - used to find out what will be the next starting node and the next starting index in the string from which the traversal for the j_plus_one extensionw will start
    param: node             - node to check whether it is a leaf or not
    param: edge             - could be the incoming edge of the node or the outgoing edge depending on one of the cases mentioned at the start
    param: n_o_e_t_t        - number of elements left to travel
    param: jth_extension    - current extension going on
    param: phase_i          - previous phase (i) of the current phase (i + 1)
    return:                 - (new_starting_node,new_start_index) for the j_plus_one extension

    '''

    def get_next_starting_node_and_index_for_j_plus_one_extension(self,node,edge,n_o_e_t_t,jth_extension,phase_i):

        # CASE -1 OR CASE -3 [str[j..i] ending at some node X]
        # X can be
        #   a)leaf node         (CASE - 3)
        #   b)root node         (CASE - 1)
        #   c)intermediate node (CASE - 1)

        if(n_o_e_t_t == 0):

            #CASE - 3
            if(self.is_leaf(node)):

                #walk up one edge from leaf
                parent = node.parent

                #walk up leads to root
                if(self.is_root(parent)):
                    return (parent,jth_extension + 1)

                #walk up leads to an intermediate node
                else:
                    total_elems_j_to_i = phase_i - jth_extension + 1
                    total_elms_k_to_i = self.get_edge_length(edge)
                    new_start_index = jth_extension + (total_elems_j_to_i - total_elms_k_to_i)

                    new_starting_node = parent.suffix_link

                    if(self.is_root(new_starting_node)):
                        return (new_starting_node, jth_extension + 1)

                    return (new_starting_node,new_start_index)

            #CASE - 1
            else:

                #current intermediate node is the root
                if (self.is_root(node)):
                    return (node, jth_extension + 1)

                #current intermediate node is not the root. Suffix link can be taken
                else:
                    new_starting_node = node.suffix_link
                    if (self.is_root(new_starting_node)):
                        return (new_starting_node, jth_extension + 1)
                    return (new_starting_node,phase_i + 1)

        # CASE - 2 [str[j..i] ending in between some edge Y]
        # Need to walk up from edge Y to some Node X
        # X can be
        #   a)root node         (CASE - 2)
        #   c)intermediate node (CASE - 2)
        else:

            parent = node                           #node is the one with the outgoing edge

            #parent is the root
            if (self.is_root(parent)):
                return (parent, jth_extension + 1)

            #parent is an intermediate node. We can take the suffix link
            else:
                total_elems_j_to_i = phase_i - jth_extension + 1
                total_elems_k_to_i = n_o_e_t_t
                new_start_index = jth_extension + (total_elems_j_to_i - total_elems_k_to_i)
                new_starting_node = parent.suffix_link

                if (self.is_root(new_starting_node)):
                    return (new_starting_node, jth_extension + 1)

                return (new_starting_node,new_start_index)





'''

description:        - an depth first traversal is performed to find all the leaves and the suffix indexes are added to the suffix array
param: trav         - traversal node from which the traversal will start. trav will initially be the root node
param: suffixArray  - array which will hold sorted suffix id's
return:             - None

'''
def dfs(trav, suffixArray):
    if (trav.suffix_id == None):
        for i in range(256):
            edge = trav.children[i]
            if (edge != None):
                dfs(edge.receiving_Node, suffixArray)

    else:

        suffixArray.append(trav.suffix_id)

'''

description:        - bwt of the string is computed is the suffixArray
param: suffixArray  - suffixArray
param: string       - string of which the bwt is to be computed
return:             - length of the edge

'''
def computeBWT(suffixArray, string):
    bwt_string = ''

    for item in suffixArray:
        if (item - 1 < 0):
            bwt_string = bwt_string + '$'
        else:
            bwt_string = bwt_string + string[item - 1]

    return bwt_string


def run_alternate():

    textFile = input("Please enter File Name: ")

    text_file = open(textFile, 'r')
    text = ""
    text += text_file.read().strip()
    text+="$"

    myTree = suffixTree(text)

    sArray = []
    dfs(myTree.root, sArray)

    out = computeBWT(sArray, text)
    file = open('output_bwt.txt', 'w')

    file.write(out)


if __name__ == '__main__':
    run_alternate()
    #main()
    #string = "An_algorithm_such_as_this_must_be_beheld_to_be_believed--Donald_Ervin_Knuth$"
    #string = "abbabc$"
    #string  = "ACCCTGAACCCTAAACCCTGAACCCTGAACCCTAAACCTAAACCCTGAAACCCTAAACCCTGAACCCTAAACCTAAACCCTGAACCCTAAACCCTGAACCCTGAAC$"
    #string = "suffix_trees_and_bwt_are_related$"
    #myTree = suffixTree(string)

    #sArray = []
    #dfs(myTree.root, sArray)

    #print(computeBWT(sArray, string) == "hd-$-__dnnhtoeesmsdn______uellbbvbhbiltcettlvhraeaeh_iAoKtDgoEiau_su_i_smner")


