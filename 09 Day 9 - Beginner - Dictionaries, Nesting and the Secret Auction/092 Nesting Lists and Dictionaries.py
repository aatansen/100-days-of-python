# Nesting
capitals = {
    'France': 'Paris',
    'Spain': 'Madrid',
    'United Kingdom': 'London',
    'India': 'New Delhi'
}

# Nesting a list in a Dictionary
travel_log = {
    'France': ['Paris', 'London'],
    'Spain': ['Madrid', 'Barcelona'],
}
# print(travel_log['France'][0])

# Nesting a dictionary in a dictionary
travel_log = {
    'France': {
        'cities_visited': ['Paris', 'London'], 'Total_visits': 12
    },
    'Spain': {
        'cities_visited': ['Madrid', 'Barcelona'], 'Total_visits': 10
    },
}

print(travel_log['France']['cities_visited'][0])
print(travel_log['France']['Total_visits'])
print(travel_log['Spain']['cities_visited'][0])
print(travel_log['Spain']['Total_visits'])

# Nesting Dictionarys in a List
travel_log = [
    {'country': "France",
     "cities_visited": ["Paris", "London"],
     'total_visits':12
     },
    {'country': "Spain",
     "cities_visited": ["Madrid", "Barcelona"],
     'total_visits':3
     },
]
print(travel_log)