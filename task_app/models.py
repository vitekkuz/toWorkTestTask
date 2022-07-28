from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Profession(models.Model):
    text = models.CharField(max_length=150, blank=False, unique=True)

    def count_users(self):
        return self.user_set.count()

    def __str__(self):
        return self.text

    class Meta:
         verbose_name = "Профессия"
         verbose_name_plural = "Профессии"


class Sex(models.Model):

    SEX = [
        ('М', 'Мужчина'),
        ('Ж', 'Женщина')
    ]

    sex = models.CharField("sex", choices=SEX, blank=False, max_length=1, unique=True) # М или Ж

    def __str__(self):
        return self.sex

    class Meta:
         verbose_name = "Пол"
         verbose_name_plural = "Пол"


class PhoneNumber(models.Model):
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)

    def __str__(self):
        return self.phoneNumber

    class Meta:
         verbose_name = "Номер телефона"
         verbose_name_plural = "Номера телефона"


# Модели для формирования адреса
class Aria(models.Model):
    text = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.text

    class Meta:
         verbose_name = "Область"
         verbose_name_plural = "Области"


class District(models.Model):
    text = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.text

    class Meta:
         verbose_name = "Район"
         verbose_name_plural = "Районы"

class City(models.Model):
    text = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.text

    class Meta:
         verbose_name = "Город"
         verbose_name_plural = "Города"


# Модель пользователя
class User(models.Model):
    surname = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=False, default='-')
    first_name = models.CharField(max_length=100, blank=False)
    sex = models.ForeignKey(Sex, on_delete=models.PROTECT, default='М')
    age = models.PositiveSmallIntegerField(blank=False)
    phoneNumber = models.OneToOneField(PhoneNumber, on_delete=models.PROTECT)
    profession = models.ForeignKey(Profession, on_delete=models.PROTECT)
    area = models.ForeignKey(Aria, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.surname} {self.first_name} {self.middle_name}'

    class Meta:
         verbose_name = "Пользователь"
         verbose_name_plural = "Пользователи"

    def get_address(self):
        return f'{self.area} область, {self.district} р-н, г. {self.city}'
