import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns



class TrackGV55:
    
    def __init__(self, db_path):
        """
        Inicia o objeto TrackGV55, carrega os dados em um dataframe e faz a decodificacao.

        Parameters:
            db_path (string): Caminho do arquivo com os dados.
        """
        
        # Carrega os dados em um dataframe e converte para bytes
        info_df = pd.read_excel(db_path)
        for raw in info_df.index:
            info_df["raw"][raw] = bytes.fromhex(info_df["raw"][raw])
        
        # Inicia novo dataframe para dados tratados
        location_cols = [
            "timestamp",                             # Timestamp
            "ignition", "battery", "extern_voltage",    # Informacoes eletricas
            "satellites", "accuracy",                   # Informacoes de rastreamento
            "speed", "mileage"                          # Informacoes de deslocamento
        ]
        self.location_df = pd.DataFrame(columns=location_cols)

        # Trata os dados e insere no dataframe
        for _ in reversed(range(0,len(info_df)-1)):
        #for _ in reversed(range(0,10)):
            # Prepara a lista
            info = []

            # Aquisita os dados crus
            report = info_df["raw"][_]
            
            # Trata os dados
            date = "{:04d}/{:02d}/{:02d}".format(report[49]*256+report[50],report[51],report[52])
            time = "{:02d}:{:02d}:{:02d}".format(report[53],report[54],report[55])
            timestamp = date + " " + time                                                               
            info.append(timestamp)                                  # Timestamp
            info.append(report[27])                                 # Estado da ignicao
            info.append(report[24])                                 # Tensao da bateria
            info.append(float(report[25]*256+report[26])/1000)      # Tensao externa
            info.append(report[30])                                 # Numero de satelites conectados
            info.append(report[33])                                 # Qualidade do sinal
            info.append(report[34]*256+report[35]+report[36]/10)    # Velocidade
            info.append(report[65]*256+report[66]+report[67]/10)    # Distancia total percorrida

            # Adiciona os dados tratados ao dataframe
            self.location_df.loc[_] = info



    def save_xls(self, name, sheetname):
        """
        Salva um documento .xlsx com nome de arquivo e de aba determinados.

        Parameters:
            name (string): Nome do arquivo.
            sheetname (string): Nome da aba. 
        """
        
        # Salva os dados em .xlsx
        self.location_df.to_excel(".\{0}.xlsx".format(name), sheet_name=sheetname)



    def avg_speed(self):
        """
        Retorna a velocidade media das medicoes realizadas.
        """

        # Calcula e retorna a velocidade media
        return self.location_df["speed"].mean()



    def mileage(self, start, stop):
        """
        Calcula o deslocamento total no intervalo dado.

        Parameters:
            start (string): Data e hora iniciais (YYYY/MM/DD HH:MM:SS).
            stop (string): Data e hora finais (YYYY/MM/DD HH:MM:SS).

        Returns
            (tuple): Distância percorrida em milhas e intervalo de deslocamento. 
        """

        # Define o formato de data e hora
        datetime_format = "%Y/%m/%d %H:%M:%S"
        
        # Converte as strings de data hora em objetos data hora
        start_time = datetime.strptime(start, datetime_format)
        stop_time = datetime.strptime(stop, datetime_format)

        # Inicia as listas
        miles = []
        #miles = 0
        interval = []

        # Vasse a lista dentro do intervalo desejado
        for _ in self.location_df.index:
            if datetime.strptime(self.location_df["timestamp"][_], datetime_format) >= start_time \
                and datetime.strptime(self.location_df["timestamp"][_], datetime_format) <= stop_time:

                # Acumula os valores
                miles.append(self.location_df["mileage"][_])
                #miles += self.location_df["mileage"][_]
                interval.append(self.location_df["timestamp"][_])
            
            # Sai do loop caso ultrapasse o intervalo desejado
            elif datetime.strptime(self.location_df["timestamp"][_], datetime_format) > stop_time:
                break

        # Calcula a diferença de tempo
        start_time = datetime.strptime(interval[0],  datetime_format)
        stop_time  = datetime.strptime(interval[-1], datetime_format)
        difference = stop_time - start_time

        
        # Retorna os resultados
        return (miles[-1] - miles[0], difference)
        #return (miles, difference)



    def top_speed(self):
        """
        Retorna a velocidade maxima registrada.

        Returns:
            (int): Velocidade máxima presente nos registros.
        """
        
        # Aquisita e retorna o valor maximo encontrado
        return self.location_df["speed"].max()



    def plot_graphics(self):
        """
        Plota os graficos a partir das informacoes do dataframe.
        """

        # Variaveis auxiliares
        data = self.location_df
        x = "timestamp"
        
        # Plota o grafico de velocidade e deslocamento
        ax = sns.lineplot(x=x,y="speed",data=data,color="g")
        ax2 = plt.twinx()
        sns.lineplot(x=x,y="mileage",data=data,color="b", ax=ax2)
        ax.xaxis.set_visible(False)
        plt.show()

        # Plota os graficos com as caracteristicas eletricas
        ax = sns.lineplot(x=x,y="battery",data=data,color="g")
        ax2 = plt.twinx()
        sns.lineplot(x=x,y="extern_voltage",data=data,color="b",ax=ax2)
        ax.xaxis.set_visible(False)
        plt.show()

        # Plota o grafico com o estado da ignicao
        ax = sns.lineplot(x=x,y="ignition",data=data)
        ax.xaxis.set_visible(False)
        plt.show()

        # Plota o grafico dos parametros de GPS
        ax = sns.lineplot(x=x,y="satellites",data=data,color="g")
        ax2 = plt.twinx()
        sns.lineplot(x=x,y="accuracy",data=data,color="b",ax=ax2)
        ax.xaxis.set_visible(False)
        plt.show()