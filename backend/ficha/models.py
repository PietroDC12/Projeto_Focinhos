from django.db import models


class Ficha(models.Model):
    escolha_sexo = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    escolha_tamanho = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande')
    )


    nome_cachorro: models.CharField(max_length=100)
    idade: models.CharField(max_length=2)
    sexo: models.CharField(max_length=1, choices=escolha_sexo)
    raca: models.CharField(max_length=50)
    cor_pelagem: models.CharField(max_length=20)
    tamanho: models.CharField(max_length=1, choices=escolha_tamanho)
    info_cachorro: models.CharField(max_length=500)
    nome_dono: models.CharField(max_length=100)
    endereco: models.CharField(max_length=200)
    email: models.EmailField(max_length=75)
    telefone: models.CharField(max_length=14)
    imagem_focinho: models.FileField()

    def __str__(self):
        return self.nome_cachorro

    class Meta:
        verbose_name = 'Ficha'
        verbose_name_plural = 'Fichas'

