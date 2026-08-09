def whyihaveto(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "error : You can't divide by zero!"