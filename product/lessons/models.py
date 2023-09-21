from django.db import models


class Owner(models.Model):
    owner_name = models.CharField(max_length=20)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.owner_name


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=200)
    video = models.URLField(max_length=200)
    time_video = models.DurationField()

    def __str__(self):
        return self.lesson_name


class Product(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    lesson = models.ManyToManyField(Lesson)
    product_name = models.CharField(max_length=20)
    product_description = models.TextField()

    def __str__(self):
        return self.product_name

# class Lesson(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     lesson_name = models.CharField(max_length=200)
#     video = models.URLField(max_length=200)
#     time_video = models.DurationField()
#
#     def __str__(self):
#         return self.lesson_name
