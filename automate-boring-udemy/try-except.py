def div50by (divideby):
    return 50/ divideby

print(div50by(2))

#function above works, but not when you divide by 0

def div10by (divby0):
    try:
        return 10/divby0
    except ZeroDivisionError:
        print("error we cant divide by 0")

print(div10by(0))