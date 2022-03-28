import json


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


if __name__ == '__main__':
    # print(leer_archivo("farmers-protest-tweets-2021-03-5.json")[1])
    # print(mas_retweet("farmers-protest-tweets-2021-03-5.json"))
