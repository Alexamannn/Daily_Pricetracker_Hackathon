import pandas as pd
from another import xx

data = pd.read_csv('C:/Users/39338/Downloads/customer.csv')


def pricecheker(x,y,z):
    pricenew=xx(x)
    if pricenew	<= y:
        print('emailsent')
    else:
        ww=1
    return ww


data['boolean'] = data.apply(lambda x: pricecheker(x['url'], x['price'],x['email']), axis=1)
