# ULTIMA VERIFICAÇÃO: 23/3/2024
linhas = [
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        'linha': 'A11',
        'nome': 'Cavaleiros',
        'h_inicial_tc': [['06:00'], ['06:00'], ['06:00']],
        'h_final_tc': [['21:36'], ['21:36'], ['21:36']],
        'frequencia_tc': [['104min'], ['104min'], ['104min']],
        'h_inicial': [['06:52'], ['06:52'], ['06:52']],
        'h_final': [['22:28'], ['22:28'], ['22:28']],
        'frequencia': [['104min'], ['104min'], ['104min']],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        'linha': 'A11B',
        'nome': 'Cavaleiros',
        'h_inicial_tc': [['06:52'], ['06:52'], ['06:52']],
        'h_final_tc': [['22:28'], ['22:28'], ['22:28']],
        'frequencia_tc': [['104min'], ['104min'], ['104min']],
        'h_inicial': [['06:00'], ['06:00'], ['06:00']],
        'h_final': [['21:36'], ['21:36'], ['21:36']],
        'frequencia': [['104min'], ['104min'], ['104min']],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        'linha': 'A12',
        'nome': 'Parque Atlântico',
        'h_inicial_tc': [['05:54', '20:20'], ['05:50'], ['05:50']],
        'h_final_tc': [['20:20', '22:00'], ['21:40'], ['21:40']],
        'frequencia_tc': [['36min', '50min'], ['50min'], ['50min']],
        'h_inicial': [['05:00'], ['05:00'], ['05:00']],
        'h_final': [['20:36'], ['20:50'], ['20:50']],
        'frequencia': [['36min'], ['50min'], ['50min']],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        # imprime o 05:30 depois de 06:36 em h_inicial.
        # TODO soluc. possivel: acrescentar um sort na lista de horários em sitcalc
        'linha': 'A13',
        'nome': 'Horto',
        'h_inicial_tc': [['04:30', '07:18', '22:00', '22:40', '23:10'], ['05:00', '23:00'], ['05:00', '23:00']],
        'h_final_tc': [['07:18', '22:00', '22:40', '23:10', '00:00'], ['23:00', '00:00'], ['23:00', '00:00']],
        'frequencia_tc': [['28min', '21min', '40min', '30min', '40min'], ['40min', '60min'], ['40min', '60min']],
        'h_inicial': [['05:12', '05:30', '06:57', '22:42', '23:15'], ['05:40'], ['05:40']],
        'h_final': [['06:57', '05:30', '22:42', '23:15', '23:30'], ['23:00'], ['23:00']],
        'frequencia': [['28min', '1min', '21min', '33min', '15min'], ['40min'], ['40min']],
        'dias': ['Dias úteis', 'Sábado', 'Domingo']
    },
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        'linha': 'A13C',
        'nome': 'Horto (Circular)',
        'h_inicial_tc': [['06:00'], ['06:00'], ['06:00']],
        'h_final_tc': [['22:48'], ['22:48'], ['22:48']],
        'frequencia_tc': [['84min'], ['84min'], ['84min']],
        'h_inicial': [['Circular'], ['Circular'], ['Circular']],
        'h_final': [['Circular'], ['Circular'], ['Circular']],
        'frequencia': [[''], [''], ['']],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        'linha': 'A21',
        'nome': 'Vila Moreira',
        'h_inicial_tc': [['06:20', '20:20'], ['06:20'], ['06:20']],
        'h_final_tc': [['20:20', '21:40'], ['21:00'], ['21:00']],
        'frequencia_tc': [['40min', '80min'], ['80min'], ['40min']],
        'h_inicial': [['05:40', '19:40'], ['05:40'], ['05:40']],
        'h_final': [['19:40', '21:00'], ['20:20'], ['20:20']],
        'frequencia': [['40min', '80min'], ['80min'], ['80min']],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        'linha': 'A22A',
        'nome': 'Verdes Mares',
        'h_inicial_tc': [
            ['05:45', '08:09', '16:35', '20:48', '22:44', '23:20'],
            ['05:42', '15:40', '23:00'],
            ['05:40', '23:00']
        ],
        'h_final_tc': [
            ['08:09', '16:35', '20:48', '22:44', '23:20', '00:00'],
            ['15:40', '23:00', '00:00'],
            ['23:00', '00:00']
        ],
        'frequencia_tc': [
            ['18min', '22min', '18min', '22min', '36min', '40min'],
            ['28min', '40min', '60min'],
            ['40min', '60min']
        ],
        'h_inicial': [
            ['05:00', '08:36', '17:20', '19:48', '22:00'],
            ['05:00', '14:20'],
            ['05:00']
        ],
        'h_final': [
            ['08:36', '17:20', '19:48', '22:00', '23:00'],
            ['14:20', '23:00'],
            ['23:00']
        ],
        'frequencia': [
            ['18min', '22min', '18min', '22min', '30min'],
            ['28min', '40min'],
            ['40min']
        ],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {
        'linha': 'A22B',
        'nome': 'Bosque Azul',
        'h_inicial': [
            ['05:09', '09:04', '16:48', '19:17', '21:49', '22:15'],
            ['05:14', '14:40'],
            ['05:20']
        ],
        'h_final': [
            ['09:04', '16:48', '19:17', '21:49', '22:15', '22:45'],
            ['14:40', '22:00'],
            ['22:00']
        ],
        'frequencia': [
            ['18min', '22min', '18min', '22min', '26min', '30min'],
            ['28min', '40min'],
            ['40min']
        ],
        'h_inicial_tc': [
            ['05:54', '08:18', '16:44', '20:38', '23:00'],
            ['05:56', '16:00'],
            ['06:00']
        ],
        'h_final_tc': [
            ['08:18', '16:44', '20:38', '23:00', '23:30'],
            ['16:00', '22:40'],
            ['22:40']
        ],
        'frequencia_tc': [
            ['18min', '22min', '18min', '22min', '30min'],
            ['28min', '40min'],
            ['40min']
        ],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {
        'linha': 'A23',
        'nome': 'Virgem Santa',
        'h_inicial': [
            ['05:00'],
            ['05:00'],
            ['05:00']
        ],
        'h_final': [
            ['23:00'],
            ['23:00'],
            ['23:00']
        ],
        'frequencia': [
            ['20min'],
            ['30min'],
            ['60min']
        ],
        'h_inicial_tc': [
            ['06:00', '23:30'],
            ['06:00'],
            ['06:00']
        ],
        'h_final_tc': [
            ['23:30', '00:00'],
            ['00:00'],
            ['00:00']
        ],
        'frequencia_tc': [
            ['20min', '30min'],
            ['30min'],
            ['60min']
        ],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        'linha': 'A31',
        'nome': 'Vila Moreira',
        'h_inicial_tc': [
            ['05:15', '16:45', '17:18', '19:42', '20:15', '23:15'],
            ['05:40', '20:20', '22:00'],
            ['05:40', '23:00']
        ],
        'h_final_tc': [
            ['16:45', '17:18', '19:42', '20:15', '23:15', '00:00'],
            ['20:20', '22:00', '00:00'],
            ['23:00', '00:00']
        ],
        'frequencia_tc': [
            ['30min', '33min', '36min', '33min', '30min', '45min'],
            ['80min', '100min', '120min'],
            ['80min', '60min']
        ],
        'h_inicial': [
            ['06:00', '17:00', '20:00'],
            ['06:20', '21:00'],
            ['06:20', '22:20']
        ],
        'h_final': [
            ['17:00', '20:00', '23:30'],
            ['21:00', '22:40'],
            ['22:20', '23:20']
        ],
        'frequencia': [
            ['30min', '36min', '30min'],
            ['80min', '100min'],
            ['80min', '70min']
        ],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {
        'linha': 'A32F',
        'nome': 'Fronteira',
        'h_inicial': [['06:20', '13:30', '19:30']],
        'h_final': [['13:30', '19:30', '20:15']],
        'frequencia': [['40min', '60min', '45min']],
        'h_inicial_tc': [['Circular']],
        'h_final_tc': [['Circular']],
        'frequencia_tc': [['']],
        'dias': ['Dias Úteis']
    },
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        'linha': 'A33',
        'nome': 'Novo Hospital',
        'h_inicial_tc': [['05:20'], ['06:40'], ['06:40']],
        'h_final_tc': [['22:40'], ['21:20'], ['21:20']],
        'frequencia_tc': [['40min'], ['80min'], ['80min']],
        'h_inicial': [['05:20'], ['06:00'], ['06:00']],
        'h_final': [['22:40'], ['20:40'], ['20:40']],
        'frequencia': [['40min'], ['80min'], ['80min']],
        'dias': ['Dias úteis', 'Sábado', 'Domingo']
    },
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        'linha': 'A41',
        'nome': 'Nova Macaé',
        'h_inicial_tc': [['06:30'], ['06:30'], ['06:30']],
        'h_final_tc': [['21:10'], ['20:30'], ['20:30']],
        'frequencia_tc': [['20min'], ['60min'], ['60min']],
        'h_inicial': [['05:00'], ['06:00'], ['06:00']],
        'h_final': [['20:40'], ['21:00'], ['21:00']],
        'frequencia': [['20min'], ['60min'], ['60min']],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {
        'linha': 'A51',
        'nome': 'Vale das Palmeiras',
        'h_inicial_tc': [['05:50', '08:40', '16:10', '19:00'], ['06:00'], ['06:00']],
        'h_final_tc': [['08:40', '16:10', '19:00', '21:40'], ['19:20'], ['19:20']],
        'frequencia_tc': [['34min', '50min', '34min', '34min'], ['100min'], ['100min']],
        'h_inicial': [['05:50', '06:41', '09:30', '17:00', '19:50'], ['06:50'], ['06:50']],
        'h_final': [['06:41', '09:30', '17:00', '19:50', '22:30'], ['20:10'], ['20:10']],
        'frequencia': [['51min', '34min', '50min', '34min', '34min'], ['100min'], ['100min']],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {
        'linha': 'A52',
        'nome': 'Nova Holanda',
        'h_inicial_tc': [['05:30', '07:40', '21:00'], ['06:30', '21:00'], ['06:30', '21:00']],
        'h_final_tc': [['07:40', '21:00', '23:30'], ['21:00', '23:30'], ['21:00', '23:30']],
        'frequencia_tc': [['20min', '18min', '30min'], ['30min', '60min'], ['30min', '60min']],
        'h_inicial': [['Circular'], ['Circular'], ['Circular']],
        'h_final': [['Circular'], ['Circular'], ['Circular']],
        'frequencia': [[''], [''], ['']],
        'dias': ['Dias Úteis', 'Sábados', 'Domingo']
    },
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        'linha': 'A73',
        'nome': 'Engenho da Praia',
        'h_inicial_tc': [['06:10', '06:48', '07:14', '19:30', '20:50', '21:40'], ['07:15'], ['07:15']],
        'h_final_tc': [['06:48', '07:14', '19:30', '20:50', '21:40', '22:20'], ['20:45'], ['20:45']],
        'frequencia_tc': [['38min', '26min', '32min', '40min', '50min', '40min'], ['90min'], ['90min']],
        'h_inicial': [['05:22', '06:00', '06:26', '19:14', '20:00'], ['06:30'], ['06:30']],
        'h_final': [['06:00', '06:26', '19:14', '20:00', '21:20'], ['20:00'], ['20:00']],
        'frequencia': [['38min', '26min', '32min', '46min', '40min'], ['90min'], ['90min']],
        'dias': ['Dias úteis', 'Sábado', 'Domingo']
    },
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        'linha': 'A73R',
        'nome': 'Engenho da Praia (Rápido)',
        'h_inicial_tc': [['06:31', '21:05', '22:00'], ['06:30'], ['06:30']],
        'h_final_tc': [['21:05', '22:00', '23:00'], ['20:00'], ['20:00']],
        'frequencia_tc': [['46min', '55min', '60min'], ['90min'], ['90min']],
        'h_inicial': [['05:45'], ['05:45'], ['05:45']],
        'h_final': [['21:51'], ['19:15'], ['19:15']],
        'frequencia': [['46min'], ['90min'], ['90min']],
        'dias': ['Dias úteis', 'Sábado', 'Domingo']
    },
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        'linha': 'C41A',
        'nome': 'Bairro da Glória',
        'h_inicial_tc': [['05:00'], ['05:00'], ['05:00']],
        'h_final_tc': [['22:24'], ['00:00'], ['00:00']],
        'frequencia_tc': [['36min'], ['60min'], ['60min']],
        'h_inicial': [['Circular'], ['Circular'], ['Circular']],
        'h_final': [['Circular'], ['Circular'], ['Circular']],
        'frequencia': [[''], [''], ['']],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {  # ULTIMA VERIFICAÇÃO: 23/3/2024
        'linha': 'C41B',
        'nome': 'Bairro da Glória',
        'h_inicial_tc': [['05:18', '22:42', '23:30'], ['05:30'], ['05:30']],
        'h_final_tc': [['22:42', '23:30', '00:00'], ['22:30'], ['22:30']],
        'frequencia_tc': [['36min', '48min', '30min'], ['60min'], ['60min']],
        'h_inicial': [['Circular'], ['Circular'], ['Circular']],
        'h_final': [['Circular'], ['Circular'], ['Circular']],
        'frequencia': [[''], [''], ['']],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {
        "linha": "S13",
        "nome": "Frade",
        "h_inicial_tc": [
            ["05:40", "06:00", "16:30", "18:30", "20:00", "22:00", "22:45"],
            ["06:06", "07:10", "11:30", "16:50", "18:10", "21:30", "22:30"],
            ["05:15", "06:00", "20:00", "20:40", "21:40", "22:30"]
        ],
        "h_final_tc": [
            ["06:00", "16:30", "18:30", "20:00", "22:00", "22:45", "23:45"],
            ["07:10", "11:30", "16:50", "18:10", "21:30", "22:30", "23:45"],
            ["06:00", "20:00", "20:40", "21:40", "22:30", "23:45"]
        ],
        "frequencia_tc": [
            ["20min", "30min", "10min", "15min", "30min", "45min", "60min"],
            ["16min", "20min", "25min", "35min", "40min", "60min", "75min"],
            ["45min", "30min", "40min", "60min", "50min", "75min"]
        ],
        "h_inicial": [
            ["04:00", "04:30", "05:00", "07:30", "19:00", "20:00", "20:30","21:20"],
            ["04:40", "08:40", "09:50", "15:40", "19:00", "20:20"],
            ["05:00", "18:00", "19:20", "19:40", "20:40", "21:00"]
        ],
        "h_final": [
            ["04:30", "05:00", "07:30", "19:00", "20:00", "20:30", "21:30", "22:20"],
            ["08:40", "09:50", "15:40", "19:00", "20:20", "22:20"],
            ["18:00", "19:20", "19:40", "20:40", "21:00", "22:20"]
        ],
        "frequencia": [
            ["30min", "15min", "10min", "30min", "10min", "30min", "50min", "60min"],
            ["16min", "20min", "25min", "35min", "40min", "60min"],
            ["30min", "40min", "20min", "30min", "20min", "40min"]
        ],
        "dias": ["Dias Úteis", "Sábado", "Domingo e Feriado"]
    },

    {
        "linha": "T22",
        "nome": "Ajuda",
        "h_inicial_tc": [
            ["05:06", "07:42", "16:08", "20:15", "22:34", "23:30", "23:35"],
            ["05:45", "15:10"],
            ["05:40", "23:00"]
        ],
        "h_final_tc": [
            ["07:42", "16:08", "20:15", "22:34", "23:00", "23:35", "00:00"],
            ["15:10", "00:00"],
            ["23:00", "00:00"]
        ],
        "frequencia_tc": [
            ["13min", "23min", "13min", "23min", "26min", "35min", "25min"],
            ["18min", "44min"],
            ["40min", "60min"]
        ],
        "h_inicial": [
            ["04:20", "08:27", "16:54", "19:30", "21:48", "22:30", "22:50"],
            ["05:00", "13:42"],
            ["05:00"]
        ],
        "h_final": [
            ["08:27", "16:54", "19:30", "21:48", "22:30", "22:50", "23:20"],
            ["13:42", "23:15"],
            ["23:00"]
        ],
        "frequencia": [
            ["13min", "23min", "13min", "23min", "42min", "20min", "30min"],
            ["18min", "44min"],
            ["40min"]
        ],
        "dias": ["Dias Úteis", "Sábado", "Domingo"]
    },
    {
        "linha": "T31A",
        "nome": "Lagoa",
        "h_inicial_tc": [
            ["05:45", "08:30", "16:10", "19:55"],
            ["05:45"],
            ["05:45"]
        ],
        "h_final_tc": [
            ["08:30", "16:10", "19:55", "20:35"],
            ["20:15"],
            ["20:15"]
        ],
        "frequencia_tc": [
            ["15min", "20min", "15min", "20min"],
            ["30min"],
            ["30min"]
        ],
        "h_inicial": [
            ["Circular"],
            ["Circular"],
            ["Circular"]
        ],
        "h_final": [
            ["Circular"],
            ["Circular"],
            ["Circular"]
        ],
        "frequencia": [
            [""],
            [""],
            [""]
        ],
        "dias": ["Dias Úteis", "Sábado", "Domingo"]
    },
    {
        'linha': 'T31B',
        'nome': 'Mirante da Lagoa',
        'h_inicial_tc': [['05:30'], ['05:30'], ['05:30']],
        'h_final_tc': [['22:30'], ['20:00'], ['20:00']],
        'frequencia_tc': [['20min'], ['30min'], ['30min']],
        'h_inicial': [['Circular'], ['Circular'], ['Circular']],
        'h_final': [['Circular'], ['Circular'], ['Circular']],
        'frequencia': [[''], [''], ['']],
        'dias': ['Dias Úteis', 'Sábado', 'Domingo']
    },
    {
        "linha": "T51",
        "nome": "Terminal P. Tubos",
        "h_inicial_tc": [["05:00", "08:50", "17:05", "19:10", "21:40", "22:00"], ["05:00", "14:00", "23:20"], ["05:00", "15:12", "23:26"]],
        "h_final_tc": [["08:50", "17:05", "19:10", "21:40", "22:00", "00:00"], ["14:00", "23:20", "00:00"], ["15:12", "23:26", "00:00"]],
        "frequencia_tc": [["10min", "15min", "10min", "15min", "20min", "30min"], ["15min", "20min", "40min"], ["36min", "26min", "34min"]],
        "h_inicial": [["06:00", "07:50", "16:05", "19:55", "22:40", "23:00"], ["06:00", "15:00"], ["05:54", "16:06", "16:30", "23:26"]],
        "h_final": [["07:50", "16:05", "19:55", "22:40", "23:00", "00:00"], ["15:00", "00:00"], ["16:06", "16:30", "23:26", "00:00"]],
        "frequencia": [["10min", "15min", "10min", "15min", "20min", "30min"], ["15min", "20min"], ["36min", "24min", "26min", "34min"]],
        "dias": ["Dias Úteis", "Sábado", "Domingo"]
    },
    {
        "linha": "T61",
        "nome": "Cavaleiros Firmas",
        "h_inicial_tc": [["06:00"], ["06:10"], ["14:10"]],
        "h_final_tc": [["22:24"], ["22:10"], ["21:10"]],
        "frequencia_tc": [["24min"], ["60min"], ["60min"]],
        "h_inicial": [["Circular"], ["Circular"], ["Circular"]],
        "h_final": [["Circular"], ["Circular"], ["Circular"]],
        "frequencia": [[""], [""], [""]],
        "dias": ["Dias Úteis", "Sábado", "Domingo"]
    },
    {
        "linha": "T111W1",
        "nome": "Lagomar (Via W1)",
        "h_inicial_tc": [["06:15"], ["07:00"]],
        "h_final_tc": [["22:00"], ["22:00"]],
        "frequencia_tc": [["45min"], ["90min"]],
        "h_inicial": [["05:30"], ["06:15"]],
        "h_final": [["21:15"], ["21:15"]],
        "frequencia": [["45min"], ["90min"]],
        "dias": ["Dias Úteis", "Sábado"]
    },
    {
        "linha": "T111",
        "nome": "Lagomar (UPA)",
        "h_inicial_tc": [["16:00"]],
        "h_final_tc": [["20:35"]],
        "frequencia_tc": [["25min"]],
        "h_inicial": [["06:00"]],
        "h_final": [["09:20"]],
        "frequencia": [["25min"]],
        "dias": ["Dias Úteis"]
    },

]
