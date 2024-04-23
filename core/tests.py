from config.wsgi import *
from django.test import TestCase
from core.models import *

query = Type.objects.all()
print(query)

t = Type.objects.get(pk=1)
print(t)