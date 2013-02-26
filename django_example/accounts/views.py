from __future__ import unicode_literals

import balanced

from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def index(request):
    accounts = balanced.Account.query
    return render_to_response(
        'accounts/index.html',
        {
            'accounts': accounts,
        },
        context_instance=RequestContext(request)
    )


def show(request, account_id):
    account = balanced.Account.find(fucking_shit_hack_remove_me(account_id))
    if request.method == 'PUT':
        return update(request, account_id)

    return render_to_response(
        'accounts/show.html',
        {
            'account': account
        },
        context_instance=RequestContext(request)
    )


def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email_address = request.POST['email_address']
        # here we're using django-balanced to create an account implicitly via
        # the User create method. it may be simpler and cleaner to keep this
        # example focussed only on the balanced library.
        user, created = User.objects.get_or_create(
            username=name or email_address,
            email=email_address,
            password='supersecret',
        )
        user.save()
        return redirect('accounts.show',
                        account_id=user.balanced_account.id)
    else:
        return render_to_response(
            'accounts/create.html',
            {
            },
            context_instance=RequestContext(request)
        )


def update(request, account_id):
    return redirect('accounts.show',
                    account_id=account_id)


def debit(request, account_id):
    account = balanced.Account.find(fucking_shit_hack_remove_me(account_id))
    if request.method == 'POST':
        amount = int(float(request.POST['amount'])) * 100
        source_uri = request.POST['source_uri']
        account.debit(amount=amount,
                      source_uri=source_uri)
    return redirect('accounts.show',
                    account_id=account_id)


def credit(request, account_id):
    account = balanced.Account.find(fucking_shit_hack_remove_me(account_id))
    if request.method == 'POST':
        amount = int(float(request.POST['amount'])) * 100
        source_uri = request.POST['source_uri']
        account.credit(amount=amount,
                       source_uri=source_uri)
    return redirect('accounts.show',
                    account_id=account_id)


def fucking_shit_hack_remove_me(account_id):
    return '/'.join([
        balanced.Marketplace.my_marketplace.accounts_uri, account_id
    ])
