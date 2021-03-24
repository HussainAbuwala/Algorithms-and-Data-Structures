def edit_distance_recursive(string1,string2):

    return _aux_edit_distance(string1,string2,0,0,0)

def _aux_edit_distance(string1,string2,i,j,count):

    if i == len(string1) and j == len(string2):
        return count
    elif i >= len(string1) and j < len(string2):
        return count + len(string2[j:])
    elif i < len(string1) and j >= len(string2):
        return count + len(string1[i:])
    else:

        if string1[i] == string2[j]:
            return _aux_edit_distance(string1, string2, i+1, j+1, count)
        else:
            return min(_aux_edit_distance(string1,string2,i+1,j+1,count + 1),
                       _aux_edit_distance(string1,string2,i,j+1,count + 1),
                       _aux_edit_distance(string1,string2,i+1,j,count + 1))

def minimumEditDistance(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]


if __name__ == '__main__':

    print(minimumEditDistance('missin','missing'))