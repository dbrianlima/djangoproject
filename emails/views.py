from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import EmailEntry
from .forms import EmailEntryForm
# Create your views here.


def email_entry_get_view(request, id=None, *args, **kwargs):
    print(*args, kwargs)
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404
    return render(request, 'get.html', {'obj': obj})


def email_entry_create_view(request, *args, **kwargs):
    form = EmailEntryForm(request.POST)
    if form.is_valid():

        form.save()
        form = EmailEntryForm()

    return render(request, 'index.html', {'form': form})


# def email_entry_view(*args, **kwargs):


# def email_entry_listview():
    # return
