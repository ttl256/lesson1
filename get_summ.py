def get_summ(a, b, delimeter="&"):
    a = str(a)
    b = str(b)
    result = f"{a}{delimeter}{b}"
    return(result)

string = get_summ("Learn", 3.4)
print(string.upper())