import pandas as pd
def data(url,email,price,w):
    f = open("C:/Users/39338/Downloads/customer.txt", "a")
    f.writelines([url,w,email,w, price])
    f.close()
