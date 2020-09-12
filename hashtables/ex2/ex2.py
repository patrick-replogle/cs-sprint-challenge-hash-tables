#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = []
    hashMap = {}

    for ticket in tickets:
        hashMap[ticket.source] = ticket.destination

    route.append(hashMap['NONE'])
    del hashMap['NONE']

    while len(route) < length:
        curr = route[len(route) - 1]
        route.append(hashMap[curr])

    return route


# Test data below
tickets = [
    Ticket("PIT", "ORD"),
    Ticket("XNA", "CID"),
    Ticket("SFO", "BHM"),
    Ticket("FLG", "XNA"),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO"),
    Ticket("CID", "SLC"),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT"),
    Ticket("BHM", "FLG"),
]


print(reconstruct_trip(tickets, 10))
# -> ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD", "NONE"]
