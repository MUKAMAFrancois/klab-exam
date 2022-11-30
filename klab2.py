from collections import ChainMap
#a =[ {'name': 'Bike', 'price':100}, {'name': 'TV', 'price':200},
            #   {'name': 'Album', 'price':10},
             #  {'name': 'Book', 'price':5}, {'name': 'Phone', 'price':500},
              # {'name': 'Computer', 'price':1000}]
cost_items=[{'Bike':100},{'TV':200},{'Book':5},{'Phone':500},{'Computer':1000}]
single_dictionary=dict(ChainMap(*cost_items))
print(single_dictionary)

##first question
cheapest=min(single_dictionary,key=lambda j :single_dictionary[j] )
print(f'CHEAPEST ITEM IS: {cheapest}')
## second question
expensive=max(single_dictionary,key=lambda j :single_dictionary[j])
print(f'EXPENSIVE ITEM IS: {expensive}')

## Third question
def SumOfAllPrices(x):
    prices=[]
    for i in x:
        prices.append(x[i])
    Total = sum(prices)

    return Total


print(f'SUM OF ALL PRICES=${SumOfAllPrices(single_dictionary)}')

## greater than 10
def greater_than10(y):
    greater=0
    for i in y:
        if y[i]>10:
            greater+=y[i]
    return greater

print(f'GREaTER THAN $10=${greater_than10(single_dictionary)}')

from collections import ChainMap
#a =[ {'name': 'Bike', 'price':100}, {'name': 'TV', 'price':200},
            #   {'name': 'Album', 'price':10},
             #  {'name': 'Book', 'price':5}, {'name': 'Phone', 'price':500},
              # {'name': 'Computer', 'price':1000}]
cost_items=[{'Bike':100},{'TV':200},{'Book':5},{'Phone':500},{'Computer':1000}]
single_dictionary=dict(ChainMap(*cost_items))
print(single_dictionary)

##first question
cheapest=min(single_dictionary,key=lambda j :single_dictionary[j] )
print(f'CHEAPEST ITEM IS: {cheapest}')
## second question
expensive=max(single_dictionary,key=lambda j :single_dictionary[j])
print(f'EXPENSIVE ITEM IS: {expensive}')

## Third question
def SumOfAllPrices(x):
    prices=[]
    for i in x:
        prices.append(x[i])
    Total = sum(prices)

    return Total


print(f'SUM OF ALL PRICES=${SumOfAllPrices(single_dictionary)}')

## greater than 10
def greater_than10(y):
    greater=0
    for i in y:
        if y[i]>10:
            greater+=y[i]
    return greater

print(f'GREaTER THAN $10=${greater_than10(single_dictionary)}')