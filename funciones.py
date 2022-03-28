import json
from leer_archivo import leer_archivo
from collections import namedtuple


def mas_retweet(archivo):

    lista = leer_archivo(archivo)
    top = list()
    for tweet in lista:
        retweets = tweet["retweetCount"]
        if len(top) < 10:
            top.append(tweet)
        else:
            minimo = min(top, key=lambda x: x['retweetCount'])
            if minimo['retweetCount'] < retweets:
                top.remove(minimo)
                top.append(tweet)
    return top


def usuarios_top(archivo):
    """El archivo no me carga en mi compu :(
    """
    Usuario = namedtuple("Usuario", ["nombre", "tweets"])
    lista = leer_archivo(archivo)
    nombres = set()
    usuarios = list()
    for tweet in lista:
        if tweet["user"]["username"] not in nombres:
            nombres.add(tweet["user"]["username"])

    for nombre in nombres:
        contador = 0
        for tweet in lista:
            if tweet["user"]["username"] == nombre:
                contador += 1
        usuarios.append(Usuario(nombre, contador))

    final = list()
    for _ in range(10):
        jugador = max(usuarios, key=lambda x: x.tweets)
        final.append(jugador)
        usuarios.remove(jugador)
    return final


if __name__ == '__main__':
    # print(leer_archivo("farmers-protest-tweets-2021-03-5.json")[1])
    # print(mas_retweet("farmers-protest-tweets-2021-03-5.json"))
    print(usuarios_top("farmers-protest-tweets-2021-03-5.json"))
