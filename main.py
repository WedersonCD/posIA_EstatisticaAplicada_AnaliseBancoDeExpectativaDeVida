import pandas

dataFrame_lifeExpectancy_raw = pandas.read_csv('life_expectancy.csv', delimiter=';', decimal=',')

dataFrame_lifeExpectancy = dataFrame_lifeExpectancy_raw[["Country","Region","Year","Economy_status_Developed","Under_five_deaths"]]

print(dataFrame_lifeExpectancy.head(5))