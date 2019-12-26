from django.shortcuts import render,redirect
from .models import Todo
from .form import TodoForm 

# Create your views here.
def index(request):
    context=Todo.objects.order_by('id')
    form=TodoForm()
    
    return render(request,'index.html',{'todo':context ,'forms':form})

def todoforms(request):
    form= TodoForm(request.POST)
    if form.is_valid():
        new_todo=Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('/')
def update(request,id):
    todo=Todo.objects.get(pk=id)
    todo.complete=True
    todo.save()
    return redirect('/')
def destroy(request):
    todo=Todo.objects.all()
    todo.delete()
    return redirect('/')