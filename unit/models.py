from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LOS(models.Model):
    serial = models.IntegerField()
    ref = models.CharField(max_length=255)
    originator = models.CharField(max_length=100)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True , related_name='senderr')
    receiver_unit = models.ManyToManyField(User, related_name='receivers', verbose_name='receiver_unit')
    main_receiver = models.CharField(max_length=255)
    file = models.FileField(upload_to='los/')
    date_of_rec = models.DateField()
    time_of_rec = models.TimeField()
    datetime_of_action = models.DateTimeField(auto_now_add=True)
    action_taken_by = models.CharField(max_length=10)

    def __str__(self):
        return str(self.ref)

    def written_by(self):
        return ','.join([str(p) for p in self.receiver_unit.all()])