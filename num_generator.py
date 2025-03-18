import os
import random

def main():
    #Ask the user for the number of values to generate
    try:
        num_values = int(input("Enter the number of values to generate: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    #Ask for the number of files to generate
    try:
        num_files = int(input("Enter the number of files to generate: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    #Ask for the directory to save the files
    directory = input("Enter the directory to save the files: ")
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} created.")    
    else:
        print(f"Using directory {directory}.")
        
    #Ask the user for the input range
    try:
        min_value = float(input("Enter the lower bound: "))
        max_value = float(input("Enter the upper bound: "))
        if min_value > max_value:
            print("The lower bound must be less than the upper bound.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    #Gererate the files
    for i in range(1, num_files + 1):
        file_name = f"file_{i}.txt"
        file_path = os.path.join(directory, file_name)
        with open(file_path, "w") as file:
            for j in range(num_values):
                value = random.uniform(min_value, max_value)
                file.write(f"{value:.4f}\n")
            print(f"Generated {file_path}")

if __name__ == "__main__":
    main()
        
