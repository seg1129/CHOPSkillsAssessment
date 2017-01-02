from django.shortcuts import render
from django.http import HttpResponse
from data.models import Aliquot



def home(request):
    return render(request, "home.html")

def aliquot(request):
    available_aliquots = Aliquot.objects.filter(available_flag = "Y")
    context = {'available_aliquots': available_aliquots,
               }
    return render(request, "aliquot.html", context)

def aliquotAdd(request):
    return render(request, "aliquotAdd.html")

#def aliquotList(request):
 #   AliquotFormSet = formset_factory(AliquotForm)
 #   return render(request, "aliquotList.html", {'formset': formset})

#def aliquotList(request):
#    AliquotFormSet = formset_factory(AliquotForm)
#    if request.method == 'aliquotList':
#        formset = AliquotFormSet(request.aliquotList, request.FILES)
#        if formset.is_valid():
            # do something with the formset.cleaned_data
#            pass
#    else:
#        formset = AliquotFormSet()
#    return render(request, 'aliquotList.html', {'formset': formset})

