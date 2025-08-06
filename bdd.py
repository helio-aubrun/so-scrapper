from pymongo import MongoClient

def connect_db(uri="mongodb://localhost:27017/", db_name="so_scraper", collection_name="questions"):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    return collection

def insert_data(collection, data):
    if not data:
        print("[WARNING] Aucune donnée à insérer.")
        return
    if isinstance(data, list):
        result = collection.insert_many(data)
        print(f"[INFO] {len(result.inserted_ids)} documents insérés.")
    else:
        result = collection.insert_one(data)
        print("[INFO] 1 document inséré.")
