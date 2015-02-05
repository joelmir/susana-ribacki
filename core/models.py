# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Category(models.Model):
    """Categoria de produtos"""
    name = models.CharField(max_length=30, verbose_name='Nome da Categoria')
    ranking = models.IntegerField(verbose_name='Ordenação da exibição')
    active = models.BooleanField(verbose_name='Categoria ativa/inativa', default=True)

    class Meta:
        ordering = ["ranking", "name"]
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=500, verbose_name='Nome do produto')
    description = models.TextField(verbose_name='Descrição do produto', null=True, blank=True)
    size = models.CharField(max_length=200, verbose_name='Tamanhos do produto')
    price = models.CharField(max_length=200, verbose_name='Preço do produto')
    active = models.BooleanField(verbose_name='Produto ativo/inativo', default=True)
    ranking = models.IntegerField(verbose_name='Ordenação da exibição', default=0)
    categories = models.ManyToManyField(Category, verbose_name='Categorias que o produto faz parte')

    #Imagens do produto
    tumb = models.ImageField(upload_to = 'products/tumb/', default ='products/tumb/default.png')
    image = models.ImageField(upload_to = 'products/images/', default ='products/images/default.png')

    class Meta:
        ordering = ["ranking", "name"]
        verbose_name_plural = "Produtos"

    def __unicode__(self):
        return self.name

    def categories_str(self):
        return ' '.join(['category-{0}'.format(category.pk) for category in self.categories.all()])

    def is_featured(self):
        try:
            category = Category.objects.filter(active=True)[0]
        except IndexError:
            #Caso nenhuma categoria estiver ativa, exibe todos os produtos cadastrados
            return True
        return category in self.categories.all()

class Banner(models.Model):
    description = models.TextField(verbose_name='Descrição do banner', null=True, blank=True)
    ranking = models.IntegerField(verbose_name='Ordenação do banenr', default=0)
    image = models.ImageField(upload_to = 'banner/', default ='banner/default.png')
    active = models.BooleanField(verbose_name='Banner ativo/inativo', default=True)

    class Meta:
        ordering = ["ranking", "description"]
        verbose_name_plural = "Banners"

    def __unicode__(self):
        return u'{0}-{1}'.format(self.ranking, self.description )
