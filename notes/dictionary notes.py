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

print(nested_dictionary["GA"]["POPULATION"])
print(nested_dictionary["FL"]["NAME"])

print(nested_dictionary["GA"]
print("GA")

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "CITIES": [
            "Fresno",
            "Los Angeles",
            "San Fransisco"
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
            "Juneau"
        ],

    },
    "GA": {
        "NAME": "Georgia",
        "CITIES": [
            "Atlanta",
            "Savannah",
            "Augusta"
        ]
    }
}

print(complex_dictionary["AK"]["CITIES"][0])
