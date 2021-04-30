def average(array):
    try: 
        l = list(array)
    except: #invalid data type
        return None
    if(len(l) < 1): #no elements, divide by zero error
        return None
    sum = 0
    for e in l: #for each element in the list
        try: 
            sum += e #add to sum
        except: #invalid data type
            return None 
    return sum / len(l) #return sum / count (the average)
