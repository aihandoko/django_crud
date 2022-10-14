from django.db import models

# Create your models here.
class Post(models.Model):
    judul = models.CharField(max_length=255)
    sinopsis = models.TextField()
    created_at = models.DateTimeField( auto_now_add = True)

    class Meta:  
        db_table = "buku_sinopsis"

        