from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """
    Форма отправки обратной связи
    """

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
