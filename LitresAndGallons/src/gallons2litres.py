'''
Created on Jun 19, 2019

@author: Glen Millard
'''
#!/usr/bin/python


# glenmillard@gmail.com
# This takes US gallons of gasoline, converts the currency 
# and gallons to litres, and shows the equivalent price per litre
# that Americans would pay using the forex_python currency converter.

# This imports the currency converter forex_python
from forex_python.converter import CurrencyRates

#Sets the rate variable to grab currency rates
rate = CurrencyRates()

def usg2canl():
    ppgusd = float(input('Price per US Gallon?'))
    lpusg = float(3.85)
    can2usd = rate.convert('USD','CAD', ppgusd)
    print("The price in Canadian Dollars is : % 2.2f" %(can2usd))
    pplcad = ppgusd / lpusg
    print('The price per litre would be $: % 2.3f' %(pplcad))

usg2canl()
