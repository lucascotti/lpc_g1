from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

class Evento(models.Model):
    nome=models.CharField('nome', max_length=150)
    evento_principal=models.CharField('evento principal', max_length=150)
    sigla=models.CharField('sigla')
    dataEHoraDeinicio= models.DateTimeField('data e hora inicio')
    palavraChave=models.CharField('palavra chave')
    logotipo=models.CharField('logo tipo')
    realizador_id=models.IntegerField()
    cidade=models.CharField('cidade')
    uf=models.CharField('uf')
    endereco=models.CharField('endreço')
    cep=models.CharField('cep')

class EvetoCientifico(Evento):
    issn=models.CharField('is sn ')

class Pessoa(models.Model):
    nome=models.CharField('nome', max_length=150)
    email=models.CharField('Email')

class PessoaFisica(Pessoa):
    cpf=models.CharField('CPF')

class PessoaJuridica(Pessoa):
    cnpj=models.CharField('CNPJ')
    razaoSocial=models.TextField('Razão Social')

class Autor(Pessoa) :
    curriculo=models.TextField('curriculo')
    artigos= ArrayField(ArrayField(models.CharField(max_length=50)))

class ArtigoCientifico(models.Model):
    titulo=models.CharField('titulo')
    autores=ArrayField(ArrayField(models.CharField(max_length=50)))
    evento_id=models.IntegerField()
