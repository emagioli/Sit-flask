from datetime import datetime as dt
from datetime import timedelta

from linhas_sit import linhas

# retorna o objeto {} da linha correspondente, ou False caso não encontrada
def get_line(linha):
    for l in linhas:
        if l['linha'] == linha:
            return l
    return False

# retorna lista de linhas. Ex.: ['A33','A45']
def get_lines_list():
    lines = []
    for l in linhas:
        lines.append(l['linha'])
    return lines

# retorna string com as linhas (formato: A33 - NOVO HOSPITAL)
def print_lines_list():
    s = ""
    for l in linhas:
        s = s + f"{l['linha']} - {l['nome']}\n"
    return s

# retorna a string com a tabela de horários
def generate_timetable_list(h_ini, h_fim, freq, ciclos):
    horarios = []
    if(ciclos < 2): ciclos +=1
    for i in range(0, ciclos+1):
        if (h_ini + i*freq) <= h_fim:
            horarios.append((h_ini + i*freq).strftime('%H:%M'))
    return horarios

# retorna uma lista, onde os elementos são listas com os horários calculados
def seeyouspacecowboy(linha):
    timetables_list = [
        [[],[]],
        [[],[]],
        [[],[]],
    ]
    for n in range(0, len(linha['dias'])):
        if (linha['frequencia'] and linha['frequencia'][0][0]!=''):
            h_variaveis = len(linha['h_inicial'][n])
            for f in range(0, h_variaveis):
                h_ini = dt.strptime(linha['h_inicial'][n][f] + ':00', '%H:%M:%S')
                h_fim = dt.strptime(linha['h_final'][n][f] + ':00', '%H:%M:%S')
                if(h_ini > h_fim): h_fim += timedelta(days=1)
                tempo_circulando = (h_fim - h_ini)
                freq = timedelta(minutes=float(
                    linha['frequencia'][n][f].replace('min', '')))
                ciclos = int(tempo_circulando.total_seconds() / freq.total_seconds())
                horarios = generate_timetable_list(h_ini, h_fim, freq, ciclos)
                cache = timetables_list[n][0]
                for h in horarios:
                    if h not in cache:
                        timetables_list[n][0].append(h)

        if (linha['frequencia_tc'] and linha['frequencia_tc'][0][0]!=''):
            h_variaveis = len(linha['h_inicial_tc'][n])
            for f in range(0,h_variaveis):
                h_ini = dt.strptime(linha['h_inicial_tc'][n][f] + ':00', '%H:%M:%S')
                h_fim = dt.strptime(linha['h_final_tc'][n][f] + ':00', '%H:%M:%S')
                if(h_ini > h_fim): h_fim += timedelta(days=1)
                tempo_circulando = (h_fim - h_ini)
                freq = timedelta(minutes=float(linha['frequencia_tc'][n][f].replace('min', '')))
                ciclos = int(tempo_circulando.total_seconds() / freq.total_seconds())
                horarios = generate_timetable_list(h_ini, h_fim, freq, ciclos)
                cache = timetables_list[n][1]
                for h in horarios:
                    if h not in cache:
                        timetables_list[n][1].append(h)

    return timetables_list

def generate_timetable_string(linha):
    string = ''
    timetables_list = seeyouspacecowboy(linha)
    string += f'    Linha: {linha["nome"]} ({linha["linha"]})\n'
    for n in range(len(timetables_list)):
        if(n<len(linha["dias"])): # 3: seg-sex / sab / dom
            string += '\n' + '--'*5 + f'    {linha["dias"][n]}    ' + '--'*5 + '\n\n'
            for l in range(len(timetables_list[n])): # 2: saida xxx | saida terminal
                if(len(timetables_list[n][l]) > 0):
                    string += f'Saída {linha["nome"] if l==0 else "Terminal Central"}:\n\n'
                    for i in range(len(timetables_list[n][l])): # qtd de horarios
                        string += timetables_list[n][l][i]
                        string += '\n' if ((i+1)%4==0) else '\t'
                    string += '\n'
                    string += '\n' + '--'*10 + '\n\n'
    string += '\n'

    return string
#

# teste = 'S13'
# for l in linhas:
#     if (l['linha'] == teste):
#         print(generate_timetable_string(l))
#         break