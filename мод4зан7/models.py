from django.db import models

# Create your models here.

class Advertisment(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField('название', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='отметьте, если торг возможен')
    created_at = models.DateTimeField(auto_now_add=True)
    undated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f"Advertisment(id={self.id}, title={self.title}, price={self.price})"

   
