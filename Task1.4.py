def average_waiting_time(customers):
    actual_time = 0  
    total_waiting_time = 0  
    n = len(customers)  
    
    for arrival_time, time_required in customers:
        if actual_time < arrival_time:
            actual_time = arrival_time
        waiting_time = actual_time + time_required - arrival_time
        total_waiting_time += waiting_time
        actual_time += time_required  
    
    return total_waiting_time / n  

customers = [(5, 2), (5, 4), (10, 3), (20, 1)]


average_waiting_time_value = average_waiting_time(customers)

print(f"Average waiting time: {average_waiting_time_value:.2f}") 

# Average waiting time: 3.25