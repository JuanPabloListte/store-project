from apps.core.models import *

data = ['Carnes', 'Frutas', 'Verduras', 'Cereales']
for i in data:
    cat = Category(name=i)
    cat.save()
    print('Guardando registro N°: {}'.format(cat.id))
