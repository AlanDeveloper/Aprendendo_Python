from datetime import datetime

def getData(dia, mes, ano):
    mydate = datetime(int(ano), int(mes), int(dia))
    print(mydate.strftime("%Y") + ',' + mydate.strftime("%d") + ' of ' + mydate.strftime("%B"))
    print(mydate.strftime("%d") + '/' + mydate.strftime("%m") + '/' + mydate.strftime("%Y"))
    print('Ano: ' + mydate.strftime("%Y") + ',dia: ' + mydate.strftime("%j"))

dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
getData(dia, mes, ano)