from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class item(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()

    def _str_(self):
        return self.title


class Orderitem(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def _str_(self):
        return f'{self.quantity} of {self.item.title}'

class Order(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Orderitem)
    ordered = models.BooleanField(default=False)
    start_date =models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def _str_(self):
        return self.user.username


