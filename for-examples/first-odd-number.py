def main():  

  

    ls=[2,8,6,5,2,7,9]   
    
    index = next(i for i, num in enumerate(ls) if num % 2 != 0)

    return index  

  

main() 