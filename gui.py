from tkinter import Tk, Label, Button
import tkinter

class ask():

    result = []
    def __init__(self): 

        cards = [ask.D(),ask.R(),ask.C()]

        window = Tk()
        Label(window, text="Ask?", bg = '#D0D0D0').grid(row = 0, column=1)
        window.geometry('800x300') 
        window.configure(bg='#D0D0D0')   
        Button1 = Button(window, text=cards[0], command=lambda: [f for f in (self.result.append("D"),window.destroy() )] )
        Button1.config(height = 5, width = 20)
        Button1.grid(row = 4, column=0, padx = 55, pady = 50)
        Button2 = Button(window, text=cards[1], command=lambda: [f for f in (self.result.append("R"),window.destroy() )] )
        Button2.config(height = 5, width = 20)
        Button2.grid(row = 4, column=1, padx = 55, pady = 50) 
        Button3 = Button(window, text=cards[2], command=lambda: [f for f in (self.result.append("C"),window.destroy() )] )
        Button3.config(height = 5, width = 20)
        Button3.grid(row = 4, column=2, padx = 55, pady = 50)

        window.mainloop()

    
    def D():
    
        print("Decode")
        return 'Decode'


    def R():
    
        print("Reencode")
        return 'Re-encode'


    def C():
        
        print("Cancel")
        return 'Complete'
    

if __name__ == '__main__':
    r = ask()

    print(f"response : {r.result[0]}")
