def dis(price, discount):
    percentdis = discount / 100
    dissedprice = percentdis * price
    finalprice = price - dissedprice
    print (int(finalprice))
    return round(finalprice, 2)


dis(100, 75)
