import tkinter as tk
from tkinter import font
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("科学计算器")
        master.configure(bg='#F0F0F0')
        
        # 创建自定义字体
        self.default_font = font.Font(family='Segoe UI', size=12)
        self.symbol_font = font.Font(family='Arial', size=14, weight='bold')
        
        # 初始化变量
        self.total = tk.StringVar()
        self.current = tk.StringVar()
        self.entry_value = ''
        self.current.set('0')
        self.total.set('')
        self.functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log10,
            'ln': math.log,
            '√': math.sqrt,
            'x²': lambda x: x**2,
            'x!': math.factorial,
            '1/x': lambda x: 1/x,
            'π': lambda: math.pi,
            'e': lambda: math.e
        }
        
        # 创建界面
        self.create_display()
        self.create_buttons()
        
    def create_display(self):
        # 结果显示区域
        frame = tk.Frame(self.master, height=100, bg='#FFFFFF')
        frame.pack(expand=True, fill='both', padx=5, pady=5)
        
        total_label = tk.Label(frame, textvariable=self.total, anchor='e',
                              bg='#FFFFFF', fg='#666666', font=self.default_font)
        total_label.pack(expand=True, fill='both', padx=5)
        
        current_label = tk.Label(frame, textvariable=self.current, anchor='e',
                                bg='#FFFFFF', fg='#000000', font=(self.default_font, 20, 'bold'))
        current_label.pack(expand=True, fill='both', padx=5)
        
    def create_buttons(self):
        # 按钮布局
        button_frame = tk.Frame(self.master, bg='#F0F0F0')
        button_frame.pack(expand=True, fill='both', padx=5, pady=5)
        
        buttons = [
            ('2nd', '(', ')', 'CE', 'C'),
            ('sin', 'cos', 'tan', 'log', 'ln'),
            ('x²', 'x!', '√', '^', '÷'),
            ('7', '8', '9', '×', '%'),
            ('4', '5', '6', '-', '1/x'),
            ('1', '2', '3', '+', '='),
            ('0', '.', 'π', 'e', '')
        ]
        
        for row_idx, row in enumerate(buttons):
            for col_idx, text in enumerate(row):
                if text == '=':
                    btn = self.create_button(button_frame, text, 6, 3, colspan=2)
                elif text == '0':
                    btn = self.create_button(button_frame, text, 6, 0, colspan=2)
                elif text == '':
                    continue
                else:
                    btn = self.create_button(button_frame, text, row_idx, col_idx)
                
                # 设置特殊按钮颜色
                if text in ['=', 'CE', 'C']:
                    btn.configure(bg='#4A90E2', fg='white')
                elif text in ['sin', 'cos', 'tan', 'log', 'ln', 'x²', 'x!', '√', '1/x', 'π', 'e']:
                    btn.configure(bg='#F8F8F8', fg='#4A90E2')
                elif text in ['2nd']:
                    btn.configure(bg='#E6E6E6', fg='#666666')
        
    def create_button(self, frame, text, row, column, colspan=1):
        btn = tk.Button(frame, text=text, font=self.symbol_font if text in ['÷','×','-','+','^'] else self.default_font,
                       command=lambda t=text: self.on_button_click(t),
                       bg='#FFFFFF', fg='#333333', relief='flat', 
                       activebackground='#E0E0E0', activeforeground='#000000')
        btn.grid(row=row, column=column, columnspan=colspan, 
                sticky='nsew', padx=2, pady=2)
        frame.rowconfigure(row, weight=1)
        frame.columnconfigure(column, weight=1)
        return btn
        
    def on_button_click(self, value):
        if value == 'C':
            self.entry_value = ''
            self.current.set('0')
            self.total.set('')
        elif value == 'CE':
            self.entry_value = self.entry_value[:-1]
            self.current.set(self.entry_value or '0')
        elif value == '=':
            try:
                result = eval(self.entry_value.replace('^', '**').replace('×','*').replace('÷','/'))
                self.total.set(self.entry_value + '=')
                self.current.set(str(result))
                self.entry_value = str(result)
            except Exception as e:
                self.current.set('错误')
                self.entry_value = ''
        elif value in self.functions:
            try:
                if value in ['π', 'e']:
                    num = self.functions[value]()
                    self.entry_value += str(num)
                    self.current.set(self.entry_value)
                else:
                    num = float(self.entry_value)
                    result = self.functions[value](num)
                    self.total.set(f"{value}({num})")
                    self.current.set(str(result))
                    self.entry_value = str(result)
            except Exception as e:
                self.current.set('错误')
                self.entry_value = ''
        else:
            self.entry_value += str(value)
            self.current.set(self.entry_value)
        
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("500x600")
    root.resizable(False, False)
    calc = ScientificCalculator(root)
    root.mainloop()