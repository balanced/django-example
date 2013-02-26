from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import accounts
import ach
import card_processing
from accounts import views
from ach import views
from card_processing import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_example.views.home', name='home'),
    # url(r'^django_example/', include('django_example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # root url
    url(r'^$',
        accounts.views.index,
        name='home'),
    # accounts urls
    url(r'^accounts$',
        accounts.views.index,
        name='accounts.index'),
    url(r'^accounts/new$',
        accounts.views.create,
        name='accounts.create'),
    url(r'^accounts/(?P<account_id>\w+)$',
        accounts.views.show,
        name='accounts.show'),
    url(r'^accounts/(?P<account_id>\w+)/debit$',
        accounts.views.debit,
        name='accounts.debit'),
    url(r'^accounts/(?P<account_id>\w+)/credit$',
        accounts.views.credit,
        name='accounts.credit'),

    # card processing urls
    url(r'^(?P<account_id>\w+)/cards$',
        card_processing.views.index,
        name='card_processing.index'),
    url(r'^(?P<account_id>\w+)/cards/new$',
        card_processing.views.create,
        name='card_processing.create'),
    url(r'^(?P<account_id>\w+)/cards/(?P<card_id>\w+)$',
        card_processing.views.show,
        name='card_processing.show'),
    url(r'^card_processing$',
        card_processing.views.overview,
        name='card_processing.overview'),

    # bank account urls
    url(r'^(?P<account_id>\w+)/bank_accounts$',
        ach.views.index,
        name='ach.index'),
    url(r'^(?P<account_id>\w+)/bank_accounts/new$',
        ach.views.create,
        name='ach.create'),
    url(r'^(?P<account_id>\w+)/bank_accounts/(?P<bank_account_id>\w+)$',
        ach.views.show,
        name='ach.show'),
    url(r'^bank_accounts',
        ach.views.overview,
        name='ach.overview'),

)

urlpatterns += staticfiles_urlpatterns()
