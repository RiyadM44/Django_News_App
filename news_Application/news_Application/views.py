# views.py
from django.shortcuts import render, redirect
from .forms import TextInputForm

def save_text_input(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = TextInputForm()
    return render(request, 'hello.html', {'form': form})
