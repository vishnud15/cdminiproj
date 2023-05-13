import tkinter as tk
import re

class CodeOptimizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Code Optimizer")
        self.root.geometry("1000x600")

        self.root.configure(bg="#f26868")

        self.heading = tk.Label(self.root, text="Code Optimizer", font=("Times Bold", 20),fg="black",bg="#f26868")
        self.heading.pack(side=tk.TOP, pady=20)

        self.input_label = tk.Label(self.root, text="Input", font=("Helvetica",16),fg="black",bg="#f26868")
        self.input_label.pack(side=tk.LEFT,anchor=tk.CENTER, pady=50)
        self.input_text = tk.Text(self.root, height=20, width=50)
        self.input_text.pack(side=tk.LEFT,anchor=tk.CENTER)

        self.output_label = tk.Label(self.root, text="Output", font=("Helvetica",16),fg="black",bg="#f26868")
        self.output_label.pack(side=tk.RIGHT,anchor=tk.CENTER, pady=50)
        self.output_text = tk.Text(self.root, height=20, width=50)
        self.output_text.pack(side=tk.RIGHT,anchor=tk.CENTER)

        self.optimize_button = tk.Button(self.root, text="Optimize", command=self.optimize)
        self.optimize_button.pack(side=tk.BOTTOM,anchor=tk.CENTER)
        self.root.mainloop()
    
    def optimize(self):
        input_code = self.input_text.get("1.0", tk.END).strip()
        list_of_lines = input_code.split("\n")
        dictValues = dict()
        constantFoldedList = []
        outputList= []
        print("Quadruple form after Constant Folding")
        print("-------------------------------------")
        for i in list_of_lines:
            i = i.strip("\n")
            op,arg1,arg2,res = i.split()
            if(op in ["+","-","*","/"]):
                if(arg1.isdigit() and arg2.isdigit()):
                    result = eval(arg1+op+arg2)
                    dictValues[res] = result
                    print("=",result,"NULL",res)
                    constantFoldedList.append(["=",result,"NULL",res])
                elif(arg1.isdigit()):
                    if(arg2 in dictValues):
                        result = eval(arg1+op+dictValues[arg2])
                        dictValues[res] = result
                        print("=",result,"NULL",res)
                        constantFoldedList.append(["=",result,"NULL",res])
                    else:
                        print(op,arg1,arg2,res)
                        constantFoldedList.append([op,arg1,arg2,res])
                elif(arg2.isdigit()):
                    if(arg1 in dictValues):
                        result = eval(dictValues[arg1]+op+arg2)
                        dictValues[res] = result
                        print("=",result,"NULL",res)
                        constantFoldedList.append(["=",result,"NULL",res])
                    else:
                        print(op,arg1,arg2,res)
                        constantFoldedList.append([op,arg1,arg2,res])
                else:
                    flag1=0
                    flag2=0
                    arg1Res = arg1
                    if(arg1 in dictValues):
                        arg1Res = str(dictValues[arg1])
                        flag1 = 1
                    arg2Res = arg2
                    if(arg2 in dictValues):
                        arg2Res = str(dictValues[arg2])
                        flag2 = 1
                    if(flag1==1 and flag2==1):
                        result = eval(arg1Res+op+arg2Res)
                        dictValues[res] = result
                        print("=",result,"NULL",res) 
                        constantFoldedList.append(["=",result,"NULL",res])
                    else:
                        print(op,arg1Res,arg2Res,res)
                        constantFoldedList.append([op,arg1Res,arg2Res,res])

            elif(op=="="):
                if(arg1.isdigit()):
                    dictValues[res]=arg1
                    print("=",arg1,"NULL",res)
                    constantFoldedList.append(["=",arg1,"NULL",res])
                else:
                    if(arg1 in dictValues):
                        print("=",dictValues[arg1],"NULL",res)
                        constantFoldedList.append(["=",dictValues[arg1],"NULL",res])
                    else:
                        print("=",arg1,"NULL",res)
                        constantFoldedList.append(["=",arg1,"NULL",res])

            else:
                print(op,arg1,arg2,res)
                constantFoldedList.append([op,arg1,arg2,res])

        print("\n")
        print("Constant folded expression - ")
        print("--------------------")
        for i in constantFoldedList:
            if(i[0]=="="):
                print(i[3],i[0],i[1])
            elif(i[0] in ["+","-","*","/","==","<=","<",">",">="]):
                print(i[3],"=",i[1],i[0],i[2])
            elif(i[0] in ["if","goto","label","not"]):
                if(i[0]=="if"):
                    print(i[0],i[1],"goto",i[3])
                if(i[0]=="goto"):
                    print(i[0],i[3])
                if(i[0]=="label"):
                    print(i[3],":")
                if(i[0]=="not"):
                    print(i[3],"=",i[0],i[1])

        print("\n")
        print("After dead code elimination - ")
        print("------------------------------")
        for i in constantFoldedList:
            if(i[0]=="="):
               pass
            elif(i[0] in ["+","-","*","/","==","<=","<",">",">="]):
               print(i[3],"=",i[1],i[0],i[2])
               outputList.append([i[3],"=",i[1],i[0],i[2]])
            elif(i[0] in ["if","goto","label","not"]):
               if(i[0]=="if"):
                  print(i[0],i[1],"goto",i[3])
                  outputList.append([i[0],i[1],"goto",i[3]])
               if(i[0]=="goto"):
                  print(i[0],i[3])
                  outputList.append([i[0],i[3]])
               if(i[0]=="label"):
                  print(i[3],":")
                  outputList.append([i[0]=="label"])
               if(i[0]=="not"):
                  print(i[3],"=",i[0],i[1])
                  outputList.append([i[3],"=",i[0],i[1]])

              
        
        outputString=""          
        
        for i in outputList:
            outputString += " ".join(i) + "\n"
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END,outputString)

if __name__ == '__main__':
    CodeOptimizer()

