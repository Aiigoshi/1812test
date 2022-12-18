from django.db import models


class MyTable(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to="myapp/static", blank=True)

  




class MyLessons(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to="myapp/static", blank=True)
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Мои уроки'
# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)


    def speak(self):
        print(f"The {self.name} says {self.sound}")
        return f"The {self.name} says {self.sound}"