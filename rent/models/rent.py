from django.db import models
from rent.models.order import Order
from rent.models.city import City


class Rent(models.Model):
    # rent and order should be one on one
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)

    # 真實被借出去的時間
    created_time = models.DateTimeField(auto_now_add=True)

    # the time that the car is returned.. will be null when created => does not know when the car will be return
    actual_return_time = models.DateTimeField(null=True)
    actual_return_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="rents"
    )
