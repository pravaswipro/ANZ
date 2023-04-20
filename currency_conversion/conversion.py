from math import *
import os
rate={'AUD':0.8371,'CAD':0.8711,'EUR':1.2315,'GBP':1.5683,'NZD':0.7750,
      'CNY':1/6.1715,'JPY':1/119.95,'CZK':0.0446,'DKK':0.1655,'NOK':0.1421,'USD':1}
def convert(input_currency,output_currency):
#    input_currency=input('From:')
#    output_currency=input('To:')
    input_list=input_currency.split()
    l1=input_list[0]
    l2=float(input_list[1])
    k=rate.keys()
    list=[]
    for i in k:
        list.append(i)
    if l1 not in list:
        print('Unable to find rate for',l1,'/',output_currency)
        os._exit(0)
    elif output_currency not in list:
        print('Unable to find rate for',l1,'/',output_currency)
        os._exit(0)
    CZK=rate['EUR']/rate['CZK']
    DKK=rate['EUR']/rate['DKK']
    NOK=rate['EUR']/rate['NOK']
    if output_currency=='CZK':
        result=l2*rate[l1]/CZK
    elif l1=='CZK':
        result=l2*CZK / rate[output_currency]
    elif output_currency=='DKK':
        result=l2*rate[l1]/DKK
    elif l1=='DKK':
        result=l2*DKK / rate[output_currency]
    elif output_currency=='NOK':
        result=l2*rate[l1]/NOK
    elif l1=='NOK':
        result=l2*NOK / rate[output_currency]
    result=l2*rate[l1] / rate[output_currency]
    if l1=='USD':
        rlt=1/rate[output_currency]
        result=str(output_currency)+' '+str("{:.2f}".format(l2*rlt))
    elif output_currency=='USD':
        result=str(output_currency)+' '+str("{:.2f}".format(l2*rate[l1]))
    elif output_currency=='AUD':
        result=str(output_currency)+' '+"{:.2f}".format(result)
    elif output_currency=='CAD':
        result=str(output_currency)+' '+"{:.2f}".format(result)
    elif output_currency=='CNY':
        result=str(output_currency)+' '+"{:.2f}".format(result)
    elif output_currency=='CZK':
        result=str(output_currency)+' '+"{:.2f}".format(result)
    elif output_currency=='DKK':
        result=str(output_currency)+' '+"{:.2f}".format(result)
    elif output_currency=='EUR':
        result=str(output_currency)+' '+"{:.2f}".format(result)
    elif output_currency=='GBP':
        result=str(output_currency)+' '+"{:.2f}".format(result)
    elif output_currency=='NOK':
        result=str(output_currency)+' '+"{:.2f}".format(result)
    elif output_currency=='NZD':
        result=str(output_currency)+' '+"{:.2f}".format(result)
    elif output_currency=='JPY':
        result=str(output_currency)+' '+str(floor(result))
    return result
#x=convert()
#print(x)
#input_currency,output_currency