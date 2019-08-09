#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    # first step
    # place each source as key
    # place each destination as value
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        if ticket.source == None: 
            route[0] = ticket.destination
        elif ticket.destination == None:
            route[length-1] = ticket.source 

    # second step
    # retrieve each source ticket to return a destination, and use that
    # destination to find the next source
    currentlDestination = route[0]
    
    i = 1 
    while currentDestination != None 
        nextDestination = hash_table_retrieve(hashtable, currentDestination)
        route[i] = nextDestination
        # third step place each source and destination onto the routes
        currentlDestination = nextDestination
        i += 1 

    # return 

    return route
