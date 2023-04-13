from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://web10_user:567234@cluster0.vc2lsr9.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.web10

if __name__ == "__main__":
    cats = db.cats.find()
    for cat in cats:
        print(cat)
