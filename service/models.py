from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200, help_text="Enter Service Title")
    description = models.TextField(help_text="Enter Product Description")
    price = models.CharField(max_length=20, help_text="Enter Product price")
    group = models.CharField(max_length=20, help_text="Enter Product group", default='computerService')

    # eraee dahande service kie

    def __str__(self):
        return self.title
