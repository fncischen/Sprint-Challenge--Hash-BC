#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    i = 0
    for weight in weights:
        hash_table_insert(ht, weight,i)
        i += 1 

    # i.e. {4: 0}, {6: 1}, {10: 2}, {15: 3}, {16: 4}
    # first step:
    # loop through each weight in weights

    for first_weight in weights:

        # second step
        # subtract 21 from that key
        first_index = hash_table_retrieve(ht, first_weight)
        second_weight = limit - first_weight

        print(first_index,second_weight)
        # third step
        # search for that second value on the hash table

        if hash_table_retrieve(ht, second_weight) != None:
            second_index = hash_table_retrieve(ht, second_weight)
            
            merged_packages = [first_index, second_index]
            merged_packages.sort(reverse=True)
            return merged_packages
    
        # if it doesnt exist, skip to next item in hash table 
    return None


e = [ 4, 4 ]
print(get_indices_of_item_weights(e,2,8))

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
