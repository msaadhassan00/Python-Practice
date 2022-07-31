#regression
sizes = [523,645,708,1034,2290,2545]
prices = [115,150,210,280,255,440]

c= 0;
# proce = size * m + c;

# m = price/size * class
multipliers = []

m = 0
loc = 0
for price in prices:
    m = price/sizes[loc]
    multipliers.append(m)
    loc=loc+1

multipliers = sum(multipliers)/len(multipliers)
print(multipliers)

price = 0.21734 * 523 + c
print(price)

for loc in range(len(prices)):
    price = m * sizes[loc]
    print("Predicted:",price," Actual Prices:",prices[loc])

