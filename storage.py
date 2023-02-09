import pyrebase
import os
# Upload customer image to firebase
def upload_to_storage(dirname):
    config = {
        "apiKey": "AIzaSyB7XJgi-Ffb69nkXGgSR2KtZBJBxtz-Xc0",
        "authDomain": "facepay-c4406.firebaseapp.com",
        "databaseURL": "https://facepay-c4406-default-rtdb.asia-southeast1.firebaseio.com",
        "projectId": "facepay-c4406",
        "storageBucket": "facepay-c4406.appspot.com",
        "messagingSenderId": "237899514967",
        "appId": "1:237899514967:web:1c665f418ba62df6780f12",

    }

    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    images = os.listdir('customer_images')

    for image in images:
        local_path = 'customer_images/'+image
        cloud_storage_path = 'customer_faces/'+image
        storage.child(cloud_storage_path).put(local_path)

    delete_images()

    return cloud_storage_path

# Delete customer image once it has beeen uploaded


def delete_images():
    images = os.listdir('customer_images')

    for image in images:
        delete_path = 'customer_images/'+image
        os.remove(delete_path)

# Download customer images from database for facial recogniton algorithm


def download_from_storage(ref_list):
    config = {
        "apiKey": "AIzaSyB7XJgi-Ffb69nkXGgSR2KtZBJBxtz-Xc0",
        "authDomain": "facepay-c4406.firebaseapp.com",
        "databaseURL": "https://facepay-c4406-default-rtdb.asia-southeast1.firebasedatabase.app/",
        "projectId": "facepay-c4406",
        "storageBucket": "facepay-c4406.appspot.com",
        "messagingSenderId": "237899514967",
        "appId": "1:237899514967:web:1c665f418ba62df6780f12",

    }

    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()

    for ref in ref_list:
        local_path = ref
        storage_path = ref
        storage.child(storage_path).download(local_path)
