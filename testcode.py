import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from pizzas.models import *

pizzas = Pizza.objects.all()

p = Pizza.objects.get(id=1)

toppings = Topping.objects.filter(pizza=p)


