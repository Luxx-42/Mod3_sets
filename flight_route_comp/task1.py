# Task 1 Flight route comaprison
def compare_flight_routes(our_routes, competitor_routes, all_airline_destinations):
    '''Comparing flight routes between two airlines using sets and set methods'''
    
    shared_destinations = our_routes.intersection(competitor_routes)
    print(f"\nDestinations both airlines are flying to:", shared_destinations)

    unique_to_us = our_routes.difference(competitor_routes)
    print(f"\nDestinations that are only ours:", unique_to_us)

    all_destinations = our_routes.union(competitor_routes)
    print(f"\nHere are the destinations combined between us and our competitors:", all_destinations)

    destinations_neither_fly = all_airline_destinations - all_destinations
    print(f"\nHere are destinations neither airlines fly to:", destinations_neither_fly)

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

all_airline_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK", "NRT", "SIN"}

compare_flight_routes(our_routes, competitor_routes, all_airline_destinations)



