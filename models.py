from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.

class Advertisment(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField('название', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='отметьте, если торг возможен')
    created_at = models.DateTimeField(auto_now_add=True)
    undated_at = models.DateTimeField(auto_now=True)


    @admin.display(description='дата совпадает')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; forn-wieght: bold;"> Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='время совпадает')
    def undated_time(self):
        from django.utils import timezone
        if self.undated_at.date() == timezone.now().date():
            undated_tm = self.undated_at.time().strftime('%H:%M:%S')
            return format_html(
                    '<span style="color: blue; forn-wieght: bold;"> Сегодня в {}</span>', undated_tm
                )
        return self.undated_at.strftime("%d.%m.%Y в %H:%M:%S")

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f"Advertisment(id={self.id}, title={self.title}, price={self.price})"

   
