import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
fileName = credentials.Certificate('json_file.json')
firebase_admin.initialize_app(fileName, {
                  'databaseURL': 'https://python-1-dc357-default-rtdb.europe-west1.firebasedatabase.app/'
})
ref = db.reference('user')
print(ref.get())