import flet as ft

class Bac1(ft.Container):
    def __init__(self):
        super().__init__()                
                 
        self.a =ft.TextField(label="Nhập a",hint_text="a")        
        self.b=ft.TextField(label="Nhập b",hint_text="b")
        self.c=ft.TextField(label="Nhập c",hint_text="c")   
        self.result=ft.Text("", color="#000000", italic=True, weight="bold")
        self.result2=ft.Text("", color="#f24b0c", weight="bold")         
        self.content = ft.Column(
            controls=[   
                ft.Container(
                    padding=ft.padding.only(top=10),                    
                    content=ft.Column(                        
                        controls=[ 
                            ft.Row(
                                controls=[
                                    ft.Text("Pt: Ax + B = C", size=22, weight="bold")
                                ], alignment="center"
                            ),                         
                            ft.ResponsiveRow(controls=[
                                ft.Row(controls=[
                                    ft.Text("", size=0)]), 
                                    ft.Column(col={"xs": 12}, controls=[self.a]),   
                            ]), 
                            ft.Row(controls=[ft.Text("", size=0)]), 
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.b]),   
                            ]), 
                            ft.Row(controls=[ft.Text("", size=0)]),    
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.c]),   
                            ]),                                                                          
                            ft.Row(controls=[ft.Text("", size=0)]),  
                            ft.Row(
                                controls=[                           
                                    ft.ElevatedButton(" Kết quả ", bgcolor="blue50", color="blue", on_click=self.calc),
                                    ft.ElevatedButton(" Làm lại ", bgcolor="blue50", color="blue", on_click=self.de)                                     
                                ], alignment="spaceEvenly"
                            ),                                     
                            ft.Row(controls=[ft.Text("", size=0)]), 
                            ft.Container(
                                padding=ft.padding.only(left=5, right=5),
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(col={"xs":12},controls=[self.result])                                                                                    
                                    ]                                        
                                )                                    
                            ),                                   
                            ft.Container(
                                padding=ft.padding.only(left=5, right=5),
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(col={"xs":12},controls=[self.result2])                                                                                    
                                    ]                                        
                                )                                    
                            ),
                            ft.Row(controls=[ft.Text("", size=0)]), 
                            ft.Row(controls=[ft.Text("", size=0)]),
                                                                                                    
                        ]                                                                                          
                    )                                                           
                )   
            ]
        )
    
    def de (self,e):       
        self.a.value = ""
        self.b.value = ""
        self.c.value = ""        
        self.result.value = ""            
        self.result2.value = ""       
        self.update()      
               
    def calc(self,e):        
        self.result.size=18
        self.result2.size=20
        choice_a= float(self.a.value)
        choice_b= float(self.b.value)
        choice_c= float(self.c.value)      
        if (choice_a != 0):      
            if choice_b > 0:
                x = float((choice_c - choice_b) / choice_a)              
                self.result.value = str("Phương trình: \n {0}x + {1} = {2}".format(choice_a,choice_b,choice_c) + " có nghiệm: ")
                self.result2.value = str(" x = " + str("%.2f" %(x)) )         
            elif choice_b < 0:
                y = float((choice_c + (choice_b * -1)) / choice_a)
                self.result.value = str("Phương trình: \n {0}x + {1} = {2}".format(choice_a,choice_b,choice_c) + " có nghiệm: ")    
                self.result2.value = str(" x = " + str("%.2f" %(y)))
            elif choice_b == 0:
                x = float((choice_c - choice_b) / choice_a)              
                self.result.value = str("Phương trình: \n {0}x + {1} = {2}".format(choice_a,choice_b,choice_c) + " có nghiệm: ")
                self.result2.value = str(" x = " + str("%.2f" %(x)) ) 
        elif (choice_a == 0):
            if (choice_b - choice_c != 0): 
                self.result.value = str("Phương trình: \n {0}x + {1} = {2}".format(choice_a,choice_b,choice_c))
                self.result2.value = str("=> vô nghiệm")
            elif (choice_b - choice_c == 0):
                self.result.value = str("Phương trình: \n {0}x + {1} = {2}".format(choice_a,choice_b,choice_c))
                self.result2.value = str("=> vô số nghiệm")                 
        self.update()         
