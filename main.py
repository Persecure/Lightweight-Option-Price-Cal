from optionprice import Option

#initialize the option
'''
european :  True , False for American
kind :      call or put
s0 :        spot price 
k :         strike price
r :         risk free rate
sigma :     volatility 
dv :        dividends
start :     start date
end :       end date
'''
option_test = Option(european=True,
                    kind='call',
                    s0=167.53,
                    k=167.500,
                    r=0.03,
                    sigma=1.23,
                    dv=0,
                    start='2022-08-25',
                    end='2022-09-02')
            
# Check the option details
print(option_test)
# Calculate price options 
'''
Black scholes model : default
Monte Carlo : method = 'MC'
Binomial Tree : method = 'BT'
'''

price_bsm = option_test.getPrice()
print(price_bsm)

price_mc = option_test.getPrice(method='MC',iteration=5000)
print(price_mc)

price_bt = option_test.getPrice(method='BT',iteration=100)
print(price_bt)
