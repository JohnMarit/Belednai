from django.shortcuts import render
from firebase_admin import firestore

# Initialize Firestore
db = firestore.client()

def user_list(request):
    # Fetch all users from Firebase
    users_ref = db.collection('users')
    users = users_ref.stream()

    # Convert Firebase data to a list of dictionaries
    user_list = []
    for user in users:
        user_list.append(user.to_dict())

    # Pass the data to the template
    context = {'users': user_list}
    return render(request, 'user_list.html', context)