# views.py
from django.shortcuts import render, redirect
from .forms import TextInputForm
from django.http import JsonResponse
# from .models import NewsData

# def save_text_input(request):
#     if request.method == 'POST':
#         form = TextInputForm(request.POST)
#         # if form.is_valid():
#         form.save()
#             # return redirect('')
#             # return redirect('success_url')
#     else:
#         form = TextInputForm()
#     return render(request, 'index.html', {'form': form})

def save_text_input(request):
    return render(request, 'index.html')

def show_news(request):
    # Add any necessary logic here
    return render(request, 'News.html')

# def create_news(request):
#     if request.method == 'POST':
#         data = request.POST
#         news = NewsData.objects.create(
#             title=data.get('newsTitle'),
#             description=data.get('newsDescription'),
#             image_url=data.get('newsImageUrl'),
#             news_url=data.get('newsUrl')
#         )
#         return JsonResponse({'message': 'News created successfully.'})
#     else:
#         return JsonResponse({'error': 'Invalid request method.'}, status=400)
