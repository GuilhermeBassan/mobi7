# Problema 1

## Questões:

Através da análise dos pacotes, pode-se concluir:
* A velocidade média é 66.9 milhas por hora;
* A velocidade máxima é 97.1 milhas por hora;
* O deslocamento no intervalo de 10 a 11 horas é de 44.2 milhas;
* A velocidade máxima registrada, apesar de apresentar um valor aparentemente factível, parece ser uma dispersão. Para essa conclusão, pode-se analisar o gráfico de velocidade e deslocamento (abaixo) e notar que no momento desse pico de velocidade não há uma variação condizente no deslocamento.
 
## Gráficos:
![Distância e velocidade](https://github.com/GuilhermeBassan/mobi7/blob/main/images/spd_mil.png "Distância e velocidade")

![Estado da ignição](https://github.com/GuilhermeBassan/mobi7/blob/main/images/ign.png "Ignição")

![Características elétricas](https://github.com/GuilhermeBassan/mobi7/blob/main/images/bat_ext.png "Características elétricas")

![Informações de GPS](https://github.com/GuilhermeBassan/mobi7/blob/main/images/sat_acc.png "Informações de GPS")

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

# Problema 2

Processo de validação de equipamento instalado.

## Variáveis a observar para garantir a instalação correta dos pontos elétricos:
* Antes de qualquer verificação, deve-se prestar muita atenção na polaridade da tensão da bateria quando a mesma estiver sendo instalada. Caso o equipamento não possua proteção, uma inversão de polaridade pode causar danos e possivelmente irá estragar o dispositivo;
* Estando a polaridade instalada de forma correta, o atendente pode requisitar os dados do dispositivo para confrontá-los com os dados reais:
  * Fazer a requisição dos dados com a ignição desligada, e após isso ligada, e verificar os dados recebidos;
  * Verificar a tensão externa indicada na requisição e compará-la com a tensão real;
  * Verificar o nível de bateria indicado na requisição e compará-lo com o nível real.
* Se algum dos dados apresentar inconsistências, deve-se verificar as conexões.
  
## Verificação do estado de bloqueio:
* Antes da verificação, ligar o veículo para conferir se o mesmo está funcionando corretamente;
* Então, enviar o comando de bloqueio e observar se o mesmo irá causar o desligamento do motor;
* Caso não aconteça, checar as conexões elétricas e averiguar se o rele que realiza o desligamento da bomba de combustível está funcionando e está ligado corretamente - pode-se usar um multímetro e testar a continuidade do rele com o bloqueio acionado (não deve apresentar continuidade) ou desacionado (deve apresentar continuidade).

## Qualidade de sinal do GPS:
* Se possível, fazer o teste em local aberto;
* Após posicionar o dispositivo no local recomendado, verificar os dados de número de satélites conectados e qualidade de sinal;
* Se esses dados não forem compatíveis com os padrões sugeridos pela fabricante, ou então os patamares estabelecidos pela empresa, verificar possíveis obstruções no ambiente (edifícios, galpões, etc), que possam estar prejudicando a comunicação;
* Ao confirmar que o problema de recepção não é do ambiente, então pode-se tentar reposicionar a antena para melhor qualidade - lembrando que a melhor posição é, geralmente, na parte de cima com visada para o céu.