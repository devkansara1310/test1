from order import models
from order.models import Order
from django import forms
from django.shortcuts import render
from .forms import orderForm
from django.views.generic import UpdateView, CreateView, DetailView, DeleteView, ListView
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.

def index(request):
    if request.method== 'GET':
        query = request.GET.get('search')
        search = Order.object.filter(Q(customer_id__icontains=query) | Q(product_id__icontains=query))
        context1 = {'search':search}
        return render(request,'search.html',context1)
    form = orderForm()

    if request.method == 'POST':
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'order.html',context)

    

class updateOrder(UpdateView):
    
    model = Order
    template_name = 'update.html'
    fields = '__all__'

class deleteOrder(DeleteView):
    model = Order
    template_name = 'delete.html'
    success_url = reverse_lazy('show')

def show(request):
    items = Order.objects.all()
    context= {'items': items}
    return render(request,'show.html',context)

