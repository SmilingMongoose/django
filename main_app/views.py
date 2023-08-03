from django.shortcuts import render, redirect
from .forms import BasicInput
from .models import Visitor

# Create your views here.
def index(request):
    input_text = request.POST.get('visitor_input', None)
    print(input_text)
    if input_text == None:
        input_text = ''
    else:
        input_text = request.POST.get('visitor_input')
    
    visitors = Visitor.objects.all()

    context = {
        'visitors': visitors,
        'input_text': input_text
    }
    return render(request, 'index.html', context)

# def visitor_page(request):
#     context = {
#         'input_text_rec'
#     }

# def index(request):
#     if request.method == 'POST':
#         form = BasicInput(request.POST)
#         if form.is_valid():
#             form.save()

#         return redirect('index')
#     else:
#         form = BasicInput()
#         visitors = Visitor.objects.all()

#     context = {
#         'form': form,
#         'visitors': visitors     
#     }
#     return render(request, 'index.html', context)