def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    num,char=0,0
    f=open(data).read()
    for i in f :
        if i.isdigit():
            num+=1
        elif i.isalpha():
            char+=1
    return [num,char]
# Read data from file
print(main('txt_file/data05.txt'))