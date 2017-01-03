from django.shortcuts import render
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.shortcuts import redirect

from data.models import Aliquot
from .forms import AliquotForm


def home(request):
    return render(request, "home.html")

def aliquot(request):
    available_aliquots = Aliquot.objects.filter(available_flag = "Y")
    context = {'available_aliquots': available_aliquots,
               }
    return render(request, "aliquot.html", context)

def AliquotAddForm(request):
    if request.method == 'POST':
        form = AliquotForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AliquotForm(request.POST)
    return render(request, "aliquotAdd.html", {'form': form})

    ######################Working List of Forms######################
#def AliquotForm(request):
    #AliquotFormSet = modelformset_factory(Aliquot, fields=('aliquot_id', 'received_on', 'sample_type'))
    
    #if request.method == 'POST':
    #    formset = AliquotFormSet(request.POST, 
                                # request.FILES
                                #instance=post,
    #    )
    #    if formset.is_valid():
    #        formset.save()
            # do something.
            
    #else:
    #    formset = AliquotFormSet()
    #return render(request, 'aliquotAdd.html', {'formset': formset})



