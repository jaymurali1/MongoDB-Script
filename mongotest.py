import pymongo

# Test if PyMongo is installed successfully
try:
    client = pymongo.MongoClient("mongodb://ImagineRIT2024:TbcYVfnMAfhqYzTX%23d@tide.csh.rit.edu/?ssl=true&authSource=ImagineRIT2024")
    print("PyMongo is installed and ready to be used.")
except Exception as e:
    print(f"Error: {e}")