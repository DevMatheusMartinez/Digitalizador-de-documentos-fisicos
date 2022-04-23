from django.db import models

# Create your models here.
#mudar isso
class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class SelectedField(Base):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'SelectedField'
        verbose_name_plural = 'SelectedFields'

    def __str__(self):
        return self.name