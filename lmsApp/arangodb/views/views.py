# views.py

from django.shortcuts import get_object_or_404
from lmsApp.arangodb.arango_utils import connect_to_arangodb, create_document, get_document_by_id, update_document_by_id, delete_document_by_id
import json

# Connect to ArangoDB
db = connect_to_arangodb('Testdb', 'root', 'root')

# Create
def create_item(collection_name, data):
    collection = db[collection_name]
    create_document(collection, data)

# Read
def get_item_by_id(collection_name, item_id):
    collection = db[collection_name]
    return get_document_by_id(collection, item_id)

# Update
def update_item_by_id(collection_name, item_id, new_data):
    collection = db[collection_name]
    update_document_by_id(collection, item_id, new_data)

# Delete
def delete_item_by_id(collection_name, item_id):
    collection = db[collection_name]
    delete_document_by_id(collection, item_id)


def get_all_items(collection_name):
    collection = db[collection_name]
    items = list(collection.fetchAll())  # Retrieve all documents from the collection
    return items

def serialize_to_json(items):
    # Serialize the list of documents to JSON format
    json_data = json.dumps([item._createDict() for item in items], default=str)
    return json_data