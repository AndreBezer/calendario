import datetime, calendar

agora = datetime.datetime.now()
ano_atual = agora.year
mes_atual = agora.month
dia_atual = agora.day
print(f"calendario do mês {mes_atual} de {ano_atual}")

dias_com_estudo = []

def Calendario():
    for semana in calendar.monthcalendar(ano_atual, mes_atual):
            linha = ""
            for dia in semana:
                if dia == 0:
                    linha += "    "
                else:
                    data_dia = datetime.date(ano_atual, mes_atual, dia)
                    if data_dia.day in [int(dia) for dia in dias_com_estudo]:
                        linha += " ✅ "
                    elif data_dia.day == dia_atual:
                        linha += f"[{dia:2}]"
                    else:
                        linha += f" {dia:2} "
            print(linha)

def Menu():
    acao = int(input("""
[1] - entrar no calendario
[2] - adicionar dias estudados
"""))
    
    if acao == 1:
        Calendario()

    else:
        Calendario()
        dia_com_estudo = str(input("Quais os dias estudados? "))
        dia_com_estudo = dia_com_estudo.split()
        for dia in dia_com_estudo:
            dias_com_estudo.append(dia)

        print("Dias com esrudos: ")
        print(dias_com_estudo)
        

while True:    
    Menu()