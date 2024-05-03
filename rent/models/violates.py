from django.db import models
from rent.models.order import Order
from rent.models.users import CustomUser


class Violation_types(models.Model):
    name = models.TextField()

    # 也可能是下訂單但是沒有去真實去借車 => fee = 0 => 超過 n 次多久不能借車
    fee = models.IntegerField(default=0)


class Violation_records(models.Model):
    Violation_types_id = models.ForeignKey(
        Violation_types, on_delete=models.CASCADE, related_name="violate_records"
    )

    # has to change the the fk
    # 一筆訂單可能有多筆的違規紀錄
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="violate_records"
    )


# user that violates how many times...
# 就算已經付完罰款, 但是還是需要冷凍起來
class Violation_name_list(models.Model):
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="violate_records"
    )

    violate_record_id = models.ForeignKey(Violation_records, on_delete=models.CASCADE)
    started_time = models.DateTimeField()
    ended_time = models.DateTimeField()
