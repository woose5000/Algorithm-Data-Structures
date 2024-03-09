import tkinter as tk
from tkinter import messagebox

def cum_sum(n):
    return int(n * (n + 1) / 2)

def calculate():
    try:
        n = int(entry.get())
        if 1 <= n <= 10000:
            result = cum_sum(n)
            result_label.config(text=f"결과: {result}")
        else:
            messagebox.showerror("오류", "범위 안의 숫자가 아닙니다.")
    except ValueError:
        messagebox.showerror("오류", "올바른 자료형이 아닙니다.")

# GUI 창을 생성하고 구성합니다.
root = tk.Tk()
root.title("Cumulative Sum Calculator")

# 입력 필드 생성
entry = tk.Entry(root)
entry.pack(pady=10)

# 계산 버튼 생성
calculate_button = tk.Button(root, text="계산", command=calculate)
calculate_button.pack(pady=5)

# 결과 레이블 생성
result_label = tk.Label(root, text="결과: ")
result_label.pack(pady=10)

# GUI 실행
root.mainloop()