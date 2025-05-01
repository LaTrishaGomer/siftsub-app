from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Subscription  

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('subscription-index')
        else:
            error_message = 'Invalid sign up - try again'

    form  = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def subscription_index(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    return render(request, 'subscriptions/index.html', {
        'subscriptions': subscriptions
    })

@login_required
def subscription_detail(request, subscription_id):
    subscription = Subscription.objects.get(id=subscription_id)
    return render(request, 'subscriptions/detail.html', {
        'subscription': subscription
    })

class SubscriptionCreate(LoginRequiredMixin, CreateView):
    model = Subscription
    fields = ['name', 'cost', 'renewal_date', 'status'] 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
