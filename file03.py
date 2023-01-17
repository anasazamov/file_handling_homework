def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    arr2=[]
    txt=open(data,mode="r").read()
    for i in txt:
        
        if i.isdigit():
            arr2.append(i)
# Read data from file
    return arr2
    
# Read data from file
print(main('txt_file/data03.txt'))