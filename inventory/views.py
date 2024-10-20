# # inventory/views.py
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Item
# from .forms import ItemForm
# from django.db.models import Q  # Import Q for complex queries

# def item_list(request):
#     query = request.GET.get('q')  # Get the search query from the request
#     if query:
#         items = Item.objects.filter(
#             Q(name__icontains=query) | Q(description__icontains=query)
#         )
#     else:
#         items = Item.objects.all()
#     return render(request, 'inventory/item_list.html', {'items': items, 'query': query})



# # View to create a new item
# def item_create(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('item_list')
#     else:
#         form = ItemForm()
#     return render(request, 'inventory/item_form.html', {'form': form})

# # View to update an item
# def item_update(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.method == 'POST':
#         form = ItemForm(request.POST, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect('item_list')
#     else:
#         form = ItemForm(instance=item)
#     return render(request, 'inventory/item_form.html', {'form': form})

# # View to delete an item
# def item_delete(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.method == 'POST':
#         item.delete()
#         return redirect('item_list')
#     return render(request, 'inventory/item_confirm_delete.html', {'item': item})


# inventory/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# def item_list(request):
#     query = request.GET.get('q')
#     items = Item.objects.filter(name__icontains=query) if query else Item.objects.all()
#     return render(request, 'inventory/item_list.html', {'items': items, 'query': query})

def item_list(request):
    items = Item.objects.all()
    # Calculate total inventory value
    total_inventory_value = sum(item.quantity * item.price for item in items)
    context = {
        'items': items,
        'total_inventory_value': total_inventory_value,
    }
    return render(request, 'inventory/item_list.html', context)


def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'inventory/item_form.html', {'form': form})

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('item_list')
