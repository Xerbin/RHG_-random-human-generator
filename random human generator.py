from faker import Faker

faker = Faker()
Name = input("enter RND for random name(or enter your custom name): ")
if Name == 'RND':
    Name = faker.name()
#ADBOOL = input("do you want an address?")
#if ADBOOL == 'yes':
    address = faker.address()
#else:
#    address = None
#EMBOOL = input("do you want an email?")
#if EMBOOL == 'yes':
email = faker.email(True, "google.com")
#else:
#    email = None
#CCBOOL = input("do you want the visa credit card info?")
#if CCBOOL == 'yes':
Credit = faker.credit_card_number('visa')
#else:
#    Credit = None
#BDBOOL = input("do you want Birth Date?")
#if BDBOOL == 'yes':
MINAGE = int(input("Enter minimum age (def = 0)"))
MAXAGE = int(input("Enter maximum age (def = 115)"))
birthday = faker.date_of_birth(None, MINAGE, MAXAGE)
#else:
#    birthday = None
print("here's you data!")
print("Name: ", Name) 
print("Address: ", address)
print("Email: ", email)
print("Credit Card info: ", Credit)
print("Birth Date: ", birthday)

