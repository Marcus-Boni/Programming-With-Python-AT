from datetime import datetime

def obter_data_formatada():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")