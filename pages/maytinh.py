import flet as ft
import math

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = button_clicked
        self.data = text                  
class DigitButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text, button_clicked, expand) 
        self.style = ft.ButtonStyle(                       
            color= "#000000", 
            bgcolor= "#FFFFFF",           
            side=ft.BorderSide(2, color= "#FFFF00"),
            shape=ft.RoundedRectangleBorder(radius=0)                       
        )                 
class ActionButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text, button_clicked)    
        self.style = ft.ButtonStyle(
            color= "#FF7335",            
            bgcolor= "#FFFFFF",          
            side=ft.BorderSide(2, color= "#FFFF00"),
            shape=ft.RoundedRectangleBorder(radius=0)           
        )     
class CalculatorApp(ft.Container):    
    def __init__(self):
        super().__init__()
        self.reset()   
        self.width = 350         
        self.bgcolor = "#37d4bc"   
        self.padding = ft.padding.only(top=50, left=18, right=18, bottom=18)         
        self.border_radius = ft.border_radius.only(top_left=20, top_right=20)      
        self.result = ft.TextField(read_only=True,border_color="#FFFFFF",bgcolor="#FFFFFF",text_align="end",text_style=ft.TextStyle(size=32, color="#000000", weight=ft.FontWeight.W_500))                 
        self.content = ft.Column(     
            controls=[     
                ft.ResponsiveRow(
                    controls=[                        
                        ft.Column(col={"xs":12}, controls=[self.result], alignment="end")  
                    ]
                ),                          
                ft.Row(
                    controls=[
                        ActionButton(text="AC", button_clicked=self.button_clicked),                        
                        DigitButton(text="+/-", button_clicked=self.button_clicked),  
                        DigitButton(text="0", button_clicked=self.button_clicked),    
                        ActionButton(text="/", button_clicked=self.button_clicked),                                                      
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="7", button_clicked=self.button_clicked),
                        DigitButton(text="8", button_clicked=self.button_clicked),
                        DigitButton(text="9", button_clicked=self.button_clicked),
                        ActionButton(text="X", button_clicked=self.button_clicked),                                           
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="4", button_clicked=self.button_clicked),
                        DigitButton(text="5", button_clicked=self.button_clicked),
                        DigitButton(text="6", button_clicked=self.button_clicked),
                        ActionButton(text="一", button_clicked=self.button_clicked),                                             
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="1", button_clicked=self.button_clicked),
                        DigitButton(text="2", button_clicked=self.button_clicked),
                        DigitButton(text="3", button_clicked=self.button_clicked),
                        ActionButton(text="+", button_clicked=self.button_clicked),                                                
                    ]
                ),  
                ft.Row(
                    controls=[                        
                        ActionButton(text="A²", button_clicked=self.button_clicked),   
                        ActionButton(text="A³", button_clicked=self.button_clicked),  
                        ActionButton(text="%", button_clicked=self.button_clicked)                      
                    ]
                ),              
                ft.Row(
                    controls=[
                        DigitButton(text="√A", button_clicked=self.button_clicked),     
                        DigitButton(text="∛A", button_clicked=self.button_clicked),   
                        DigitButton(text=".", button_clicked=self.button_clicked),    
                        ActionButton(text="=", button_clicked=self.button_clicked),   
                    ]
                )     
            ]
        )

    def button_clicked(self, e):
        data = e.control.data     
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()
        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "." ):
            if self.result.value == "0" or self.new_operand == True:            
                self.result.value = data
                self.new_operand = False
            else:                
                self.result.value = self.result.value + data
        elif data in ("+", "一", "X", "/", "√A", "∛A", "%", "A²", "A³"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator)            
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True   
        elif data in ("="):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator)            
            self.reset()           
        elif data in ("+/-"):
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)
            elif float(self.result.value) < 0:
                self.result.value = str(self.format_number(abs(float(self.result.value))))              
        self.update()   

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return round(num,10)    
        
    def calculate(self, operand1, operand2, operator):
        if operator == "+": 
            return self.format_number(operand1 + operand2)                     
        elif operator == "一":
            return self.format_number(operand1 - operand2)       
        elif operator == "X":
           return self.format_number(operand1 * operand2)    
        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)       
        elif operator == "A²":
            return self.format_number(operand1 ** 2)
        elif operator == "A³":
            return self.format_number(operand1 ** 3)       
        elif operator == "√A":
            if float(self.result.value) < 0:
                return "Error"            
            else:
                return self.format_number(math.sqrt(float(operand1)))             
        elif operator == "∛A":
            return self.format_number(math.cbrt(float(operand1)))     
        elif operator == "%":
            return self.format_number(operand1 / 100)    
                      
    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True
