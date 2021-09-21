from hrd_kantor.models import Profile
from django.core.validators import RegexValidator
from django.db import models
# from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

NIK_VALIDATOR = RegexValidator("^\d{16}$",
                               "Format NIK Tidak Sesuai")
HP_VALIDATOR = RegexValidator(
    "^(08+[1-9])([0-9]{7,9})$", "Format NO HP TIDAK SESUA!!!")

NO_REK_VALIDATOR = RegexValidator("^\d{6,}$", "No Rekening Harus Berupa Angka")

EKSTENSI_VALIDATOR = RegexValidator(
    ".*\.(jpg|JPG|JPEG|pdf|PDF)", "Only Support PDF dan JPG")

STATUS = (
    ('MENIKAH','MENIKAH'),
    ('TIDAK MENIKAH', 'TIDAK MENIKAH'),
    ('CERAI HIDUP','CERAI HIDUP'),
    ('CERAI MATI', 'CERAI MATI'),
)

class NoKPJ(models.Model):
    no_kpj = models.CharField(max_length=11)
    tgl_keps = models.DateField()
    tgl_na = models.DateField(blank=True, null=True)
    is_aktif = models.BooleanField(default=True)

    class Meta:
        verbose_name = "DAFTAR KPJ"
        verbose_name_plural = "DAFTAR LIST KPJ"

    def __str__(self):
        return self.no_kpj

    def save(self, *args, **kwargs):
        if self.tgl_na:
            self.is_aktif = False
        super(NoKPJ, self).save(*args, **kwargs) 

class TenagaKerja(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    kpj = models.ForeignKey(NoKPJ, on_delete=models.CASCADE)
    alamat = models.CharField(max_length=250)
    nama_ibu = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS, max_length=13)
    nama_pasangan = models.CharField(max_length=50, blank=True, null=True)
    tgl_lahir_psg = models.DateField(blank=True, null=True)
    nama_anak_s = models.CharField(max_length=50, blank=True, null=True)
    tgl_lahir_s = models.DateField(blank=True, null=True)
    nama_anak_d = models.CharField(max_length=50, blank=True, null=True)
    tgl_lahir_d = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=100)
    no_rekening = models.CharField(max_length=25)
    nama_rekening = models.CharField(max_length=100)
    file_kk = models.FileField(upload_to='tenaga-kerja/kk/', validators=[EKSTENSI_VALIDATOR])
    file_ktp = models.FileField(upload_to='tenaga-kerja/ktp/', validators=[EKSTENSI_VALIDATOR])
    file_paklaring = models.FileField(upload_to='tenaga-kerja/paklaring/', validators=[EKSTENSI_VALIDATOR])
    file_lain = models.FileField(upload_to='tenaga-kerja/file-lain/', validators=[EKSTENSI_VALIDATOR])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "DATA TK"
        verbose_name_plural = "LIST DATA TK"

    def __str__(self):
        return '{} - {}'.format(self.profile.user.username, self.nama)
    

    