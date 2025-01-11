import flet as ft
import numpy as np

class Hept_Baan(ft.Container):
    def __init__(self):
        super().__init__()   
                       
        self.a1 =ft.TextField(label="Nhập a1",hint_text="a1")        
        self.b1=ft.TextField(label="Nhập b1",hint_text="b1")        
        self.c1=ft.TextField(label="Nhập c1",hint_text="c1")
        self.d1=ft.TextField(label="Nhập d1",hint_text="d1")      
        self.a2 =ft.TextField(label="Nhập a2",hint_text="a2")        
        self.b2=ft.TextField(label="Nhập b2",hint_text="b2")        
        self.c2=ft.TextField(label="Nhập c2",hint_text="c2")
        self.d2=ft.TextField(label="Nhập d2",hint_text="d2")              
        self.a3 =ft.TextField(label="Nhập a3",hint_text="a3")        
        self.b3=ft.TextField(label="Nhập b3",hint_text="b3")        
        self.c3=ft.TextField(label="Nhập c3",hint_text="c3")
        self.d3=ft.TextField(label="Nhập d3",hint_text="d3")                  
        self.result=ft.Text("", color="#000000", italic=True, weight="bold")
        self.result2=ft.Text("", color="#f24b0c", weight="bold")        
        self.content = ft.Column(
            controls=[   
                ft.Container(
                    padding=ft.padding.only(top=10),
                    content=ft.ResponsiveRow(
                        controls=[                                                                       
                            ft.Column(col={"xs":12}, controls=[ ft.Text("GIẢI HỆ PT BẬC NHẤT 3 ẨN", size=20, weight="bold")])                                                                                                                                              
                        ]                                        
                    )                     
                ),      
                ft.Container(                           
                    content=ft.Column(
                        controls=[ 
                            ft.Row(controls=[ft.Text("", size=0)]),                             
                            ft.ResponsiveRow(controls=[                              
                                ft.Column(col={"xs": 12}, controls=[self.a1]),   
                            ]),                        
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.b1]),   
                            ]),                           
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.c1]),   
                            ]),     
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.d1]),   
                            ]),                         
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.a2]),   
                            ]),   
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.b2]),   
                            ]),      
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.c2]),   
                            ]),       
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.d2]),   
                            ]),  
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.a3]),   
                            ]),  
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.b3]),   
                            ]),  
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.c3]),   
                            ]),      
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.d3]),   
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
                        ], scroll=ft.ScrollMode.AUTO, height=410                                                                                         
                    )                                                           
                )                                                  
            ]
        )  

    def de (self,e):       
        self.a1.value = ""
        self.b1.value = ""
        self.c1.value = ""  
        self.d1.value = ""
        self.a2.value = ""
        self.b2.value = ""
        self.c2.value = ""  
        self.d2.value = ""
        self.a3.value = ""
        self.b3.value = ""
        self.c3.value = ""  
        self.d3.value = ""        
        self.result.value = ""            
        self.result2.value = ""       
        self.update()           
       
    def calc(self,e):        
        self.result.size=18
        self.result2.size=20
        choice_a1= float(self.a1.value)
        choice_b1= float(self.b1.value)
        choice_c1= float(self.c1.value)    
        choice_d1= float(self.d1.value)
        choice_a2= float(self.a2.value)
        choice_b2= float(self.b2.value) 
        choice_c2= float(self.c2.value)
        choice_d2= float(self.d2.value)
        choice_a3= float(self.a3.value)    
        choice_b3= float(self.b3.value)
        choice_c3= float(self.c3.value)
        choice_d3= float(self.d3.value)     
        left_side = np.array([[choice_a1,choice_b1,choice_c1],[choice_a2,choice_b2,choice_c2],[choice_a3,choice_b3,choice_c3]])
        right_side = np.array([choice_d1,choice_d2,choice_d3])     
        x = np.linalg.solve(left_side,right_side)  
        self.result.value = str("Hệ pt: \n {0}x + {1}y +{2}z = {3} ; \n {4}x + {5}y + {6}z = {7} ; \n {8}x + {9}y + {10}z = {11} ; ".format(choice_a1,choice_b1,choice_c1,choice_d1,choice_a2,choice_b2,choice_c2,choice_d2,choice_a3,choice_b3,choice_c3,choice_d3) + " \n có các nghiệm: ")        
        self.result2.value = str(x)     
        self.update()         
