# This is an advanced Calculator
import math
import cmath
def prints(word):
    print(word)
    print("-"*30)
# Classify operations
two_var = ['add', 'sub', 'mul', 'div', 'exp', 'rem']
one_var = ['abs', 'sroot', 'croot']
conversion = ['Degree To radian','Radian to degree']
all_op = two_var + one_var + conversion + ["trig","arctrig","constants"]
# Constants: e, pi, tau, ..etc
constants = {
    "e": math.e,
    "pi": math.pi,
    "tau": math.tau,
    "i": 1j,
    "golden ratio": 1.61803
}
# Global function for checking the range of numbers
def check(ans):
    if isinstance(ans, tuple):
        return False, ans[1]
    if isinstance(ans, str):
        return True
    mini = 10 ** -99
    maxi = 10 ** 99
    abs_ans = abs(ans)
    if ans == 0:
        return True
    if abs_ans >= mini and abs_ans <= maxi:
        return True
    elif abs_ans < mini:
        return False, 0
    else:
        return False, "Too Large Value"
# Add
def add(a, b):
    result = round((a + b), 4)
    return result
# Subtract
def sub(a, b):
    result = round((a - b), 4)
    return result
# Multiply
def mul(a, b):
    result = round((a * b), 4)
    return result
# Divide
def div(a, b):
    if b == 0:
        return False, "Can't Divide by Zero"
    result = round((a / b), 4)
    return result
# Exponent
def exp(a, b):
    if a == 0 and b <= 0:
        return False, "Math Error"
    result = round((a ** b), 4)
    return result
# Remainder
def remainder(a, b):
    if b == 0:
        return False, "Math Error" 
    result = a % b
    return result
# Absolute Value
def absolute(a):
    result = abs(a)
    return result
# Square Root
def sroot(a):
    if isinstance(a, complex):
        result = cmath.sqrt(a)
    else:
        if a < 0:
            result = cmath.sqrt(a)
        else:
            result = round((math.sqrt(a)), 4)
    return result
# Cube root
def croot(a):
    result = round((math.cbrt(a)), 4)
    return result
# Convert degree to radian
def degtorad(a):
    rad = round((a * (math.pi/180)), 4)
    return rad
# Convert radian to degree
def radtodeg(a):
    deg = round((a * (180/math.pi)), 4)
    return deg
# Trig-ratios of an angle + arc
def trig(function, a):
    norm_a = a % 360
    is_90_or_270 = math.isclose(norm_a, 90, abs_tol=1e-9) or math.isclose(norm_a, 270, abs_tol=1e-9)
    is_0_or_180 = math.isclose(norm_a, 0, abs_tol=1e-9) \
        or math.isclose(norm_a, 180, abs_tol=1e-9)\
        or math.isclose(norm_a, 360, abs_tol=1e-9)
    if (function == "tan" and is_90_or_270)\
        or (function == "csc" and is_0_or_180 ) \
        or (function == "sec" and is_90_or_270)\
        or (function == "cot" and is_0_or_180 ):
        return False, f"{function} {a} is not valid"
    # Convert to radian
    radian = degtorad(a)
    match function:
        case "sin":
            ans = round((math.sin(radian)), 4)
        case "cos":
            ans = round((math.cos(radian)), 4)
        case "tan":
            ans = round((math.tan(radian)), 4)
        case "csc":
            ans = round((1/math.sin(radian)), 4)
        case "sec":
            ans = round((1/math.cos(radian)), 4)
        case "cot":
            ans = round((1/math.tan(radian)), 4)
    if ans == 0.0:
        ans = 0.0
    expr = f"{function} {a} = {ans}"
    return expr
def arctrig(ratio, function):
    type_1 = ["arcsin", "arccos"]
    type_2 = ["arccsc", "arcsec"]
    if (function in type_1) and not (-1 <= ratio <= 1):
        return False, "DomainError: sin/cos must fall within [-1, 1]"
    elif (function in type_2) and (-1 < ratio < 1):
        return False, "DomainError: csc/sec must fall R-]-1, 1["
    # Calculations
    match function:
        case "arcsin":
            ans = math.asin(ratio)
            deg = radtodeg(ans)
        case "arccos":
            ans = math.acos(ratio)
            deg = radtodeg(ans)
        case "arctan":
            ans = math.atan(ratio)
            deg = radtodeg(ans)
        case "arccsc":
            ans = math.asin(1/ratio)
            deg = radtodeg(ans)
        case "arcsec":
            ans = math.acos(1/ratio)
            deg = radtodeg(ans)
        case "arccot":
            if ratio == 0:
                ans = constants["pi"]/2
            else:
                ans = math.atan(1/ratio)
            deg = radtodeg(ans)
    ans= round(ans, 4)
    expr = f"θrad = {ans}, θ° = {deg}"
    return expr
# Main Calculator Logic
print("="*30)
prints("Welcome To Casio 991")
for i, op in enumerate(all_op):
    print(f"{i+1}. {op.capitalize()}")
    print("."*5)
while True:
    try:
        index = int(input("=> ").strip().lower())
        if index < 0:
            print("Not A Valid Index")
            continue
        operation = all_op[index-1]
        break
    except ValueError:
        print("-"*30)
        prints("Not A Valid Index")
    except IndexError:
        print("-"*30)
        prints("Not A Valid Index")
print("-"*30)
if operation in two_var:
    while True:
        try:
            x = float(input("Enter first number: ").strip())
            print("-"*30)
            break
        except ValueError:
            print("-"*30)
            prints("Not A Valid Number")
    while True:
        try:
            y = float(input("Enter second number: ").strip())
            print("-"*30)
            break
        except ValueError:
            print("-"*30)
            prints("Not A Valid Number")
    # Perform Operation
    match operation:
        case "add":
            ans = add(x,y)
            operator = "+"
        case "sub":
            ans = sub(x,y)
            operator = "-"
        case "mul":
            ans = mul(x,y)
            operator = "x"
        case "div":
            ans = div(x,y)
            operator = "/"
        case "exp":
            ans = exp(x,y)
            operator = "^"
        case "rem":
            ans = remainder(x,y)
            operator = "%"
    # Check The Answer
    is_ans = check(ans)
    if is_ans is True:
        prints(f"{x} {operator} {y} = {ans}")
    else:
        prints(f"MathError: {is_ans[1]}")
elif operation in one_var:
    while True:
        try:
            x = float(input("Enter number: ").strip())
            print("-"*30)
            break
        except ValueError:
            print("-"*30)
            prints("Not A Valid Number")
    match operation:
        case 'abs':
            ans = absolute(x)
            expr = f"|{x}| = {ans}"
        case "sroot":
            ans = sroot(x)
            expr = f"√{x} = {ans}"
        case "croot":
            ans = croot(x)
            expr = f"∛{x} = {ans}"
    is_ans = check(ans)
    if is_ans is True:
        prints(expr)
    else:
        prints(f"MathError: {is_ans[1]}")    
elif operation in conversion:
    while True:
        try:
            x = float(input("Enter Value: ").strip())
            print("-"*30)
            break
        except ValueError:
            print("-"*30)
            prints("Not A Valid Number")
    match operation:
        case "Degree To radian":
            ans = degtorad(x)
            expr = f"{x}° = {ans} rad"
        case "Radian to degree":
            ans = radtodeg(x)
            expr = f"{x} rad = {ans}°"
    is_ans = check(ans)
    if is_ans is True:
        prints(expr)
    else:
        prints(f"MathError: {is_ans[1]}")
elif operation == "trig":
    trig_func = ['sin', 'cos', 'tan', 'sec', 'csc', 'cot']
    for func in trig_func:
        print(f"{func}  ", end="")
    print("\n"+"-"*30)
    while True:
        function = input("Enter function: ").strip().lower()
        print("-"*30)
        if function not in trig_func:
            prints("Not A Valid Function")
            continue
        break
    while True:
        try:
            angle = float(input("Enter angle in degrees: ").strip())
            print("-"*30)
            break
        except:
            print("-"*30)
            prints("Not a Valid angle")
    # Apply the function
    expr = trig(function, angle)
    is_ans = check(expr)
    if is_ans is True:
        prints(expr)
    else:
        prints(f"MathError: {is_ans[1]}")
elif operation == "arctrig":
    arc_functions = ["arcsin", "arccos", "arctan", "arccsc", "arcsec", "arccot"]
    for i in range(6):
        print(f"{arc_functions[i]}  ", end="")
    print("\n"+"-"*30)
    while True:
        function = input("Enter The Inverse Trig Function: ").strip().lower()
        print("-"*30)
        if function not in arc_functions:
            prints(f"{function} is not a valid inverse trig function")
        else:
            break
    while True:
        try:
            ratio = float(input("Enter The Trig Ratio: ").strip())
            print("-"*30)
            break
        except ValueError:
            print("-"*30)
            prints("Not A Valid Ratio")
    expr = arctrig(ratio, function)
    is_ans = check(expr)
    if is_ans is True:
        prints(expr)
    else:
        prints(f"MathError: {is_ans[1]}")
elif operation == "constants":
    prints("Choose from these constants (Type the name of the constant itself)")
    constant = list(constants.keys())
    for i, val in enumerate(constant):
        print(f"{i+1}. {val}    ", end="")
    print("\n" + "-"*30)
    while True:
        con = input("=> ").strip().lower()
        print("-"*30)
        if con not in constant:
            prints("Not A Valid Constant")
        else:
            value = constants[con]
            break
    prints(f"{con} = {value}")