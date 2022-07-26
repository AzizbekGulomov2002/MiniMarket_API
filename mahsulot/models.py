from django.db import models

class Menyu(models.Model):
    nomi = models.CharField(max_length=200, help_text='Menyu turini kiriting...')
    
    def __str__(self):
        return self.nomi
    
    class Meta:
        verbose_name = 'Menyu'
        verbose_name_plural = 'Menyular'
        
    

class Mahsulot(models.Model):
    turi = models.ForeignKey(Menyu, on_delete=models.CASCADE, help_text='Mahsulot turini kiriting...')
    nomi = models.CharField(max_length=200, help_text='Mahsulot nomini kiriting...')
    mahsulot_haqida = models.TextField(help_text="Mahsulot haqida ma'lumot kiriting...")
    rasm = models.FileField(upload_to='mahsulot/rasm',help_text="Mahsulot rasmini kiriting...")
    narx = models.IntegerField(help_text="Mahsulot narxini kiriting...")
    
    def __str__(self):
        return self.nomi
    
    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'
        

    
    
    
    
