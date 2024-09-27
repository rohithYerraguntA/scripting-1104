# Names : Rohith Yerragunta, Sandeep Dulam
# Group - 12
# date : 27th Sep, 2024
'''
Description: This code allows user to provision resources for multiple times and also check if the entered value
is either a positive or a negative value.
'''


cpu_cores_max = 16
memory_max = 500
cpu_cores_utilized = 0
memory_utilized = 0.0
resources_allocated = []
requests_pending = []
 

while True:    
    username = input("enter your username: ")
    requested_cpu_cores = int(input("enter number of cpu cores required: "))
    requested_memory = float(input("enter amount of memory: "))
    
    if requested_cpu_cores > 0 and requested_memory > 0:
        cpu_cores_left = cpu_cores_max - cpu_cores_utilized
        memory_left = memory_max - memory_utilized
        if requested_cpu_cores <= cpu_cores_left and requested_memory <= memory_left:
            resources_allocated.append({"user":username, "cpu_cores":requested_cpu_cores, "memory":requested_memory})
            cpu_cores_utilized += requested_cpu_cores
            memory_utilized += requested_memory
       
        else:
            requests_pending.append({"username":username, "cpu_cores":requested_cpu_cores, "memory":requested_memory})
    else:
        print("enter a positive number ")     
        
                
    additional_request = input("do you want to make another request? (yes/no): ").lower()
    if additional_request != "yes":
        break
print("\nallocated resources:")
for resource in resources_allocated:
    print(f"username:{resource['user']}, cpu cores:{resource['cpu_cores']}, Memory:{resource['memory']} GB")
print("\nPending Requests:")
for request in requests_pending:
    print(f"username:{request['username']}, cpu cores:{request['cpu_cores']}, Memory:{request['memory']} GB")
   
    
    
    