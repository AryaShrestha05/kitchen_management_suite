from faker import Faker
fake = Faker()

print(fake.name())

'''
Database Struct
Entities:
    Users:
        UserID
        UserName
        Email
        DOB
        Password
    Household:
        HouseholdID
        Members
        HouseholdName
    Pantry:
        PantryName
        PantryID
    Items:
        ItemID
        Quantity
        Owner
        ItemName
        InDate
    Recipe:
        RecipeID
        RecipeBody
        RecipeName
    
    Many User Member of Many Household
    One Household Owns Many Pantry
    One Pantry Contains Many Items
    Many Household Holds Many Recipes
    Many User Holds Many Recipes
'''