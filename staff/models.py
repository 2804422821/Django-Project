from django.db import models

# Create your models here.
class Staff(models.Model):
    GENDER_CHOICES = (('male', '男'),
                      ('female', '女'),)
    name = models.CharField(max_length=30, default=True, verbose_name="姓 名")
    account = models.IntegerField(unique=True, default=True, verbose_name="工 号")
    birthday = models.DateField(blank=True, null=True, verbose_name="出 生 日 期")
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, default="male", verbose_name="性 别")
    department = models.CharField(max_length=30, null=True, blank=True, verbose_name="部 门")
    position = models.CharField(max_length=30, null=True, blank=True, verbose_name="职位")
    mobile = models.CharField(max_length=11, blank=True, default=True, verbose_name="电 话")

    def __str__(self):
        return self.account
