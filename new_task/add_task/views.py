from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .forms import MyForm
from .models import MyTask
from django.db.models import Q 

def home(request):
    query = request.GET.get('q')
    tasks = MyTask.objects.filter(user=request.user)
    if query:
        tasks = MyTask.objects.filter(
            Q(user=request.user), 
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        tasks = MyTask.objects.filter(user=request.user)

    return render(request, 'home_page.html', {'tasks': tasks})

def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MyForm()
    
    return render(request, 'form_page.html', {'form': form})

def task_edit(request, task_id):
    task = get_object_or_404(MyTask, pk=task_id)
    if request.method == 'POST':
        form = MyForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = MyForm(instance=task)
    
    return render(request, 'form_page.html', {'form': form})

def task_delete(request, task_id):
    task = get_object_or_404(MyTask, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')  
    
    return render(request, 'confirm_del.html', {'task': task})

def home_view(request):
    return render(request, 'main_home.html')
@csrf_protect
def login_view(request):
    return render(request, 'login.html')

