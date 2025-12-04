import datetime, calendar

agora = datetime.datetime.now()
print(agora)
ano = agora.year
mes = agora.month

calendario_mes = calendar.month(ano, mes)
print(calendario_mes)