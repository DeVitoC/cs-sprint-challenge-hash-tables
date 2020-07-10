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
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    first = cache['NONE']
    route = [first]
    current_ticket = first
    for i in range(length - 1):
        route.append(cache[current_ticket])
        current_ticket = cache[current_ticket]
    return route