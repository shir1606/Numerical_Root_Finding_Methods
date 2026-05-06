from os import name

import numpy as np
#Gemini chat for menu,calculation,etc.
#https://www.google.com/search?sca_esv=19ca41183bcca24c&sxsrf=ANbL-n4Sp8StCY3HPYXlFrVXM4D6iXsicw%3A1778048309859&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3vWUtYx0DZdicpfE1faGYemg2KC4yuMPyQlIvlWqq2AtcdVMJmMDffRprXURy79lwWYbYYV2Zn-_3zemGi58ZoYQT-gc_TefnhK7O6tgh3cJbnRhsfD9J2bnFesALGy1NtfkyaEXUF5U34PYt9QRs96v3tWGXCPutdqk722sMCshCQjZQw&ntc=1&sa=X&ved=2ahUKEwijuIOXgqSUAxUdg_0HHZ9HCqQQoo4PegYIAQgAEAM&biw=1440&bih=765&dpr=2&q=make+function+that+does+the+next+thing%3A%0A+1.sets+polynom%28calls+a+fuction+for+this%29%0A2.sets+the+area+where+the+answer+known%0A3.sets+Number+of+segments+to+divide+the+range+defined+in+the+previous+section+or+the+size+of+the+small+segment.+%28You+can+divide+into+segments+of+0.1%29%0A4.the+program+will+ask+which+function+use+to+calc+the+roots%2Cfor+this+use+while%2C+3+options+0+to+exit+and+default+option%3Aerror+try+again%0A%0Awrite+this+code+in+python&mstk=AUtExfBG63hb7mf4-xgfLsICHKuGnlpT0S7jVY--23wuhuVaZGkXzfvmS8aAkUSepdyNZF6boXDBbDQTHsETSg3g8gepW6lH4nmGbWhDLf-zIaaLDugJwZBxEJ4Ef1-YM_hhe5tbmonFqoHPkSOfCvMk9ExO5iqbvAiRx5EqqfRNIplgHMUDKk0EOd6-YVVeCouOVUVY3oKD4P9hnTDw92JT0Rkl-qJQ9BUVIxlIowyr-jai9Caz_YSp44-STppPMWHy6MixWr_emFwMuO6Jax4rb4UWWZI_zAKiYBE&csuir=1&udm=50
#Main function
def calculate_roots():
    #Main of the program: gets data, sets data, and executes the choice
    # 1. Set polynomial
    f=lambda x:dataSet(x,"Polynom")
    # 2. Set the range/area
    print("--- Define Range ---")
    start= lambda x:dataSet(x,"Range start")
    end = lambda x:dataSet(x,"Range End")

    # 3. Set segments
    # Dividing the range into steps (e.g., 0.1)
    step = lambda x:dataSet(x,"segment size (e.g., 0.1) ")
    segments = np.arange(start, end + step, step)

    # 4. Menu loop
    while True:
        print("\n--- Root Calculation Menu ---")
        print("1. Method A (e.g., Bisection)")
        print("2. Method B (e.g., Newton-Raphson)")
        print("3. Method C (e.g., Secant)")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "0":
            print("Exiting program.")
            break

        elif choice in ["1", "2", "3"]:
            print(f"Executing Method {choice} on range [{start}, {end}] with step {step}...")
            # You would insert your specific math logic here
            # Example: for s in segments: ...

        else:
            print("Error: Invalid input. Try again.")

#Data-setting functions
def dataSet(data,Name):
    #function that gets the data- same as input("Value", but works for everything needed)
    if (Name=="Polynom"):
        data=get_polynomial()
    else:
        print("Input",Name)
        data=input("Enter the data: ")
    return data
#Setting data
def get_polynomial():
    """Defines the polynomial function."""
    print("Define Polynomial, use (VALUE)^ for exponents,*+_+ for math signs")
    polinom=input("Enter the polynomial,use simplified(without brackets,like x^2+3x+9): ")
    # 1. Get the highest degree
    max_exp = int(input("Enter the amount of objects(for example-x^2+3x+9 is 3 objects): "))
    poly_data = []
    # 2. Iterate from 0 up to the max exponent
    # This ensures index [2] matches x^2
    for i in range(max_exp + 1):
        x = input(f"Enter coefficient for first part: ")
        coefficient = float(input(f"Enter coefficient for exponent {i}: "))
        term_tuple = (x, coefficient)
        poly_data.append(term_tuple)
    return polinom
#Setting the polinom, called out of dataSet only
#Getting info by user, returns the polynomial as a tupple of (multiply,exponent), f.e. 3x^9 is (3,9)
#=========================================================================
#Calculation-solution for x and derivative
#Derivative calculation
def derivative(polinom):
    for i in range(len(polinom)):
        if (polinom[i][1]!=0):
            polinom[i][0]=polinom[i][1]*polinom[i][0]
            polinom[i][1]=polinom[i][1]-1
        else:
            polinom[i][0]=0
    return polinom
#Calculation of the value for x in polynomial
def calculate(polinom,x):
    sum=0
    for i in range(len(polinom)):
        sum+= polinom[i][0]*(x**polinom[i][1])
    return sum


#=========================================================================
##Root calculation methods

def bisection():
    return
def newton_raphson():
    return
def secant():
    return





calculate_roots()

#===========================================================================
## Newton Raphson Method
#Gemini chat for menu,calculation,etc.
#https://gemini.google.com/share/fe600a2d640f
def  Newton_Raphson (poly_expression, point_start, point_end, epsilon=0.0001):
    """
    Finds a root of a polynomial within a given range using the Newton Raphson method.

    Parameters:
    poly_expression (sympy.Expr): The symbolic polynomial expression.
    point_start (float): The start of the interval.
    point_end (float): The end of the interval.
    epsilon (float): The desired precision (tolerance).

    Returns:
    float: The approximated root if found, otherwise None.
    """

    # Define the symbolic variable
    x = sp.symbols('x')

    # Calculate the first derivative symbolically using SymPy
    f_prime = sp.diff(poly_expression, x)

    # Initial guess: Midpoint of the range is a common starting point
    x_curr = float(point_start + point_end) / 2.0

    iteration_count = 0
    max_iterations = 100  # Safety guard to prevent infinite loops in non-convergent cases

    while iteration_count < max_iterations:
        iteration_count += 1

        # Evaluate f(x) and f'(x) at the current point
        # .subs replaces the symbol with the value, .evalf() evaluates it to a float
        f_val = float(poly_expression.subs(x, x_curr).evalf())
        f_prime_val = float(f_prime.subs(x, x_curr).evalf())

        # Convergence Check: Avoid division by zero if the derivative is too small
        if abs(f_prime_val) < 1e-12:
            print(f"Newton-Raphson failed to converge: Derivative is zero at x = {x_curr}")
            return None

        # Newton Raphson Formula: x_next = x_curr - f(x_curr) / f'(x_curr)
        x_next = x_curr - (f_val / f_prime_val)

        # Check if the result is within the required epsilon (Tolerance check)
        if abs(x_next - x_curr) < epsilon:
            print(f"Root found at: {x_next:.6f}")
            print(f"Number of iterations: {iteration_count}")
            return x_next

        # Update current x for the next iteration
        x_curr = x_next

    # If the loop finishes without returning, convergence was not reached
    print(f"Method did not converge within {max_iterations} iterations.")
    return None