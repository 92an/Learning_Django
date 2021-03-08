from .forms import ItemForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item
from django.template import context, loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template("food/index.html")
    context = {
        'item_list':item_list,
    }
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse("This is an item")


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request, 'food/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("food:index")

    return render(request, "food/itemform.html", {"form":form})

def edit_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("food:index")

    return render(request, "food/itemform.html", {"form":form, "item":item})

def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == "POST":
        item.delete()
        return redirect("food:index")

    return render(request, "food/itemdelete.html", {"item":item} )
