def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    txt=open(data)
    txt2=txt.read()
    
    str2=str(txt2)
    return len(str2)
# Read data from file
print(main("txt_file/data02.txt"))