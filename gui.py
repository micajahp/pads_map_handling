from tkinter import Tk, Label, Button









class ask():

    result = []
    def __init__(self):
        
        
        
        cards = [ask.D(),ask.R(),ask.C()]

        window = Tk()
        Label(window, text="Ask?").grid(row = 0, column=1)
            
        Button1 = Button(window, text=cards[0], command=lambda: [f for f in (self.result.append("D"),window.destroy() )] )
        Button1.grid(row = 1, column = 0)
        Button2 = Button(window, text=cards[1], command=lambda: [f for f in (self.result.append("R"),window.destroy() )] )
        Button2.grid(row = 1, column = 1) 
        Button3 = Button(window, text=cards[2], command=lambda: [f for f in (self.result.append("C"),window.destroy() )] )
        Button3.grid(row = 1, column = 2)

        window.mainloop()
        
    



    def D():
    
        print("Decode")
        return 'Decode'

    def R():
    
        print("Reencode")
        return 'Re-encode'

    def C():
        
        print("Cancel")
        return 'cancel'
    



if __name__ == '__main__':
    r = ask()

    print(f"response : {r.result[0]}")