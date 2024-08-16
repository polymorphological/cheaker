import requests
import json
import time
import os

def get_balance(address, api_url, retries=3, delay=5):
    headers = {'Content-Type': 'application/json'}
    body = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [
            address
        ]
    }
    for attempt in range(retries):
        try:
            response = requests.post(api_url, headers=headers, data=json.dumps(body))
            response_json = response.json()
            balance = response_json.get('result', {}).get('value', 0)
            if balance != 0:
                return balance / 1e9  # Convert to SOL
        except Exception as e:
            print(f"Error retrieving balance for {address} on attempt {attempt + 1}: {e}")
        time.sleep(delay)  # Wait before the next retry
    print(f"Failed to retrieve balance for {address} after {retries} attempts.")
    return 0

def get_sol_price():
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd')
        response_json = response.json()
        return response_json.get('solana', {}).get('usd', 0)
    except Exception as e:
        print(f"Error retrieving SOL price: {e}")
        return 0

def load_addresses(file_path):
    try:
        with open(file_path, 'r') as file:
            addresses = file.read().splitlines()
        return addresses
    except Exception as e:
        print(f"Error loading addresses from file {file_path}: {e}")
        return []

def save_address(file_path, address):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            unique_addresses = set(file.read().splitlines())
    else:
        unique_addresses = set()

    if address in unique_addresses:
        print(f"Duplicate address: {address}")
    else:
        with open(file_path, 'a') as file:
            file.write(f"{address}\n")
        print(f"Address {address} saved in file {file_path}.")

def main():
    api_url = 'https://api.mainnet-beta.solana.com'  # Replace with the actual API URL
    active_addresses_file = '/workspaces/cheaker/active_addresses.txt'  # change it to your file path
    quality_addresses_file = '/workspaces/cheaker/quality_addresses.txt' # change it to your file path

    while True:
        addresses = load_addresses(active_addresses_file)
        sol_price = get_sol_price()

        if sol_price == 0:
            print("Failed to retrieve SOL price. Exiting script.")
            time.sleep(60)  # Wait 60 seconds before retrying
            continue

        for address in addresses:
            balance_sol = get_balance(address, api_url)
            balance_usd = balance_sol * sol_price
            if balance_usd > 1000:
                print(f"Address {address}: balance {balance_usd} USD.")
                save_address(quality_addresses_file, address)
            else:
                print(f"Address {address}: balance less than 1000 USD ({balance_usd} USD).")
        
        print("Check cycle completed. Restarting in 60 seconds.")
        time.sleep(60)  # Wait 60 seconds before the next cycle

if __name__ == "__main__":
    main()
