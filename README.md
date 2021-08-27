# Problema 1

## Questões:

Através da análise dos pacotes, pode-se concluir:
* A velocidade média é 66.9 milhas por hora;
* A velocidade máxima é 97.1 milhas por hora;
* O deslocamento no intervalo de 10 a 11 horas é de 44.2 milhas;
* A velocidade máxima registrada, apesar de apresentar um valor aparentemente factível, parece ser uma dispersão. Para essa conclusão, pode-se analisar o gráfico de velocidade e desocamento (abaixo) e notar que no momento desse pico de velocidade não há uma variação condizente no deslocamento.
 
## Gráficos:
![Distância e velocidade](../images/spd_mil.png "Distância e velocidade")

![Estado da ignição](../images/ign.png "Ignição")

![Características elétricas](../images/bat_ext.png "Características elétricas")

![Informações de GPS](../images/sat_acc.png "Informações de GPS")

## Programa:

### Para executar o programa:
O script foi escrito com o auxílio de diversas bibliotecas do python, presentes no arquivo *requirements.txt*. Para efetuar a instalação das mesmas, pode-se usar o comando no prompt do Windows:
~~~
python -m pip install -r requitements.txt
~~~

Analogamente, se o sistema usado for Linux, pode-se usar o comando de terminal:
~~~
python3 -m pip install -r requirements.txt
~~~

Deve-se antes garantir que a máquina virtual python versão 3.6 ou superior esteja instalada no computador, assim como o gerenciador de pacotes pip.

O objeto *TrackGV55*, presente no módulo utils, apresenta as seguintes funcionalidades:
* *TrackGV55([caminho_do_arquivo])*: Inicia o objeto TrackGV55, carrega os dados em um dataframe e faz a decodificação.
* *TrackGV55.save_xls([nome_do_arquivo],[nome_da_planilha])*: Salva um documento .xlsx com nome de arquivo e de aba determinados.
* *TrackGV55.avg_speed()*: Retorna a velocidade média das medições realizadas.
* *TrackGV55.mileage([inicio],[final])*: Calcula o deslocamento total no intervalo dado.
* *TrackGV55.max_speed()*: Retorna a velocidade máxima registrada.
* *TrackGV55.plot_graphics()*: Plota os gráficos a partir das informações do dataframe.
  
O script *main.py* faz uma demonstração do uso do objeto. Para executá-lo no prompt de comando do Windows, deve-se digitar:
~~~
python main.py
~~~

E no terminal do Linux:
~~~
python3 main.py
~~~

## Tarefas e tempo de desenvolvimento:
* Abertura do arquivo *.xlsx* e conversão para dataframe: 1h30m
* Decodificação do pacote: 7h
* Salvamento do dataframe decodificado em um arquivo *.xlsx*: 1h
* Aquisição dos dados de velocidade: 30m
* Geração de gráficos: 3h 

## Observações:
*  Um arquivo contendo um script com a tarefa pronta foi recebido previamente ao início da mesma. Antes de dar início ao desenvolvimento, já havia sido feita uma análise razoável do código, o que pode ter causado um viés na elaboração dessas soluções. Foram feitas tentativas de uma construção diferente de soluções, mas principalmente no caso da decodificação dos dados, o método apresentado ficou muito parecido com o recebido previamente.