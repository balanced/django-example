from __future__ import unicode_literals

import balanced

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from django_balanced.models import Account

from accounts.views import fucking_shit_hack_remove_me


def index(request, account_id):
    account = balanced.Account.find(fucking_shit_hack_remove_me(account_id))
    return render_to_response(
        'card_processing/index.html',
        {
            'account': account
        },
        context_instance=RequestContext(request)
    )


def show(request, account_id, card_id):
    if request.method == 'PUT':
        return update(request, account_id, card_id)
    account = balanced.Account.find(fucking_shit_hack_remove_me(account_id))
    card_uri = '/'.join([account.cards_uri, card_id])
    card = balanced.Card.find(card_uri)
    return render_to_response(
        'card_processing/show.html',
        {
            'account': account,
            'card': card
        },
        context_instance=RequestContext(request)
    )


def create(request, account_id):
    if request.method == 'POST':
        card = balanced.Card.find(request.POST['balancedCreditCardURI'])
        account = balanced.Account.find(
            fucking_shit_hack_remove_me(account_id)
        )
        account.add_card(card.uri)
        return redirect('card_processing.show',
                        account_id=account_id,
                        card_id=card.id)

    return render_to_response(
        'card_processing/create.html',
        {
            'account': account_id,
        },
        context_instance=RequestContext(request)
    )


def update(request, account_id, card_id):
    return redirect('card_processing.show',
                    account_id=account_id,
                    card_id=card_id)


def overview(request):
    return render_to_response(
        'card_processing/overview.html',
        {

        },
        context_instance=RequestContext(request)
    )
