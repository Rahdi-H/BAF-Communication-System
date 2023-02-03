from django.shortcuts import render, redirect
from .models import LOS
from .admin import LOSResouce
from .forms import LoginForm, LOSForm
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, UpdateView

# Create your views here.

@login_required(login_url='/login/')
def home(request):
    context= {

    }
    return render(request, 'unit/home.html', context)

def loginn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        messages.warning(request, "Username or Password didn't matched")
        return render(request, 'unit/login.html')
    else:
        form = LoginForm()
        return render(request, 'unit/login.html', {'form':form})

@login_required(login_url='/login/') 
def logoutt(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def in_los(request):
    if request.method == 'POST':
        messages = LOS.objects.filter(receiver_unit=request.user.id).order_by('-id')
        dateset = LOSResouce().export(messages)
        ds = dateset.xls
        response = HttpResponse(ds, content_type="xls")
        response['Content-Disposition'] = "attachment; filename=in_los.xls"
        return response

    messages = LOS.objects.filter(receiver_unit=request.user.id).order_by('-id')
    lenn = len(messages)
    context = {
        'messages' : messages,
        'lenn' : lenn,
    }
    return render(request, 'unit/in_los.html', context)

@login_required(login_url='/login/')
def out_los(request):
    messages = LOS.objects.filter(sender=request.user).order_by('-id')
    context = {
        'messages':messages,
    }
    return render(request, 'unit/out_los.html', context)

# @login_required(login_url='/login/')
# def los_add(request):
#     if request.method == 'POST':
#         form = LOSForm(request.POST)
#         if form.is_valid:
#             instance = form.save(commit=False)
#             instance.sender = request.user
#             instance.save()
#             messages.success(request, 'Successfully saved & sent the message')
#             return redirect('los-add')
#         else:
#             messages.warning(request, 'Something went wrong please try again')
#             return redirect('los-add')
#     else:
#         form = LOSForm()
#         context = {
#             'form':form,
#         }
#         return render(request, 'unit/los_add.html', context)

class LosCreateView(CreateView):
    model = LOS
    form_class = LOSForm
    template_name = 'unit/los_add.html'
    success_url = '/out-los/add'   

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.sender = self.request.user
        instance.save()
        return super().form_valid(form)
    
class LosUpdateView(UpdateView):
    model = LOS
    form_class = LOSForm
    template_name = 'unit/los_update.html'
    success_url = '/out-los/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.sender = self.request.user
        instance.save()
        return super().form_valid(form)