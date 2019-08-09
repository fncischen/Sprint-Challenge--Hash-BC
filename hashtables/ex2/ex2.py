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
        if ticket.source == "NONE": 
            route[0] = ticket.destination
        elif ticket.destination == "NONE":
            route[length-1] = ticket.source 

    # second step
    # retrieve each source ticket to return a destination, and use that
    # destination to find the next source
    
    currentDestination = route[0]
    
    i = 1 
    while currentDestination != "NONE":
        nextDestination = hash_table_retrieve(hashtable, currentDestination)
        if nextDestination == "NONE":
            break
        else:
            route[i] = nextDestination
        # third step place each source and destination onto the routes
        currentDestination = nextDestination
        i += 1 

    # return 

    return route

tickets = [
    Ticket("PIT","ORD" ),
    Ticket("XNA","CID" ),
    Ticket("SFO", "BHM" ),
    Ticket("FLG", "XNA" ),
    Ticket("NONE", "LAX" ),
    Ticket("LAX", "SFO" ),
    Ticket("CID", "SLC" ),
    Ticket( "ORD",  "NONE" ),
    Ticket("SLC", "PIT" ),
    Ticket("BHM","FLG" )
  ]

print(reconstruct_trip(tickets,9))