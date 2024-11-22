import json

# Sample data for instance types and costs
instance_data = {
    "t2.micro": {"price_per_hour": 0.0116, "cpu": 1, "memory": 1},
    "t2.small": {"price_per_hour": 0.023, "cpu": 1, "memory": 2},
    "t2.medium": {"price_per_hour": 0.0464, "cpu": 2, "memory": 4},
    "t2.large": {"price_per_hour": 0.0928, "cpu": 2, "memory": 8},
}

def calculate_instance_cost(instance_type, hours, storage_gb, storage_cost_per_gb=0.10):
    """
    Calculate the total cost for a cloud instance based on hours of use and additional storage.
    """
    if instance_type not in instance_data:
        raise ValueError("Invalid instance type.")
    
    instance_cost = instance_data[instance_type]["price_per_hour"] * hours
    storage_cost = storage_gb * storage_cost_per_gb
    total_cost = instance_cost + storage_cost
    
    return total_cost

def display_instance_options():
    """
    Display available instance types and their details.
    """
    print("Available Instance Types:")
    for instance, details in instance_data.items():
        print(f"{instance}: ${details['price_per_hour']}/hour, {details['cpu']} CPU, {details['memory']} GiB Memory")

def main():
    """
    Main function to handle user input and calculate costs.
    """
    print("Welcome to the Cloud Instance Cost Estimator!")
    display_instance_options()
    
    # Get user inputs
    instance_type = input("Enter the instance type (e.g., t2.micro): ").strip()
    hours = int(input("Enter the number of hours the instance will run: "))
    storage_gb = int(input("Enter the additional storage required (in GiB): "))
    
    try:
        total_cost = calculate_instance_cost(instance_type, hours, storage_gb)
        print(f"\nTotal Estimated Cost:")
        print(f"Instance Type: {instance_type}")
        print(f"Usage Hours: {hours}")
        print(f"Additional Storage: {storage_gb} GiB")
        print(f"Total Cost: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
