import datetime, calendar

agora = datetime.datetime.now()
ano_atual = agora.year
mes_atual = agora.month
dia_atual = agora.day
print(f"calendario do mês {mes_atual} de {ano_atual}")

for semana in calendar.monthcalendar(ano_atual, mes_atual):
    linha = ""
    for dia in semana:
        if dia == 0:
            linha += "    "
        else:
            data_dia = datetime.date(ano_atual, mes_atual, dia)
            if data_dia.day < dia_atual:
                linha += " ✅ "
            elif data_dia.day == dia_atual:
                linha += f"[{dia:2}]"
            else:
                linha += f" {dia:2} "
    print(linha)
