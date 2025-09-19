import heapq

cables_lenght_1 = [1,2,3,4,5,6,7,8,9]

cables_lenght_2 = [1,9,5,4,7,3,8,2,6]

# Для знаходження порядку зʼєднання кабелів з мінімальними загальними витратами 
# потрібно додавати спочатку найменші кабелі до вже доданих

def order_by_heap (values):
    while values:
        heapq.heapify(values)
        print ("Беремо кабель довжиною:", heapq.heappop(values))
    
order_by_heap(cables_lenght_1)
print("-"*100)
order_by_heap(cables_lenght_2)