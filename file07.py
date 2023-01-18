def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    answer=0
 
    for i in data:
        if i.isdigit():
            answer+=int(i)
    return answer    
# Read data from file
