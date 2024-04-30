from django.forms import *

from core.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Category: ',
            'description': 'Description: '
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Enter a category',
                }
            ),
            'description': Textarea(
                attrs={
                    'placeholder': 'Enter a description',
                    'rows': '4',
                }
            ),
        }
