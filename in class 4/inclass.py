import json

# Load EC2 instance data from the JSON file
def load_ec2_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Get user input for CPU and memory requirements
def get_cpu_requirements():
    min_cpu = int(input("Enter minimum required CPU cores: "))
    max_cpu = input("Enter maximum required CPU cores (or press Enter to skip): ")
    max_cpu = int(max_cpu) if max_cpu else None
    return min_cpu, max_cpu

def get_memory_requirements():
    min_memory = float(input("Enter minimum required memory in GiB: "))
    max_memory = input("Enter maximum required memory in GiB (or press Enter to skip): ")
    max_memory = float(max_memory) if max_memory else None
    return min_memory, max_memory

# Filter EC2 instances based on CPU and memory requirements
def filter_ec2_instances(ec2_data, min_cpu, max_cpu, min_memory, max_memory):
    filtered_instances = []
    for instance in ec2_data:
        cpu_cores = instance.get('cpu_cores')
        memory_gib = instance.get('memory_gib')
        
        # Ensure that both cpu_cores and memory_gib are not None before comparison
        if (cpu_cores is not None and memory_gib is not None and
            cpu_cores >= min_cpu and (max_cpu is None or cpu_cores <= max_cpu) and
            memory_gib >= min_memory and (max_memory is None or memory_gib <= max_memory)):
            filtered_instances.append(instance)
    return filtered_instances

# Display results in a readable format
def display_instances(instances):
    print("\nMatching EC2 Instances:")
    if not instances:
        print("No instances match the specified criteria.")
    else:
        for instance in instances:
            print(f"Instance Type: {instance['instance_type']}, "
                  f"CPU Cores: {instance['cpu_cores']}, "
                  f"Memory: {instance['memory_gib']} GiB")

# Main function
def main():
    file_path = 'ec2_instance_types.json'
    ec2_data = load_ec2_data(file_path)
    
    print("Enter your EC2 instance requirements:")
    min_cpu, max_cpu = get_cpu_requirements()
    min_memory, max_memory = get_memory_requirements()
    
    matching_instances = filter_ec2_instances(ec2_data, min_cpu, max_cpu, min_memory, max_memory)
    display_instances(matching_instances)

if __name__ == "__main__":
    main()
