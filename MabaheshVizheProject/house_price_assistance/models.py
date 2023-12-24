from django.db import models


class PredictPriceModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    predict_price = models.CharField(max_length=100)
    room = models.IntegerField()
    state = models.CharField(max_length=100)
    needParking = models.BooleanField(default=False)
    needWareHouse = models.BooleanField(default=False)
    needElevator = models.BooleanField(default=False)

    def __str__(self):
        return self.name  
    # تغییر به فیلدی که می‌خواهید در admin نمایش داده شود
