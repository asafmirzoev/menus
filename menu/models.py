from django.db import models



class Menu(models.Model):

    name = models.CharField('Название', max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Меню: {self.name}'
    
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Category(models.Model):

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, default=None, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, default=None, blank=True)
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return f'Категория: {self.name}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    