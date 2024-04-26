from django.shortcuts import render
from .forms import FeedbackForm


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def contact_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,
                          'thank_you.html')
    else:
        form = FeedbackForm()

    return render(request, 'contact_form.html', {'form': form})