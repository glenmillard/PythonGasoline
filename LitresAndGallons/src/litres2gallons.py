'''
Created on Jun 19, 2019

@author: Glen Millard
'''
#!/usr/bin/python

# This imports the currency converter forex_python
from forex_python.converter import CurrencyRates

#Sets the rate variable to grab currency rates
rate = CurrencyRates()

#print rate.get_rates('USD')

#This converts the US Dollars to Canadian Dollars
#print rate.convert('USD','CAD', num)
#usd2can = rate.convert('USD','CAD', num)

def litre2gallon():
    ppl = float(input('price per litre?'))
    float(ppl)
    lpg = float(4.54)
    #num = float(input('Enter a value - in US Dollars:'))
    usd2can = rate.convert('CAD','USD', ppl)
    print ("It would be : % 2.3f" %(usd2can) , "In USD")
    #exch = float(input('exchange rate?'))
    ppgcad = lpg * ppl #price per gallon,litres per gallon times price per litre
    ppgusd = ppgcad * 0.85 * usd2can #a US gallon is 0.85 of an Imperial Gallon times the current exchange rate
    print ('The price would be :% 2.2f' %(ppgusd) ,'per gallon in US dollars')


litre2gallon()