from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=15)
#     class Meta:
#         db_table = 'category'
#
#     def __str__(self):
#         return self.name
#
# class Product(models.Model):
#     name = models.CharField(max_length=15, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.ManyToManyField(Category)
#
#     class Meta:
#         db_table = 'products'
#
#     def __str__(self):
#         return f'{self.name} - {self.category}'
#
#
# class Supplier(models.Model):
#     name = models.CharField(max_length=20)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name + ' - ' + self.product.name
