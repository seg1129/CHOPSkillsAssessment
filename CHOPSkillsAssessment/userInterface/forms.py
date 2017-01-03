from django.forms import ModelForm
from data.models import Aliquot

        
class AliquotForm(ModelForm):
    class Meta:
        model = Aliquot
        exclude = ['collected_on', 'sample_type_code', 'secondary_sample_code']
