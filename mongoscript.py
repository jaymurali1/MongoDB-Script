import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://ImagineRIT2024:TbcYVfnMAfhqYzTX%23d@tide.csh.rit.edu/?ssl=true&authSource=ImagineRIT2024")
database = client["ImagineRIT2024"]  # Replace "mydatabase" with your database name
collection = database["default"]  # Replace "mycollection" with your collection name

# Function to add data to MongoDB
def add_data(data):
    collection.insert_one(data)
    print("Data added successfully.")

# Function to retrieve data from MongoDB
def retrieve_data(query=None):
    if query:
        data = collection.find(query)
    else:
        data = collection.find()
        
    for item in data:
        print(item)

# # Example data to add
# example_data = {""}

# # Add data to MongoDB
# add_data(example_data)

# Retrieve data from MongoDB
print("\nRetrieving data from MongoDB:")
retrieve_data()

# Close connection
client.close()
