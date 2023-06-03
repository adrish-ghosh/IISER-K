import csv

def csv_to_tuple(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [tuple(row) for row in reader]
    return data

# Example usage
file_path = ''  # Replace with the path to your CSV file
result = csv_to_tuple(file_path)

# Print the tuples with brackets
for item in result:
    print("(", ", ".join(item), ")")

