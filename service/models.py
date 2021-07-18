from django.db import models
from accounts.models import Account


class Service(models.Model):
    title = models.CharField(max_length=200, help_text="Enter Service Title")
    description = models.TextField(help_text="Enter Product Description")
    price = models.CharField(max_length=20, help_text="Enter Product price")
    group = models.CharField(max_length=50, help_text="Enter Product group", default='computerService')
    groupPersian = models.CharField(max_length=50, help_text="Enter Product group", null=True, default='تعمیر کامپیوتر')
    user = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE, null=True)
    Rating = models.IntegerField(default=5)

    def __str__(self):
        return self.title


class Comment(models.Model):
    service = models.ForeignKey(Service, to_field='id', on_delete=models.CASCADE, null=True)
    writerComment = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=200, default='عالی است')
    rate_AI = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.content


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    Services = models.ManyToManyField(Service)
    user = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return "%s the cart" % self.user.first_name