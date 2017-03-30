def fib(num):

    prev = 0  
    current = 1
    fibo = 0
    for n in range(num):
        fibo = current + prev
        prev = current
        # print n, prev, fibo
        current = fibo
    
    return prev
    
print fib(3)





def max_duffel_bag_value(tuples, duff):
    
    values = []
    
    for kg, gbp in tuples:
        cost = gbp / float(kg)
        values.append((cost, gbp, kg))
    print values
    
    values.sort(reverse=True)
    print values
    
    
    profit = 0
    
    for cake in values:
        if duff >= cake[2]:
            num_cakes = duff / cake[2]
            duff -= (num_cakes * cake[2])
            profit += (num_cakes * cake[1])
            
    return profit
        
    
    
cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

print max_duffel_bag_value(cake_tuples, capacity)