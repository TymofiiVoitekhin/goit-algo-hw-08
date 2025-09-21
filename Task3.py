import heapq

cables_lenght_1 = [1,2,3,4,5,6,7,8,9]

cables_lenght_2 = [1,9,5,4,7,3,8,2,6]

# Для знаходження порядку зʼєднання кабелів з мінімальними загальними витратами 
# потрібно додавати спочатку найменші кабелі до вже доданих

def order_by_heap (values):
    minimal_join = 0
    
    while values:
        heapq.heapify(values)
        min_value = heapq.heappop(values)
        minimal_join += min_value
        print ("Беремо кабель довжиною:", min_value)
    
    print("Мінімальне зʼєднання всіх кабелів:", minimal_join)
    
order_by_heap(cables_lenght_1)
print("-"*100)
order_by_heap(cables_lenght_2)