import tkinter as tk
from tkinter import messagebox

def cum_sum(n):
    return int(n*(n+1)/2)

while True:
    raw_input = input()
    try:
        n = int(raw_input)
        if 1 <= n <= 10000:
            print(cum_sum(n))
            break
        else:
            print("범위 안의 숫자가 아닙니다.")  
    except Exception:
        print(f"오류가 발생했습니다.")

root = tk.Tk()
root.title("Cumulative Sum Calculator")