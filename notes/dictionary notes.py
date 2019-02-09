states = {
    "CA": "California",
    "FL": "Florida",
    "AK": "Arkansas",
    "GA": "Georgia"
}

print(states["CA"])
print(states["AK"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "Population": 39500000
    },
    "FL": {
        "NAME": "Florida",
        "Population": 1300002
    },
    "AK": {
        "NAME": "Alaska",
        "Population": 737000
    },
    "GA": {
        "NAME": "Georgia",
        "Population": 10500000
    }
}

print(nested_dictionary["GA"], ["POPULATION"])
print(nested_dictionary["FL"], ["NAME"])

print(nested_dictionary["GA"])
# 1

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "CITIES": [
            "Fresno",
            "Los Angeles",
            "San Fransisco",
            ","
        ]
    },
    "FL": {
        "NAME": "Florida",
        "CITIES": [
            "Tampa",
            "Miami",
            "Orlando",
            "Jacksonville"
        ]
    },
    "AK": {
        "NAME": "Alaska",
        "CITIES": [
            "Anchorage",
            "Fair banks",
            "Juneau",
            ","
        ],

    },
    "GA": {
        "NAME": "Georgia",
        "CITIES": [
            "Alabama",
            "Atlanta",
            "Savannah",
            "Augusta",
        ]
    }
}

print(complex_dictionary["AK"]["CITIES"][0])

# Open your notes, and get it to print Florida
# And then get it to print alabama cause superbowl

print(["FL"], ["NAME"])
print(["GA"], ["CITIES"], [0])

print(complex_dictionary.keys())
print(complex_dictionary.items())
print(nested_dictionary.items())

for key, value in complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)

# This is what makes it look pretty
print()
for state, info in complex_dictionary.items():
    for label, stats in info.items():
        print(label)
        print(stats)
        print("-" * 20)
    print("-" * 20)

# Other notes
states["AR"] = "Arizona?"  # It isn't arizona

states['AR'] = "Arkansas"  # Fixed it
print([states['AR']])
