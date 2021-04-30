def volume(length):
    try: #check data types
        num = float(length)
    except: #invalid data types
        return None 
    if(num < 0): #the cube must have a side length of at least 0
        return None
    return num ** 3 #num^3