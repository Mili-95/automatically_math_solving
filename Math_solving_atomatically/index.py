import questionary as qt
import cmath
import sympy as sym





print("=========Automatical Math Problem Solving============")

def menu():
    choice = qt.select("What do you want? ",
                       choices = [
                           "Ramanujan Math",
                           "Matrix Problem",
                           "Quadratic Equation",
                           "Logarithm",
                           "Differentiation",
                           "Exit"]).ask()
    
    if choice == "Ramanujan Math":
        def sai(a):
            c=0
            for i in range(1,2000):
                for j in range(1,2000):
                        if (j*j*j)+(i*i*i)==a:
                            c=c+1
                if c==2:
                    return "Yes, It is Ramanujan Number"
                    break
            else:
                return "No, It is not Ramanujan Number"
            
        a=int(input("Enter the number: "))
        b=sai(a)
        print(b)  
        
     
    
    elif choice == "Matrix Problem":
     
                print("General Matrix Addition:-[[_, _ , _],[_, _, _],[_, _, _]]")
                
                def matrix(m,n):
                    o =[]
                    for i in range(m):
                        row = []
                        for j in range(n):
                            inp = int(input(f"Enter o[{i}][{j}]"))
                            row.append(inp)
                        o.append(row)
                    return o 

                def sum(A, B):
                    output = []
                    for i in range(len(A)): #num rows
                        row = []
                        for j in range(len(A[0])): #num column
                            row.append(A[i][j] + B[i][j])
                        output.append(row) 
                    return output               
                            
                m = int(input("Enter the first elements: \n"))
                n = int(input("Enter the second elements: \n"))       


                print("Enter Matix A")
                A = matrix(m,n)
                print(A)

                print("Enter Matrix B")
                B = matrix(m, n)
                print(B)

                res= sum(A,B)
                print("The Matrix Addition Solutions are:", res)   
                           
   
    elif choice == "Quadratic Equation":
        try:
            print("General Form:- ax**2 + bx + c = 0")
            
            a = int(input("Enter a(a!=0): "))
            b = int(input("Enter b: "))
            c = int(input("Enter e: ")) 
            
            d=(b**2)-(4*a*c)
            soll = (-b-cmath.sqrt(d))/(2*a)
            sol2 = (-b+cmath.sqrt(d)) / (2*a)  
            print("\n")
            print(f"Result for equation. {a}x**2 + {b}x + {c}=0. are:- \n")
            
            if d > 0:
                print("Type of Roots: Two Distinct Roots")
            elif d == 0:
                print("Type of Roots: Two Equal Real Roots")
            elif d < 0:
                print("Type of Roots: Two Complex Roots")
            print(f"The Solution are {soll} and {sol2}")                  
        except ValueError:
            print("Please Enter the value! Try again!")
            
            
            
    elif choice == "Logarithm":
        try:
            
            print('Input the base')
            base = int(input())

            print('Input the number')
            number = int(input())

            result = (cmath.log(number, base))

            print('Your answer =>', 'log', round(result))
            
        except ValueError:
            print("Please Enter the value! Try again!") 
            
    elif choice == 'Differentiation':
        try:
            # Declaring variables
            x, y, z = sym.symbols('x y z')
            
                 
            # expression of which we have to find derivative
            exp = x**3 * y + y**3 + z
            
            # Differentiating exp with respect to x
            derivative1_x = sym.diff(exp, x)
            print('derivative w.r.t x: ',
                derivative1_x)
            
            # Differentiating exp with respect to y
            derivative1_y = sym.diff(exp, y)
            print('derivative w.r.t y: ',derivative1_y)
                        
                        
            
        
        except ValueError:
            print("Please Enter the value! Try again!")   
                      
                
           
        
    

    
    
    
    
if __name__ == "__main__":
    while True:
       menu()
    
        