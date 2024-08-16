# cheaker
Solana Wallet Monitor

This Python application provides a robust solution for monitoring Solana wallet balances and activities. It is designed to help users track SOL balances exceeding a specified threshold and identify wallets with frequent recent transactions. This tool is particularly useful for investors, marketers, and researchers interested in the Solana blockchain's dynamics.

Features
Real-time Balance Tracking: Fetch and monitor the balance of Solana wallets in SOL and its equivalent value in USD.
Price Retrieval: Automatically fetches the latest SOL price from CoinGecko to ensure accurate USD conversions.
Retry Mechanism: Implements a retry logic to handle potential API request failures, enhancing reliability.
Unique Address Storage: Saves qualifying addresses to a file, ensuring no duplicates and easy tracking.
Continuous Monitoring: Runs in a continuous loop, providing up-to-date information and enabling long-term monitoring.
How It Works
Load Addresses: Reads a predefined list of Solana wallet addresses from a file.
Get SOL Price: Retrieves the current SOL price from CoinGecko.
Check Balances: For each address, checks the balance in SOL and converts it to USD based on the current market price.
Filter and Save: Addresses with balances over $1,000 and at least three transactions in the last 30 days are saved to a separate file for further analysis or action.
Setup and Usage
Dependencies: Ensure all required Python packages are installed:
bash
Копировать код
pip install requests json time os
Configuration: Set the API endpoint and file paths in the script according to your local setup.
Running the Script:
bash
Копировать код
python main.py
Potential Use Cases
Market Analysis: Track high-value wallets to analyze market trends and predict potential movements.
Marketing Outreach: Identify active users within the Solana ecosystem for targeted marketing campaigns.
Compliance Monitoring: Use the tool for regulatory compliance purposes, ensuring all high-value transactions are recorded and analyzed.
Contributing
Contributions to enhance functionality or improve the reliability of the application are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

This project is open-sourced under the MIT license and aims to assist the broader Solana community by providing a valuable tool for wallet monitoring and analysis.
