# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Investigation, Instrument_Host, Instrument


# Create your views here.

@login_required
def context(request):
    context_dict = {
    }

    return render(request, 'context/repository/repository.html', context_dict)


#@login_required
def investigations(request):
    context_dict = {
        'investigations':Investigation.objects.all(),
    }

    return render(request, 'context/repository/investigations.html', context_dict)

#@login_required
def instrument_hosts(request):
    context_dict = {
        'instrument_hosts':Instrument_Host.objects.all(),
    }

    return render(request, 'context/repository/instrument_hosts.html', context_dict)

#@login_required
def instruments(request):
    context_dict = {
        'instruments':Instrument.objects.all(),
    }

    return render(request, 'context/repository/instruments.html', context_dict)
