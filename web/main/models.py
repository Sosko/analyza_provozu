from django.db import models


class Cars(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '%s (%d)' % (self.name, self.id)

    def get_absolute_url(self):
        return u'/car/%d' % self.id


# Create your models here.
class Uploads(models.Model):
    name = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return u'/upload/%d' % self.id


class Positions(models.Model):
    date = models.DateTimeField()
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
