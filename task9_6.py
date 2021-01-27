import math
import sys

planet_data = {"orbital_radius":{"Mercury": 58, "Venus": 108, "Earth": 150, "Mars": 228, "Jupiter": 778, "Saturn": 1429, "Uranus": 2871, "Neptune": 4504},
"orbital_speed": {"Mercury": 47.87, "Venus": 35.02, "Earth": 29.78, "Mars": 24.13, "Jupiter": 13.07, "Saturn": 9.69, "Uranus": 6.81, "Neptune": 5.43}}

planet1 = input("Planet 1: ")
planet_year_res=[]

def daysIn_year(planet):
    orbital_radius_1 = planet_data['orbital_radius'][planet] * 1000000
    orbital_speed_1 = planet_data['orbital_speed'][planet]

    planet_year1 = 2 * math.pi * orbital_radius_1 / orbital_speed_1
    planet_year1 = planet_year1 / (60 * 60 * 24)  # converting seconds to days
    planet_year_res.append(planet_year1)

def planetYear_is_bigger():
    bigger_year = planet1 if planet_year_res[0] > planet_year_res[1] else planet2  # Looking which year is bigger
    print("The {} year is bigger".format(bigger_year))

daysIn_year(planet1)

planet2 = input("Planet 2: ")

daysIn_year(planet2)

print("The year is {} days on {}".format(int(planet_year_res[0]), planet1))
print("The year is {} days on {}".format(int(planet_year_res[1]), planet2))

planetYear_is_bigger()
