from __future__ import unicode_literals

import balanced

from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from accounts.views import fucking_shit_hack_remove_me


def index(request, account_id):
    return render_to_response(
        'ach/index.html',
        {

        },
        context_instance=RequestContext(request)
    )


def show(request, account_id, bank_account_id):
    account = balanced.Account.find(fucking_shit_hack_remove_me(account_id))
    card_uri = '/'.join([account.bank_accounts_uri, bank_account_id])
    bank_account = balanced.BankAccount.find(card_uri)

    return render_to_response(
        'ach/show.html',
        {
            'account': account,
            'bank_account': bank_account
        },
        context_instance=RequestContext(request)
    )


def create(request, account_id):
    if request.method == 'POST':
        bank_account = balanced.BankAccount.find(
            request.POST['balancedBankAccountURI'])
        account = balanced.Account.find(
            fucking_shit_hack_remove_me(account_id)
        )
        account.add_bank_account(bank_account.uri)
        return redirect('ach.show',
                        account_id=account_id,
                        bank_account_id=bank_account.id)
    return render_to_response(
        'ach/create.html',
        {

        },
        context_instance=RequestContext(request)
    )


def validate(request, account_id, bank_account_id):
    return render_to_response(
        'ach/overview.html',
        {

        },
        context_instance=RequestContext(request)
    )


def confirm(request, account_id, bank_account_id):
    return render_to_response(
        'ach/confirm.html',
        {

        },
        context_instance=RequestContext(request)
    )


def overview(request):
    return render_to_response(
        'ach/overview.html',
        {

        },
        context_instance=RequestContext(request)
    )
