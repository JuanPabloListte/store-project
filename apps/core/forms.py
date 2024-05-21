from django.forms import *

from apps.core.models import Category


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

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    def clean(self):
        data = super().clean()

        if len(data['name']) < 40:
            self.add_error('name', 'Name must be at least 4 characters long')
