from ALL_IMPORT import *
from GenerateData import *

def AddData(window) :
    #Taking File Name From Useer
    filepath = filedialog.askopenfilename(title='Select', filetypes=[("excel", ".xlsx"),("excel", ".xls"),("excel", ".xlsb"),("excel",".xlsm"),("excel",".xltx"),]);
    
    #Handeling Condition if Filepath is Entered Or Not
    if (len(filepath) == 0) :
        window.destroy();
        main();
        return;

    #Call To GenerateData Function
    GenerateData(filepath);

def main() :
    print("Jay Ganesh.....");
    window = Tk();

    #Title of GUI
    window.title("Excel To PDF Converter");

    #Size of Window 
    window.geometry('1000x300');

    #Header of Window
    Header = Label(window,font=("Courier","30","bold"),foreground="Dark Magenta",text="Mobicloud Technologies PVT LTD.");
    Header.place(relx = 0.52,rely=0.2,anchor=CENTER);

    #Creating Buttons 
    Btn = tkinter.Button(window, text='Select File',font=(24),height=2,width=15,command = lambda:AddData(window),bg="Dark Gray",fg="white") 
    Btn.place(relx = 0.3,rely=0.6,anchor=CENTER);

    Quit_btn = tkinter.Button(window, text="Close", font=(24),bg="Dark Gray",fg="white",height=2,width=15,command=window.destroy)
    Quit_btn.place(relx = 0.7,rely=0.6,anchor=CENTER);

    window.mainloop();

    # print("Jay Ganesh.....");

if __name__ == "__main__" :
    main();