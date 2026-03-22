import pandas
import matplotlib.pyplot as pyplot

dataFrame_lifeExpectancy_raw = pandas.read_csv('life_expectancy.csv', delimiter=';', decimal=',')
dataFrame_lifeExpectancy = dataFrame_lifeExpectancy_raw[["Country","Region","Year","Economy_status_Developed","Under_five_deaths"]]

dataFrame_underFiveDeaths = dataFrame_lifeExpectancy["Under_five_deaths"]
#Imprime a tabela estatistica da variavel
print(dataFrame_underFiveDeaths.describe())
print('Amplitude:', dataFrame_underFiveDeaths.max() - dataFrame_underFiveDeaths.min())
print('Distancia Interquartilica:', dataFrame_underFiveDeaths.quantile(0.75) - dataFrame_underFiveDeaths.quantile(0.25))
print('Coeficiente de variação:', dataFrame_underFiveDeaths.std() / dataFrame_underFiveDeaths.mean())
print('Mode:', dataFrame_underFiveDeaths.mode())
print('Assimetria:', dataFrame_underFiveDeaths.skew())
print('Curtose:', dataFrame_underFiveDeaths.kurtosis())




figures, axis = pyplot.subplots(1,2)

axis[0].hist(dataFrame_underFiveDeaths, bins=30, edgecolor='black')
axis[0].set_title('Histograma de Mortes antes dos 5 anos por 1.000 pessoas')
axis[0].set_xlabel('Morte antes dos 5 anos por 1.000 pessoas')
axis[0].set_ylabel('Frequência')

axis[0].axvline(dataFrame_underFiveDeaths.mean(),color="red",label="Média")
axis[0].axvline(dataFrame_underFiveDeaths.median(),color="blue",label="Mediana")
axis[0].legend(loc="upper right")

axis[1].boxplot(dataFrame_underFiveDeaths)
axis[1].set_title('Boxplot de Mortes antes dos 5 anos por 1.000 pessoas')

pyplot.show()


