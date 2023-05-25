from django.db import models

class Post(models.Model):
    '''data about post'''
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('description')
    autor  = models.CharField('autor topic', max_length=100)
    date = models.DateField('date')

    def __str__(self) -> str:
        return f'{self.title}, {self.autor}'

    class Meta:
        verbose_name = 'record'
        verbose_name_plural = "records"


