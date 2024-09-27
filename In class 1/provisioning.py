"""
Author: [Jaswant Singh]
Date: [2024/09/27]
Description: This script simulates a cloud resource provisioning system where the user requests CPU cores and memory. The program checks availability and attempts to provision resources.
"""
# Total available resources
TOTAL_CPU_CORES = 22  # Example: 22 cores available
TOTAL_MEMORY_GB = 104.0  # Example: 104 GB of memory available
# Input from user
required_cpu_cores = int(input("Enter the number of required CPU cores: "))
required_memory_gb = float(input("Enter the amount of required memory (GB): "))
# Provisioning logic
if required_cpu_cores <= TOTAL_CPU_CORES and required_memory_gb <= TOTAL_MEMORY_GB:
    print("Resources provisioned successfully.")
    remaining_cpu_cores = TOTAL_CPU_CORES - required_cpu_cores
    remaining_memory_gb = TOTAL_MEMORY_GB - required_memory_gb
else:
    print("Resource request exceeds capacity. Provisioning failed.")
    remaining_cpu_cores = TOTAL_CPU_CORES
    remaining_memory_gb = TOTAL_MEMORY_GB
# Output remaining resources
print(f"Remaining CPU cores: {remaining_cpu_cores}")
print(f"Remaining memory (GB): {remaining_memory_gb}")
