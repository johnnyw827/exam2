test_string = "45.657"
  
# printing original string  
print("The original string : " + str(test_string)) 
  
# using float() 
# Check for float string 
try :  
    float(test_string) 
    res = True
except : 
    print("Not a float") 
    res = False
      
# print result 
print("Is string a possible float number ? : " + str(res)) 