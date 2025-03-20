from django.shortcuts import redirect
from firebase_admin import firestore

# Initialize Firestore
db = firestore.client()

def delete_user(request, username):
    # Delete user from Firebase
    db.collection('users').document(username).delete()
    return redirect('user_list')