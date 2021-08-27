from utils import TrackGV55
from datetime import datetime



# Caminho da base de dados
database = ".\position_db.xlsx"

# Define um intervalo para consulta do deslocamento
start = "2019/07/13 10:00:00"
stop  = "2019/07/13 11:00:00"



def main() -> None:
    # Inicia o objeto de interpretação dos dados
    tracker = TrackGV55(database)

    # Cria uma planilha com os dados tratados
    tracker.save_xls("output", "data")

    # Mostra os dados de velocidade média, máxima e deslocamento o intervalo
    print("Velocidade media: {:.2f}".format(tracker.avg_speed()))
    print("Velocidade maxima: {:.2f}".format(tracker.top_speed()))

    (mileage,interval) = tracker.mileage(start,stop)
    print("Deslocamento no intervalo de {} horas: {:.02f}".format(interval,mileage))
    
    # Imprime os graficos
    tracker.plot_graphics()



if __name__ == "__main__":
    main()