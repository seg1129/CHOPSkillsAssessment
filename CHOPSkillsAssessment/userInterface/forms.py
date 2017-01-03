from django.forms import ModelForm
from data.models import Aliquot

        
class AliquotForm(ModelForm):
    class Meta:
        model = Aliquot
        fields = '__all__'
        #fields = ['aliquot_id', 'received_on', 'sample_type']
