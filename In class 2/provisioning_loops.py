"""
Author: [Your Name]
Date: [Current Date]
Description: This script simulates a cloud resource provisioning system using loops and lists.
It allows multiple resource allocation requests and keeps track of allocated resources and pending requests.
"""
# Total available resources
TOTAL_CPU_CORES = 16  # Total available CPU cores
TOTAL_MEMORY_GB = 64.0  # Total available memory in GB
# Lists to store allocated resources and pending requests
allocated_resources = []
pending_requests = []
# Variables to keep track of remaining resources
remaining_cpu_cores = TOTAL_CPU_CORES
remaining_memory_gb = TOTAL_MEMORY_GB
while True:
    # Get user input for the resource request
    username = input("Enter your username: ")
    required_cpu_cores = int(input("Enter the number of required CPU cores: "))
    required_memory_gb = float(input("Enter the amount of required memory (GB): "))

    # Check if the requested resources are available
    if required_cpu_cores <= remaining_cpu_cores and required_memory_gb <= remaining_memory_gb:
        # Allocate the resources and update the remaining resources
        allocated_resources.append([username, required_cpu_cores, required_memory_gb])
        remaining_cpu_cores -= required_cpu_cores
        remaining_memory_gb -= required_memory_gb
        print(f"Resources allocated successfully for {username}.")
    else:
        # Add the request to the pending requests list
        pending_requests.append([username, required_cpu_cores, required_memory_gb])
        print(f"Insufficient resources for {username}. Request added to pending.")

    # Ask the user if they want to make another request
    another_request = input("Do you want to make another request? (yes/no): ").strip().lower()
    if another_request != 'yes':
        break
# Display allocated resources in a table format
print("\nAllocated Resources:")
print(f"{'Username':<15}{'CPU Cores':<10}{'Memory (GB)':<10}")
for resource in allocated_resources:
    print(f"{resource[0]:<15}{resource[1]:<10}{resource[2]:<10}")

# Display pending requests in a table format
print("\nPending Requests:")
print(f"{'Username':<15}{'CPU Cores':<10}{'Memory (GB)':<10}")
for request in pending_requests:
    print(f"{request[0]:<15}{request[1]:<10}{request[2]:<10}")

# Show remaining available resources
print(f"\nRemaining CPU cores: {remaining_cpu_cores}")
print(f"Remaining memory (GB): {remaining_memory_gb}")
