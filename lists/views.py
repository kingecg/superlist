from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        newCreateitem = request.POST['item_text']
        return render(request, 'home.html', {
            'new_item_text': '1:'+newCreateitem
        })
    else:
        return render(request, 'home.html')
