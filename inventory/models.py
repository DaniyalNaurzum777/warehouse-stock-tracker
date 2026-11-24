from django.db import models


class Product(models.Model):
    name = models.CharField("Тауар атауы", max_length=150)
    quantity = models.PositiveIntegerField("Ағымдағы саны")
    min_quantity = models.PositiveIntegerField("Ең аз қор мөлшері")
    created_at = models.DateTimeField("Тіркелген уақыты", auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Тауар"
        verbose_name_plural = "Тауарлар"

    @property
    def is_low_stock(self):
        return self.quantity <= self.min_quantity

    def __str__(self):
        return self.name
