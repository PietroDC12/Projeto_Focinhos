from django.db import models


class Info(models.Model):
    '''escolha_sexo = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    escolha_tamanho = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande')
    )'''

    cachorro_id = models.AutoField(primary_key=True)
    nome_cachorro = models.CharField(max_length=100)
    idade = models.CharField(max_length=2, blank=True)
    escolha_sexo = models.CharField(max_length=100, blank=True)
    tamanho_cachorro = models.CharField(max_length=100, blank=True)
    raca = models.CharField(max_length=50, blank=True)
    cor_pelagem = models.CharField(max_length=20, blank=True)
    info_cachorro = models.CharField(max_length=500, blank=True)
    nome_dono = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=75, blank=True)
    telefone = models.CharField(max_length=14, blank=True)
    imagem_focinho = models.FileField(blank=True)

    def __str__(self):
        return self.nome_cachorro

    class Meta:
        verbose_name = 'Ficha'
        verbose_name_plural = 'Fichas'