from django.db import models

from rent.models.city import City


class Vender(models.Model):
    # name of the 車廠
    name = models.CharField(max_length=200)


class Vehicles_types(models.Model):

    class Size(models.IntegerChoices):
        SMALL = 4
        MEDIUM = 7

    vender_id = models.ForeignKey(
        Vender, on_delete=models.CASCADE, related_name="vehicles_types"
    )
    name = models.CharField(max_length=200)
    size = models.IntegerField(choices=Size, default=4)
    # 每分鐘多少錢
    price_per_minute = models.FloatField(default=1)
    # the year the car is bought
    produce_year = models.PositiveSmallIntegerField(blank=True, null=True)


class Vehicles(models.Model):
    vehicles_types_id = models.ForeignKey(
        Vehicles_types, on_delete=models.CASCADE, related_name="vehicles"
    )
    # 目前在哪個城市, 如果目前已經被出租 => 在起始地, 還車之後更改車子所在位置
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name="vehicles")
    # 車牌號碼
    lisense_no = models.CharField(max_length=200)
    is_rent = models.BooleanField(default=False)
