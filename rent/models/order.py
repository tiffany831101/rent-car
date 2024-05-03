from django.db import models

from rent.models.users import CustomUser
from rent.models.vehicles import Vehicles
from rent.models.city import City


class Order(models.Model):
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="orders"
    )
    vehicle_id = models.ForeignKey(
        Vehicles, on_delete=models.CASCADE, related_name="orders"
    )
    rent_city_id = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="orders"
    )

    minutes = models.IntegerField()

    # need to set the rent time and the return time
    # can not be null => if yes can not be set to the db
    rent_time = models.DateTimeField()
    expected_return_time = models.DateTimeField()
