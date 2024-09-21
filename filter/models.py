from django.db import models

class Category(models.Model):
    
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Option(models.Model):
    
    categories = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="options")
    option_name = models.CharField(max_length=255)
    option_value = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.option_name