from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def inicio(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/evento'>Evento</a></li>
                    <li><a href='/evetoCientifico'>Eveto Cientifico</a></li>
                    <li><a href='/pessoa'>Pessoa</a></li>
                    <li><a href='/pessoafisica'>Pessoa Fisica</a></li>
                    <li><a href='/pessoajuridica'>Pessoa Juridica</a></li>
                    <li><a href='/autor'>Autor</a></li>
                    <li><a href='/artigoCientifico'>Artigo Cientifico</a></li>
                </ul>
            """
    return HttpResponse(html)

def evento(request):
    lista_eventos = Evento.objects.all()
    retorno = ""
    for e in lista_eventos:
        retorn+='<li>'+'nome'+e.nome+'evento principal'+e.evento_principal+'sigla'+e.sigla+'nome'+str(e.dataEHoraDeinicio)+'palavrsChave'+e.palavrsChave+'logo tipo'+e.logotipo+'realizador'+str(e.realizador_id)+'cidade'+e.cidade+'uf'+e.uf+'endereco'+e.endereco+'CEP'+e.cep+ '</li>'

    return HttpResponse(""+retorno)
def eventoCientifico(request):
    html = "<h1>evento Cientifico</h1>"
    lista = EvetoCientifico.objects.all()
    for tipo in lista:
        html += '<li>{}</li>'.format(tipo.issn)
    return HttpResponse(html)
def pessoa(request):
    lista_pessoa=Pessoa.objects.all()
    retorno = ""
    for p in lista_pessoa:
        retorno='<li>'+'nome'+p.nome+'email'+p.email+'</li>'

    return HttpResponse(""+retorno)
def pessoaFisica(request):
    html = "<h1>Pessoa Fisica</h1>"
    lista = PessoaFisica.objects.all()
    for tipo in lista:
        html += '<li>{}</li>'.format(tipo.cpf)
    return HttpResponse(html)
def pessoaJuridica(request):
    html = "<h1>Pessoa Juridica</h1>"
    lista = PessoaJuridica.objects.all()
    for tipo in lista:
        html += '<li>{}</li>'.format(tipo.cnpj)
    return HttpResponse(html)
def autor(request):
    html = "<h1>Autor</h1>"
    lista = Autor.objects.all()
    for tipo in lista:
        html += '<li>{}</li>'.format(tipo.curriculo)
    return HttpResponse(html)
def artigoCientifico(request):
    lista_artigo=ArtigoCientifico.objects.all()
    retorno = ""
    for a in lista_artigo:
        retorno+='<li>'+'titulo'+a.titulo+'autores'+a.autores+'evento_id'+str(a.evento_id)+'</li>'

    return HttpResponse(""+retorno)

def academico(request):
    inscrito=PessoaFisica.objects.all()
    participantes=Evento.objects.all()
