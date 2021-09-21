import os
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

NIK_VALIDATOR = RegexValidator("^\d{16}$",
                               "Format NIK Tidak Sesuai")

def upload_name(instance, filename):
    if instance.is_hrd == True:
        return os.path.join('/media/HRD/%s/' % instance.user.username, filename)
    else:
        return os.path.join('/media/TK/%s' % instance.user.username, filename)

class Perusahaan(models.Model):
    nama = models.CharField(max_length=100)
    npp = models.CharField(max_length=8)

    class Meta:
        verbose_name_plural = "DAFTAR PERUSAHAAN"
    
    def __str__(self):
        return self.nama

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    nik = models.CharField(max_length=16, validators=[NIK_VALIDATOR])
    tgl_lahir = models.DateField()
    tempat_lahir = models.CharField(max_length=100)
    propic = models.FileField(upload_to=upload_name, blank=True, null=True)
    npp = models.ForeignKey(Perusahaan, on_delete=models.CASCADE)
    is_hrd = models.BooleanField(default=False)

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        a = self.user.username
        if a.find("HRD") >= 0 :
            self.is_hrd = True
        super(Profile, self).save(*args, **kwargs)