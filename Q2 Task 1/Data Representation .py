
# User input for total number of places user wants to visit

total_places = int(input('How many places do you want to visit?: '))

# Empty array list  for input values provided by user

list_of_places = []

# Set of places user wants to visit

places = ["Khomasdal", "Zoo Park", "Namibia Craft Centre", "National Museum", "Heroes Acre", "Christuskirche"]

# List of  distances between the places mentioned above
distances = [
    [0, 5.7, 5.3, 5.5, 15.4, 6.4],
    [5.8, 0, 0.8, 0.5, 11, 0.45],
    [5.3, 0.8, 0, 1.5, 10.5, 0.95],
    [5.5, 0.5, 1.6, 0, 12.9, 0.55],
    [15.4, 12.5, 10.6, 12.8, 0, 12.5],
    [6.4, 0.45, 0.95, 0.5, 12.5, 0]
]


# Function to calculate total distance of a suggested route based on places provided by user
def total_distance(list_of_places, places, distances):
    total_distance = 0
    # Loop to iterate through array list of places provided by user
    for i in range(len(list_of_places) - 1):
        current_location = places.index(list_of_places[i])
        next_location = places.index(list_of_places[i + 1])
        # Retrieves distance from distance list inorder to calculate total distance
        distance = distances[current_location][next_location]
        total_distance += distance
    return total_distance


# Prompts user to provide places to visit

for i in range(total_places):
    place = input(f"Please provide place #{i + 1} :")
    list_of_places.append(place)

total_distance = total_distance(list_of_places, places, distances)
print("The Total distance for given route for all places is ", total_distance, "km")
