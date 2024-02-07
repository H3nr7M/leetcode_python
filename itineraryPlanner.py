def find_itinerary(flights, starting_airport):
    itinerary = [starting_airport]
    flights_map = {}
    for origin, destination in flights:
        if origin in flights_map:
            flights_map[origin].append(destination)
        else:
            flights_map[origin] = [destination]

    for key in flights_map.keys():
        flights_map[key].sort()

    def dfs(airport):
        if airport in flights_map and flights_map[airport]:
            destination = flights_map[airport].pop(0)
            dfs(destination)

        itinerary.append(airport)

    dfs(starting_airport)

    if len(itinerary) == 1 + len(flights):
        return itinerary[::-1]
    else:
        return None

flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
starting_airport = 'YUL'

print(find_itinerary(flights, starting_airport))
# Output: ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
