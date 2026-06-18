import sys

def solve_case(route_num, num_stops, input_data, idx):
    num_segments = num_stops - 1
    segments = []
    for _ in range(num_segments):
        segments.append(int(input_data[idx]))
        idx += 1
        
    global_max = -1
    max_curr = 0
    
    start_curr = 1
    best_start = 1
    best_end = 1
    
    for k in range(num_segments):
        val = segments[k]
        current_stop = k + 2
        
        if max_curr + val < val:
            max_curr = val
            start_curr = k + 1
        else:
            max_curr += val
            
        if max_curr > global_max:
            global_max = max_curr
            best_start = start_curr
            best_end = current_stop
        elif max_curr == global_max:
            current_len = current_stop - start_curr
            best_len = best_end - best_start
            if current_len > best_len:
                best_start = start_curr
                best_end = current_stop
            elif current_len == best_len and start_curr < best_start:
                best_start = start_curr
                best_end = current_stop
                
    if global_max > 0:
        print(f"The nicest part of route {route_num} is between stops {best_start} and {best_end}")
    else:
        print(f"Route {route_num} has no nice parts")
        
    return idx

def read_input():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    num_routes = int(input_data[idx])
    idx += 1
    
    for route_num in range(1, num_routes + 1):
        num_stops = int(input_data[idx])
        idx += 1
        idx = solve_case(route_num, num_stops, input_data, idx)

read_input()