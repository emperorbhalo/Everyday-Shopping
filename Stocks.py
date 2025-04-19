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
    
email=client["Project-A"]
stocks=email["stocks"]
    
stocks.insert_many[
    {"HP EliteBook 830 G8":1173.79,"piece":12},
    {"Asus ROG Strix SCAR 18":7442.52,"piece":10},
    {"ASUS ROG Strix G16":1330.08,"piece":2},
    {"Acer Swift 3 Intel Evo":797.78,"piece":4},
    {"acer 15.6":699.00,"piece":7},
    {"acer Aspire Go 15":499.00,"piece":5},
    {"ACEMAGIC 2025":342.09,"piece":9}
]

#def buying():
    
                        #NOW HOW DO I MAKE A BALANCE SYSTEM?? HOW DO I GET THE OTHER BALANCE FROM THERE?

def restocking():
    stocking = int(input("Enter how many pieces you want to stock: "))
    product = input("Enter which product you want to restock: ")

    product_doc = stocks.find_one({"product": product})
    if product_doc is None:  #checls if we got any product's or no
        print("Product not found.")
        return

    stocks.update_one(
        {"product": product},
        {"$inc": {"piece": stocking}}
    )

    print(f"{stocking} pieces added to {product}.")
