from django.shortcuts import redirect,render
from django.http import HttpResponse

from lists.models import Item


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        newCreateitem = Item(text = request.POST['item_text'])
        newCreateitem.save()
        return redirect("/")
    else:
        return render(request, 'home.html',{
            'items': Item.objects.all()
        })
