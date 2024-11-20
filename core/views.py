from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, ProfileForm
from django.db import transaction
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderException


# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user_form.save()
                profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('core:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    # Get connected social accounts
    social_accounts = SocialAccount.objects.filter(user=request.user)
    connected_providers = [account.provider for account in social_accounts]

    # Get available providers
    available_providers = []
    provider_list = providers.registry.provider_map.values()
    for provider in provider_list:
        try:
            if provider.id not in connected_providers:
                available_providers.append({
                    'id': provider.id,
                    'name': provider.name,
                })
        except ProviderException:
            continue

    return render(request, 'core/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'social_accounts': social_accounts,
        'available_providers': available_providers,
        'connected_providers': connected_providers,
    })
