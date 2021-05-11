from basic import db,Puppy

# CREATES ALL THE TABLES Model --> Db Table
db.create_all()

# Create two Puppy objects
sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

# Says none because they do not have ID
print(sam.id)
print(frank.id)

# Puts objects to be added to the database
db.session.add_all([sam, frank])
# Commits objects to database
db.session.commit()

print(sam.id)
print(frank.id)
