
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://emperorbhalo:Ali09876@database.pu6qb.mongodb.net/?retryWrites=true&w=majority&appName=DATABASE"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
def info():
    email=client["Project-A"]
    users=email["users"]

    print("Enter your choice:")
    print("For sign-up enter 1")
    print("For Log-in enter 2")

    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if choice == 1:
        email_input = input("Enter your Email: ")
        password_input = input("Enter your Password: ")
        Balance_input = int(input("Enter your balance"))

        if users.find_one({"email": email_input}):
            print("This email is already registered.")
        else:
            users.insert_one({"email": email_input, "password": password_input, "Balance":Balance_input})
            print("Sign-up successful!")

    elif choice == 2:
        email_input = input("Enter your Email: ")
        password_input = input("Enter your Password: ")

        user = users.find_one({"email": email_input, "password": password_input})

        if user:
            print("Login successful!")
        else:
            print("Invalid email or password!")

    else:
        print("Invalid choice!")
    else:
        print(123)