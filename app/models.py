from django.db import models

# Create your models here.
class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class ConnectionsMysql(Base):
    host = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    database = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'ConnectionMsql'
        verbose_name_plural = 'ConnectionsMsql'

    def __str__(self):
        return self.database

class UserMan(Base):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'UserMan'
        verbose_name_plural = 'UsersMan'

    def __str__(self):
        return self.database

class SelectedField(Base):
    name = models.CharField(max_length=50)
    nameBank = models.CharField(max_length=50, default='null')

    class Meta:
        verbose_name = 'SelectedField'
        verbose_name_plural = 'SelectedFields'

    def __str__(self):
        return self.name