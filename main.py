import tkinter as tk
from tkinter import font
import yfinance as yf

root = tk.Tk()
HEIGHT = 800
WIDTH = 900

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH) # screen size
canvas.pack()

bg_image = tk.PhotoImage(file='stock-market-3.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

canvas = tk.Canvas(root, width=1000, height= 750, bg="#B8BAC8")
canvas.create_text(200, 50, text="Enter a stock ticker: ", fill="black", font=('Courier', 18))
canvas.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.1, anchor='n')

frame = tk.Frame(root, bg='black', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18), text='Enter the stock ticker: ')
entry.place(relwidth=0.65, relheight=1)

main_button = tk.Button(frame, text='Get Info', font=('Courier', 18), command=lambda:get_infos(entry.get()))
main_button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#B4D6D3', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18), bg='#3E92CC')
label.place(relwidth=1, relheight=1)


def show(stock):
    try:
        name = stock['shortName']
        sector = stock['sector']
        country = stock['country']
        lastDividend = stock['lastDividendValue']
        recommend = stock['recommendationKey']
        employ = stock['fullTimeEmployees']
        dayLow = stock['dayLow']
        dayHight = stock['dayHigh']
        dividends = stock['dividendYield']
        valuation = stock['enterpriseValue']
        if type(dividends) in [int, float]:
            final = f'Name: {name} \n Sector: {sector} \n Country: {country} \n Market Value: {valuation}$ \n Dividend Yield: {round(dividends*100, 2)}% / Last($): {lastDividend} \n Total employees: {employ} \n Day Low: {dayLow} / Day High: {dayHight} \n Recommendation: {recommend}' 
        else:
            final = f'Name: {name} \n Sector: {sector} \n Country: {country} \n Market Value: {valuation}$ \n Dividend Yield: {dividends} / Last($): {lastDividend} \n Total employees: {employ} \n Day Low: {dayLow} / Day High: {dayHight} \n Recommendation: {recommend}'

    except:
        final = 'An error has ocurred'    
    return final

def get_infos(entry):
    stock = yf.Ticker(entry).info
    label['text'] = show(stock)
root.mainloop()
