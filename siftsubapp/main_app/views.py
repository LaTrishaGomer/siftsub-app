from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Subscription
from .forms import SubscriptionForm
from datetime import date, timedelta
from django.db.models.functions import TruncMonth
from django.db.models import Sum
import calendar


def home(request):
    error_message = ''
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid login credentials'

    return render(request, 'home.html', {
        'form': form,
        'error_message': error_message,
        'on_homepage': True
    })


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


def signin(request):
    error_message = ''
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid login credentials'

    return render(request, 'signin.html', {
        'form': form,
        'error_message': error_message
    })


def about(request):
    return render(request, 'about.html')


@login_required
def subscription_detail(request, subscription_id):
    subscription = Subscription.objects.get(id=subscription_id)
    return render(request, 'subscriptions/detail.html', {
        'subscription': subscription
    })


@login_required
def archive_subscription(request, subscription_id):
    subscription = Subscription.objects.get(id=subscription_id)
    if subscription.user == request.user:
        subscription.is_active = False
        subscription.save()
    return redirect('dashboard')


@login_required
def dashboard(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    total_cost = subscriptions.aggregate(Sum('cost'))['cost__sum'] or 0

    today = date.today()
    upcoming = subscriptions.filter(renewal_date__range=[today, today + timedelta(days=3)])

    monthly_data = (
        subscriptions
        .annotate(month=TruncMonth('renewal_date'))
        .values('month')
        .annotate(monthly_total=Sum('cost'))
        .order_by('month')
    )

    chart_labels = [calendar.month_abbr[item['month'].month] for item in monthly_data]
    chart_data = [float(item['monthly_total']) for item in monthly_data]

    return render(request, 'dashboard.html', {
        'subscriptions': subscriptions,
        'total_cost': total_cost,
        'upcoming': upcoming,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
    })


class SubscriptionCreate(LoginRequiredMixin, CreateView):
    model = Subscription
    form_class = SubscriptionForm
    template_name = 'subscription_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SubscriptionUpdate(LoginRequiredMixin, UpdateView):
    model = Subscription
    form_class = SubscriptionForm
    template_name = 'subscription_form.html'
    success_url = reverse_lazy('dashboard')


class SubscriptionDelete(LoginRequiredMixin, DeleteView):
    model = Subscription
    template_name = 'subscription_confirm_delete.html'
    success_url = reverse_lazy('dashboard')




