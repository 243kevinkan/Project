import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
import numpy_financial as npf # import numpy-financial

tickers = ["SPY", "VOO", "IVV", "VTI", "QQQ", "IWM", "EEM", "EFA", "VEA", "XLU"]

# Create an empty dictionary to store the Sharpe ratios
sharpe_ratios = {}

# Create an empty dictionary to store the annualized returns
annualized_returns = {}

# Loop through each ticker
for ticker in tickers:
    # Download the historical price data for the past max years
    data = yf.download(ticker, period="max")

    # Calculate the daily returns
    data["daily_return"] = data["Adj Close"].pct_change()

    # Calculate the annualized Sharpe ratio
    sharpe_ratio = data["daily_return"].mean() / data["daily_return"].std() * np.sqrt(252)

    # Calculate the annualized return
    annualized_return = (1 + data["daily_return"].mean()) ** 252 - 1

    # Store the Sharpe ratio in the dictionary
    sharpe_ratios[ticker] = sharpe_ratio
    # Store the annualized return in the dictionary
    annualized_returns[ticker] = annualized_return

# Sort the dictionary by values in descending order
sorted_sharpe_ratios = sorted(sharpe_ratios.items(), key=lambda x: x[1], reverse=True)

# Get the top 5 tickers with the highest Sharpe ratios
top_5_tickers = [ticker for ticker, _ in sorted_sharpe_ratios[:5]]

# Print the top 5 tickers
# Print their Sharpe ratios and annualized returns round to 2 decimals
print("The top 5 tickers are: ", top_5_tickers)
for ticker, sharpe_ratio in sorted_sharpe_ratios[:3]:
    print(f"The annualized Sharpe ratio for {ticker} is {sharpe_ratio:.2f}")
    print(f"The annualized return for {ticker} is {annualized_returns[ticker]:.2f}")


# Plot the price data for the top 3 tickers

for ticker in top_5_tickers:
    data = yf.download(ticker, period="max")
    plt.plot(data.index, data["Adj Close"], label=ticker)

plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Price Data for Top 5 ETFs")
plt.legend()
plt.show()

#Let the user input his/her current age and the age he/she wants to retire. Then calculate the number of years left until retirement
current_age= eval(input("Enter your current age: "))
retire_age= eval(input("Enter the age you want to retire: "))
years_left = retire_age - current_age
print("Number of years left until retirement: ", years_left)

#Let the user input how much money he/she wants to spend each year during the retirement. Then calculate the total amount of money needed for retirement
annual_spending = eval(input("Enter the amount of money you want to spend each year during retirement: "))
expected_return_after_retirement = 0.04
total_amount_needed = int(annual_spending /expected_return_after_retirement)
print("The　expected_return is 4% after retirement")
print(f"The total amount needed for retirement is: ${total_amount_needed:,.0f}")

# count=1
# for ticker, sharpe_ratio in sorted_sharpe_ratios[:3]:
#     monthly_investment_amount = round(npf.pmt(annualized_returns[ticker]/12, years_left*12, 0, -total_amount_needed),0) # use npf.pmt
#     print("<",count,">")
#     count += 1
#     print(f"The required monthly investment amount for {ticker} to achieve the total amount of ${total_amount_needed:,.0f} is ${monthly_investment_amount:,.0f}")

# chosen_ticker = input("Choose one from the top 3 tickers: ")
# #if the user does not input the tickers, ask the user to choose again
# while chosen_ticker not in top_3_tickers:
#     chosen_ticker = input("Invalid input. Please choose one from the top 3 tickers: ")

# monthly_contribution = eval(input("Enter the monthly contribution you want to invest in: "))
# # Calculate the future value of the investment
# future_value = monthly_contribution * ((1 + annualized_returns[chosen_ticker]/12) ** (years_left*12) - 1) / (annualized_returns[chosen_ticker]/12)
# print(chosen_ticker,":", f"The future value of the investment in retirement is: ${future_value:,.0f}")

# # Ask the user if they want to invest other tickers
# other_tickers = input("Do you want to invest in other tickers? (yes/no): ")
# # Loop until the user does not input year or no
# while other_tickers != "yes" and other_tickers != "no":
#     other_tickers = input("Invalid input. Please enter yes or no: ")

# total_future_value = future_value
# # Loop until the user does not want to invest in other tickers
# while other_tickers == "yes":
#     chosen_ticker = input("Choose one from the top 3 tickers: ")
#     while chosen_ticker not in top_3_tickers:
#         chosen_ticker = input("Invalid input. Please choose one from the top 3 tickers: ")
#     monthly_contribution = eval(input("Enter the monthly contribution you want to invest in: "))
#     future_value = monthly_contribution * ((1 + annualized_returns[chosen_ticker]/12) ** (years_left*12) - 1) / (annualized_returns[chosen_ticker]/12)
#     print(chosen_ticker,":", f"The future value of the investment in retirement is: ${future_value:,.0f}")
#     total_future_value += future_value
#     other_tickers = input("Do you want to invest in other tickers? (yes/no): ")
#     print("The total future value of the investment in retirement is: ", f"${total_future_value:,.0f}")

# Difference = total_future_value - total_amount_needed
# print("The total future value of the investment in retirement is: ", f"${total_future_value:,.0f}")
# print("The difference between the total future value and the total amount of money needed for retirement is: ", f"${Difference:,.0f}")
# #If the difference is positive, print "You will have more than enough money for retirement."
# if Difference > 0:
#     print("You will have more than enough money for retirement.")
# #If the difference is negative, print "You will not have enough money for retirement."
# else:
#     print("You will not have enough money for retirement.")

import os
import requests
import base64

# Configuration
API_KEY = "cad6f84406c0487fb434010c83b6f142"
IMAGE_PATH = "Doggy.jpg"
encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

# Payload for the request
payload = {
  "messages": [
    {
      "role": "system",
      "content": "You are a financial specialist and math expert."
    },
    {
           "role": "user",
      "content": "Please recommend one investment portflio based on"+str(top_5_tickers)+"for a person who is"+str(current_age)+ 
      "and plans to retire in"+str(years_left)+"years. Please reply the ticker and weight only"
    }
  ],
  "temperature": 0.7,
  "top_p": 0.95,
  "max_tokens": 800
}

ENDPOINT = "https://azure-openai-eastus-20240916.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"

# Send request
try:
    response = requests.post(ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")

# Select the portfolio recommendation part from the reponse and print out
response_json = response.json()
portfolio_recommendation = response_json['choices'][0]['message']['content']
print(portfolio_recommendation)


# #Ask the user if they want to invest in the recommended portfolio
# invest_portfolio = input("Do you want to invest in the recommended portfolio? (yes/no): ")
# # Loop until the user does not input year or no
# while invest_portfolio != "yes" and invest_portfolio != "no":
#     invest_portfolio = input("Invalid input. Please enter yes or no: ")

# #If the user wants to invest in the recommended portfolio, print "You have chosen to invest in the recommended portfolio."
# if invest_portfolio == "yes":
#     print("You have chosen to invest in the recommended portfolio.")
# #If the user does not want to invest in the recommended portfolio, print "You have chosen not to invest in the recommended portfolio."
# else:
#     print("You have chosen not to invest in the recommended portfolio.")

