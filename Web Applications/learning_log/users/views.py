from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page
            login(request, new_user) # log in the user by using the login function with the request and new_user objects
            return redirect('learning_logs:index') # after login, redirect the user to the homepage

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)