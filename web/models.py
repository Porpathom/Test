from django.db import models

# Create your models here.

class Cate(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Cate"
        verbose_name_plural = "Cates"

    def __str__(self):
        return self.name
   
    
class Subj(models.Model):

    subj_code = models.CharField(max_length=25)
    subj_name = models.CharField(max_length=255)
    credit = models.CharField(max_length=25)
    semester = models.CharField(max_length=25)
    year = models.CharField(max_length=25)
    cate =models.ForeignKey(Cate, on_delete=models.CASCADE,default=None)

    class Meta:
        verbose_name = "Subj"
        verbose_name_plural = "Subjs"

    def __str__(self):
        return self.subj_name

   