# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SalesModel(models.Model):
    id = models.IntegerField(primary_key=True)
    order_id = models.CharField(max_length=20)
    order_date = models.DateField()
    customer_id = models.CharField(max_length=10)
    sub_category = models.CharField(max_length=20)
    region = models.CharField(max_length=10)
    sales = models.FloatField()