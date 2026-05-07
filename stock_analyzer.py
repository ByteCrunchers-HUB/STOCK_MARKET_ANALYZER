import numpy as np

data = np.genfromtxt(
    "faang_stock_prices.csv",
    delimiter=",",
    names=True,
    dtype=None,
    encoding="utf-8"
)


stock = input("Enter Stock Name (AAPL/AMZN/GOOGL/META/MSFT/NVDA): ")
stock_data = data[data["Ticker"] == stock]
prices = stock_data["Close"]


def showClosePrices(stock,stock_data):
    closed_prices=stock_data["Close"][(stock_data["Ticker"]==stock)]
    dates=stock_data["Date"][(stock_data["Ticker"]==stock)]
    print(f"For Stock: ${stock}\n")
    for i in  range(0,len(closed_prices)):
        print(f"Date : {dates[i]} Closing_Price: {closed_prices[i]}")


def showDailyReturns(prices):
    prev=prices[1:]
    curr=prices[:-1]
    returns=((prev-curr)/prev)*100
    for i in range(0,len(returns)):
        print(f"Day{i+1}  Return:  $ {returns[i]}")



def AverageDailyRet(prices):
    prev=prices[1:]
    curr=prices[:-1]
    returns=((prev-curr)/prev)*100
    print(f"Average Return for {stock} :  $ {np.mean(returns)}")



def CalculateVolatility(prices):
    prev=prices[1:]
    curr=prices[:-1]
    returns=((prev-curr)/prev)*100
    v=np.std(returns)
    if(v<=1.0 and v<5):
        print("Stable Stock")
    if(v<20 and v>=5):
        print("Moderate Risk ")
    else:
        print("Highly Risky")


def showTotalReturns(prices):
        prev=prices[1:]
        curr=prices[:-1]
        returns=((prev-curr)/prev)*100
        print(f"Total Returns for {stock}..... ${np.sum(returns)}")

def RSI(prices):
    prev=prices[1:]
    curr=prices[:-1]
    diff=(prev-curr)
    gains=diff[diff>0]
    loss=diff[diff<0]
    avg_gain=np.mean(gains)
    avg_loss=np.mean(loss)
    RS=avg_gain/avg_loss
    RSI=100-(100/(1+RS))
    if(RSI>70):
        print("OverBought---->SELL SIGNAL")

    if(RSI<30):
        print("Oversold---->BUY SIGNAL")
        
    else:
        print("NORMAL")

def MA(stocks):
    sma_7=stocks["SMA_7"]
    sma_21=stocks["SMA_21"]
    dates=stocks["Date"]
    for i in range(len(sma_7)):
        if sma_7[i] > sma_21[i]:
            print(f"{dates[i]}    :   BUY SIGNAL 📈")

        elif sma_7[i] < sma_21[i]:
            print(f"{dates[i]}    :   SELL SIGNAL 📉")

        else:
            print(f"{dates[i]}    :   HOLD")





    


while True:

    print("\n===== STOCK ANALYZER =====")
    print("1. Show Close Prices")
    print("2. Daily Returns")
    print("3. Average Daily Return")
    print("4. Volatility(Reliable/Unreilable)")
    print("5. RSI Analysis")
    print("6. Moving Average Trend")
    print("7. Total Return")
    print("8. Switch Stock ")
    print("9. Exit")

    choice = int(input("Enter Choice: "))

    

    if choice == 1:
        showClosePrices(stock,stock_data)



    elif choice == 2:
        print(f"Daily Return as per all Days for {stock}.....")
        showDailyReturns(prices)

    elif choice == 3:
        AverageDailyRet(prices)


    elif choice == 4:
        CalculateVolatility(prices)

 
    elif choice == 5:
        RSI(prices)


    elif choice == 6:
        MA(stock_data)


    elif choice == 7:
        showTotalReturns(prices)
        
        
    elif choice == 8:
        stock = input("Enter Stock Name (AAPL/AMZN/GOOGL/META/MSFT/NVDA): ")
        stock_data = data[data["Ticker"] == stock]
    elif choice == 9:

        print("Exiting...")
        break

    else:
        print("Invalid Choice")