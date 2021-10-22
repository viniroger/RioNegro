# Gráfico de cotas/nível do Rio Negro

O histórico dos valores de cotas (em metros) do Rio Negro entre 2000 e 2021
(até 20 de outubro) estão disponíveis no arquivo 'cotas_RioNegro.csv'.

O script 'plot_ts.py' faz o gráfico das séries dentro do período especificado
nas variáveis 'start_date' e 'end_date', dentro de um loop para cada ano
informado na lista 'plot_years'. O objetivo é montar um gráfico de cotas em função
do tempo dos valores no período de cheia do Rio Negro (entre dezembro e junho).
Também é calculada a média dos valores para todo o período de dados.

Fonte: Porto de Manaus https://www.portodemanaus.com.br/?pagina=nivel-do-rio-negro-hoje
