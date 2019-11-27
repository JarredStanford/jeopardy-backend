from django.db import models

# Create your models here.
class Answer(models.Model):
    category = models.CharField(max_length=200,default=None, blank=True, null=True)
    air_date = models.DateTimeField('date aired',default=None, blank=True, null=True)
    question = models.CharField(max_length=1000,default=None, blank=True, null=True)
    value = models.CharField(max_length=20,default=None, blank=True, null=True)
    answer = models.CharField(max_length=200,default=None, blank=True, null=True)
    round = models.CharField(max_length=50,default=None, blank=True, null=True)
    show_number = models.CharField(max_length=50,default=None, blank=True, null=True)

    def __str__(self):
        return f'Category: {self.category}, Question: {self.question}, Answer: {self.answer}, value: {self.value}'