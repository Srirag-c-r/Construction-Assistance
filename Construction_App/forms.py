from django.contrib.auth.models import User
from django.forms import DateInput, FileInput, ModelForm, Select, TextInput, Textarea, TimeInput, ValidationError

class CustomPasswordResetForm(ModelForm):
    class Meta:
        model=User
        fields =['email']
        widgets = {
         
         'email': TextInput(
                attrs={'class': 'form-control','placeholder':'Email'}),
    }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError("There is no user registered with this email address.")
        return email
