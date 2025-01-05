import random

big_characters =   ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
small_characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
other =["!",'"',"£","$","%","^","&","*","(",")","_","-","=","+","[","]","{","}",";",":","@","'","#","~","<",">",",",".","/","?","`","¬","|"," "]
list_of_list = small_characters + big_characters + numbers + other
#print(list_of_list)
#print(len(list_of_list))

quit_program = False
while quit_program == False:
        choice_of_task = int(input("would you like to: \n 1 - encrypt password \n 2 - decrypt password \n 3 - quit program \n"))
      
        if choice_of_task == 1:
          use_prior_key =int(input("would you like to: \n 1 - use a pre-existing key \n 2 - use a newly generated key \n"))
          
          if use_prior_key == 1:
                  key_encrypt = []
                  key_enter_encrypt = (input("enter your key"))
                  for i in range(len(key_enter_encrypt)):
                          key_encrypt.append(key_enter_encrypt[i])
                          
          elif use_prior_key == 2:
                  key_enter_encrypt = int(input("would you like to: \n 1 - enter key length \n 2 - use default key length (5) \n"))
                  if key_enter_encrypt == 1:
                          key_length_encrypt = int(input("enter key length (1 - 20 reccomended) \n"))
                  elif key_enter_encrypt == 2:
                          key_length_encrypt = 5
                          
                  key_encrypt = []
                  for i in range (key_length_encrypt):
                          key_encrypt.append(random.randint(1,len(list_of_list)))
                          
                  key_copy = []
                  for i in range (len(key_encrypt)):
                    key_copy.append((str(key_encrypt[i])).zfill(2))
                  
                  for i in range (19):
                          for j in range (key_length_encrypt):
                                  temp_key_store = (key_encrypt[i]+key_encrypt[j])
                                  if temp_key_store > ((len(list_of_list))-1):
                                          temp_key_store -= (len(list_of_list))
                                  else:
                                          pass
                                  key_encrypt.append(temp_key_store)
                  print("key = ",*key_copy, sep ="")
                  print("full key = ",*key_encrypt, sep =" ")
                  print(len(key_encrypt))
                                  
          password_input=input("enter a string to be turned into a password \n")

          shuffle_code  =[]
          password_list =[]
          password_list_index = []
          new_password_index = []
          new_password  =[]
          
          for i in range(len(password_input)):
              password_list.append(password_input[i])
              shuffle_code.append(random.randint(1,100))
          for i in range(len(password_input)):
              password_list_index.append(list_of_list.index(password_list[i]))
         
         
          for i in range(len(password_input)):
                  temp_pwd_store = password_list_index[i]
                  temp_pwd_store += key_encrypt[i]
                  if temp_pwd_store > ((len(list_of_list))-1):
                          temp_pwd_store -= (len(list_of_list))
                  else:
                          pass
                  new_password_index.append(temp_pwd_store)
         
          for i in range(len(password_input)):
                  new_password.append(list_of_list[new_password_index[i]])
          print(new_password)
          #print(new_password)
          #print(shuffle_code)    
          #print(password_list)

        elif choice_of_task == 2:
                key_decrypt = []
                key_enter_decrypt = input("enter key")
                for i in range (len(key_enter_decrypt)):
                  key_decrypt.append(key_enter_decrypt[i])
                print(key_decrypt)
                                        
          
                pass
           
   
## turn key_copy back to int , remove zfill eg 09 --> 9 etc                            
