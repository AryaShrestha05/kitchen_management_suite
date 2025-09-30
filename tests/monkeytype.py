"""
File: monkeytype.py
File-Path: test/monkeytype.py
Author: Rohan Plante
Date-Created: 09-30-2025

Description:
    Dummy data generator

Inputs:
    - Number of users to generate
    - Number of households to generate

Outputs:
    - JSON files containing dummy data for database
"""

'''
Database Struct
Entities:
    Users:
        UserID (int)
        UserName (string)
        Email (string)
        DOB (date MM/DD/YYY)
        Password (String)
    Household:
        HouseholdID (int)
        HouseholdName (String)
        Members (String/list)
    Pantry:
        PantryName (String)
        PantryID (int)
    Items:
        ItemID (int)
        Quantity (int)
        Owner (string)
        ItemName (string)
        InDate (date MM/DD/YYY)
    Recipe:
        RecipeID (int)
        RecipeBody (text)
        RecipeName (string)
    
    Many User Member of Many Household
    One Household Owns Many Pantry
    One Pantry Contains Many Items
    Many Household Holds Many Recipes
    Many User Holds Many Recipes
'''

"""
TODO:
    - Generate data for Recipes and Items
    - Figure out how to generate relationship data between entities
"""

from faker import Faker
import json
import argparse

fake = Faker()
users = []
user_struct = {
    "UserID": 0,
    "UserName": "",
    "Email": "",
    "DOB": "",
    "Password": ""
}

households = []
household_struct = {
    "HouseholdID" : 0,
    "HouseholdName" : "",
    "Members" : []
}

# used for cmd arguments
parser = argparse.ArgumentParser(description="Generate dummy data for database")
parser.add_argument("--users", type=int, help="Number of users to generate")
parser.add_argument("--households", type=int, help="Number of households to generate")
args = parser.parse_args()

num_users = args.users
num_households = args.households

# if no arguments given prompt fo input:
if not num_users:
    num_users = int(input("Enter number of users to generate: "))
if not num_households:
    num_households = int(input("Enter number of households to generate: "))

def gen_email(name: str, birth: str = None) -> str:
    # generates semi realistic email
    name = name.lower()
    parts = name.split()
    first = parts[0]
    last = parts[-1] if len(parts) > 1 else parts[0]

    chunk1_choices = [
        first[0],  # first initial
        first,     # first name
        first[0],  # first initial
        last,      # last name
        last[0]    # last initial
    ]
    chunk1 = fake.random_element(chunk1_choices)

    chunk2 = fake.random_element(["", ".", "_", "-"])

    # If chunk1 used last-name information, avoid last-name pieces in chunk3
    last_related = {last, last[0]}
    first_related = {first, first[0]}
    if chunk1 in last_related:
        chunk3_choices = [first, first[0]]
    elif chunk1 in first_related:
        chunk3_choices = [last, last[0]]
    else:
        chunk3_choices = [last, first, last[0], first[0]]
    
    chunk3 = fake.random_element(chunk3_choices)

    rand_num = str(fake.random_int(0, 99)).zfill(fake.random_int(1, 4))
    if birth:
        bparts = birth.split("-")
        year = bparts[0] if len(bparts) > 0 else ""
        month = bparts[1] if len(bparts) > 1 else ""
        year_short = year[2:] if len(year) >= 4 else year
        chunk4_choices = ["", year, month, year_short, rand_num]
    else:
        chunk4_choices = ["", rand_num]

    chunk4 = fake.random_element(chunk4_choices)

    email = f"{chunk1}{chunk2}{chunk3}{chunk4}@{fake.free_email_domain()}"

    return email

# create users
def generate_users(num) -> str:
    # generates users
    for _ in range(num):
        user = user_struct.copy()
        user["UserID"] = _
        user["UserName"] = fake.first_name() + " " + fake.last_name()
        user["DOB"] = fake.date_of_birth().isoformat()
        user["Email"] = gen_email(user["UserName"], user["DOB"])
        user["Password"] = fake.password(length = fake.random_int(8, 16))
        users.append(user)
        print(f"Generated user {_+1}/{num}")
    with open("json/dummy_users.json", "w") as f:
        json.dump(users, f, indent=4)

def generate_households(num_house) -> str:
    # generates households
    num_households = num_house
    total_users = len(users)
    print(f"Generating {num_households} households for {total_users} users")

    # reset existing households
    households.clear()

    # create an empty households
    for hid in range(num_households):
        print(f"  Initializing household {hid+1}/{num_households}")
        house = {"HouseholdID": hid, "HouseholdName": "", "Members": []}
        households.append(house)

    # every user should be assigned to at least once to a random household
    for user in users:
        hid = fake.random_int(0, num_households - 1)
        if user["UserID"] not in households[hid]["Members"]:
            households[hid]["Members"].append(user["UserID"])

    # every household should have at least one member
    for hid, house in enumerate(households):
        if not house["Members"]:
            print(f"  Household {hid+1} is empty: assigning one random user")
            candidate = fake.random_element(users)
            house["Members"].append(candidate["UserID"])

    # Set household names using the first member as admin
    for house in households:
        if house["Members"]:
            admin_id = house["Members"][0]
            admin = next((u for u in users if u["UserID"] == admin_id), None)
            house["HouseholdName"] = (admin["UserName"] + " Household") if admin else f"Household {house['HouseholdID']}"
        else:
            # if no members, household name will default to "Household {id}"
            house["HouseholdName"] = f"Household {house['HouseholdID']}"

    with open("json/dummy_households.json", "w") as f:
        json.dump(households, f, indent=4)

def generate(num_users, num_households) -> str:
    # main generator function
    generate_users(num_users)
    generate_households(num_households)

# run the generator
# usage: python monkeytype.py --users <int> --households <int>
generate(num_users, num_households)