from django.db import models
from django.shortcuts import reverse
from django.conf import settings



CATEGORY_CHOICES = (
    ('Shirt', 'Shirt'),
    ('Sport Wear','Sport Wear'),
    ('Otwear', 'Outwear')
)

LABEL_CHOICES = (
    ('primary', 'primary'),
    ('secondary', 'secondary'),
    ('danger', 'danger')
)

class Item(models.Model):
    title =         models.CharField(max_length=255)
    slug =          models.SlugField(max_length=255)
    
    price =         models.FloatField()
    category =      models.CharField(choices=CATEGORY_CHOICES, max_length=128)
    label =         models.CharField(choices=LABEL_CHOICES, max_length =128)
    new_product =   models.BooleanField(default=False)
    best_seller =   models.BooleanField(default=False)
    description =   models.TextField()

  


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    # def get_add_to_car_url(self):
    #      return reverse("add_to_car", kwargs={"slug": self.slug})
       

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity =      models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item.title


class Order(models.Model):
    user =          models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items =         models.ManyToManyField(OrderItem)
    start_date =    models.DateTimeField(auto_now_add=True)  
    ordered_date =  models.DateTimeField()
    ordered =       models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
