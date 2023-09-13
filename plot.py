import matplotlib.pyplot as plt

def plot_basic_close(figsize, df, pair):
    plt.figure(figsize=figsize)
    df['Adj Close'].plot()
    
    # Set the title and axis label
    plt.title(f'{pair} Data', fontsize=16)
    plt.xlabel('Year-Month', fontsize=15)
    plt.ylabel('Price', fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.legend(['Close'], prop={'size': 10})
    
   
    plt.show()
    
    
def pred_vs_real_plot(df, pair, x, y, predictions, n_test):
    plt.figure(figsize=(15,7))
    plt.plot(x, y, alpha=0.75, c='b')
    plt.plot(x[-n_test:], predictions, alpha=0.75, c='g')  # Forecasts
    plt.show()    
    
    
    