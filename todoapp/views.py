from django.shortcuts import render,redirect
from .models import todo

def index(request):
    usr = todo.objects.all()
    return render(request,'add.html',{'show':usr})
def mod(request):
    if request.method=="POST":
        text=request.POST.get('todo')

        obj=todo()
        obj.txt=text
        obj.save()

        return redirect('/')
def edit(request, id):
    usr = todo.objects.get(id=id)
    return render(request,'edit.html', {'user':usr})
def update(request, id):
    if request.method == "POST":
        emp = todo.objects.get(id=id)
        emp.txt= request.POST.get('todo')
        emp.save()
    return redirect("/")

def destroy(request, id):
    employee = todo.objects.get(id=id)
    employee.delete()
    return redirect("/")