from flask import Flask, request, render_template, jsonify
from datetime import datetime as dt, timedelta
from linhas_sit import linhas
import logging

app = Flask(__name__, static_folder='static')

logging.basicConfig(level=logging.DEBUG)

def get_line(linha):
    for l in linhas:
        if l['linha'] == linha:
            return l
    return False

def generate_timetable_list(h_ini, h_fim, freq, ciclos):
    horarios = []
    if ciclos < 2: ciclos += 1
    for i in range(0, ciclos+1):
        if (h_ini + i*freq) <= h_fim:
            horarios.append((h_ini + i*freq).strftime('%H:%M'))
    return horarios

def seeyouspacecowboy(linha):
    timetables_list = [[[], []], [[], []], [[], []]]
    for n in range(0, len(linha['dias'])):
        if linha['frequencia'] and linha['frequencia'][0][0] != '':
            h_variaveis = len(linha['h_inicial'][n])
            for f in range(0, h_variaveis):
                h_ini = dt.strptime(linha['h_inicial'][n][f] + ':00', '%H:%M:%S')
                h_fim = dt.strptime(linha['h_final'][n][f] + ':00', '%H:%M:%S')
                if h_ini > h_fim: h_fim += timedelta(days=1)
                tempo_circulando = (h_fim - h_ini)
                freq = timedelta(minutes=float(linha['frequencia'][n][f].replace('min', '')))
                ciclos = int(tempo_circulando.total_seconds() / freq.total_seconds())
                horarios = generate_timetable_list(h_ini, h_fim, freq, ciclos)
                cache = timetables_list[n][0]
                for h in horarios:
                    if h not in cache:
                        timetables_list[n][0].append(h)
        if linha['frequencia_tc'] and linha['frequencia_tc'][0][0] != '':
            h_variaveis = len(linha['h_inicial_tc'][n])
            for f in range(0, h_variaveis):
                h_ini = dt.strptime(linha['h_inicial_tc'][n][f] + ':00', '%H:%M:%S')
                h_fim = dt.strptime(linha['h_final_tc'][n][f] + ':00', '%H:%M:%S')
                if h_ini > h_fim: h_fim += timedelta(days=1)
                tempo_circulando = (h_fim - h_ini)
                freq = timedelta(minutes=float(linha['frequencia_tc'][n][f].replace('min', '')))
                ciclos = int(tempo_circulando.total_seconds() / freq.total_seconds())
                horarios = generate_timetable_list(h_ini, h_fim, freq, ciclos)
                cache = timetables_list[n][1]
                for h in horarios:
                    if h not in cache:
                        timetables_list[n][1].append(h)
    return timetables_list

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_timetable', methods=['POST'])
def get_timetable():
    try:
        line = request.json.get('line').upper()
        logging.debug(f"Received line: {line}")
        line_data = get_line(line)
        if not line_data:
            return jsonify({"error": "Linha não encontrada."}), 404
        timetables = seeyouspacecowboy(line_data)
        return jsonify({"line": line_data['nome'], "timetables": timetables, "code": line})
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
