from django.db import models
from rent.models.rent import Rent


class Payment_type(models.Model):
    method = models.CharField(max_length=100)


class Payment(models.Model):
    # 因為有真實出租出去才需要支付費用, 但也可能下了訂單沒有真實去開車 => violation
    rent_id = models.OneToOneField(
        Rent, on_delete=models.CASCADE, related_name="payment"
    )
    payment_type_id = models.ForeignKey(
        Payment_type, on_delete=models.CASCADE, related_name="payment_record"
    )
    fee = models.IntegerField(default=0)

    # 發票號碼 => 已經支付完成
    invoice_no = models.CharField(max_length=100)
