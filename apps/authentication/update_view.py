from django.shortcuts import render, redirect
from firebase_admin import firestore

# Initialize Firestore
db = firestore.client()

def update_user(request, username):
    if request.method == 'POST':
        # Get updated data from the form
        new_email = request.POST.get('email')

        # Update data in Firebase
        user_ref = db.collection('users').document(username)
        user_ref.update({'email': new_email})

        return redirect('user_list')
    
    # Fetch current user data
    user_ref = db.collection('users').document(username)
    user = user_ref.get().to_dict()

    # Pass the data to the template
    context = {'user': user}
    return render(request, 'update_user.html', context)