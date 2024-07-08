from faker import Faker

faker = Faker()
Name = input("enter RND for random name(enter anything else for custom name): ")
if Name == 'RND':
    Name = faker.name()
else:
    Name = input("Enter Human name")
ADBOOL = input("do you want address?")
if ADBOOL == 'yes':
    address = faker.address()
else:
    address = None
EMBOOL = input("do you want email?(with google domain)")
if EMBOOL == 'yes':
    email = faker.email(True, "google.com")
else:
    email = None
CCBOOL = input("do you want Credit card address?(visa type only)")
if CCBOOL == 'yes':
    Credit = faker.credit_card_number('visa')
else:
    Credit = None
BDBOOL = input("do you want Birth Date?")
if BDBOOL == 'yes':
    MINAGE = int(input("Enter minimum age (def = 0)"))
    MAXAGE = int(input("Enter maximum age (def = 115)"))
    birthday = faker.date_of_birth(None, MINAGE, MAXAGE)
else:
    birthday = None
print("here's you data!")
print("Name", Name, "Address", address, "Email", email, "Credit Card", Credit, "Birth Date", birthday)
