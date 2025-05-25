import json

products = []

try:
    with open("mock_data.json", "r") as f:
        products = json.load(f)
except FileNotFoundError:
    print("Error: mock_data.json not found. Please ensure the file exists in the same directory.")
except json.JSONDecodeError:
    print("Error: Could not decode JSON from mock_data.json. Please ensure it is valid JSON.") 