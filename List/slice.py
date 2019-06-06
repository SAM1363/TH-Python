def sillycase(x):
  # turn the argumnet half by taking the lenght and divide by 2
    half = int(len(x)//2) 
    
    upper = x[half:].upper()
    lower = x[:half].lower()
    return lower + upper
  

print(sillycase('samson'))

