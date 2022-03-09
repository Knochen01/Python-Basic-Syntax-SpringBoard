def convert_temp(unit_in, unit_out, temp):

    # YOUR CODE HERE
    if unit_in !="c" and unit_in !="f":
        return f"Wrong {unit_in}"
    
    if unit_out !="c" and unit_out !="f":
        return f"Wrong {unit_out}"
    
    if unit_in == "f" and unit_out =="c":
        temp = (temp - 32) * 5/9
    
    if unit_in == "c" and unit_out =="f":
        temp = (temp * 5 / 9) + 32
    
    return temp



print(convert_temp("c", "f", 0))
print(convert_temp("f", "c", 212)),
print(convert_temp("z", "f", 32)), 
print(convert_temp("c", "z", 32)), 
print(convert_temp("f", "f", 75.5)),

