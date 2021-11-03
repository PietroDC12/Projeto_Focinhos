from django.db import models


class BuscaImagem(models.Model):

    imagem_busca = models.FileField(upload_to='imagem_busca')

    def _str_(self):
        return self.imagem_busca

    class Meta:
        verbose_name = 'Imagem_busca'