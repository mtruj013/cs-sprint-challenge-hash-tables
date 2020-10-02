#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = []

    # first_flight = []

    # loop over tickets
    for ticket in tickets:
        # put key, value in cache
        cache[ticket.source] = ticket.destination
    
    # first flight
    route.append(cache['NONE'])

    for idx in range(length):
        # check if route at idx is in cache
        if route[idx] in cache:
            # if it's the first one, continue
            if cache[route[idx]] == route[0]:
                continue
            # if not, add it to the route
            else:
                route.append(cache[route[idx]])


    return route
   


    # return output


    
    
    # return route




ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                   ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

if __name__ == "__main__":
    print(reconstruct_trip(tickets, 10))