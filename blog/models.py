from django.db import models

# Create your models here.
class Post(models.Model):
    '''Данные о посте'''
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=100)
    models.DateField("Дата публикации", auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.title}, {self.author}'
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        