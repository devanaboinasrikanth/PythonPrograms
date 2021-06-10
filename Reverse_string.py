# class String:
#     def reverse_string(self,str):
#         str1 =""
#         for i in str:
#             str1 = i + str1
#         return str1
# res=String()
# str = input("enter the string:")
# print("orginal string is:", str)
# print("after reversing string is:", res.reverse_string(str))

# class Student:
#     def fre_count(self,orgstr):
#         count=1
#         lenght=''
#         if len(orgstr)>1:
#             for i in range(1,len(orgstr)):
#                 if(orgstr[i-1]==orgstr[i]):
#                     count+=1
#                 else:
#                     lenght+=orgstr[i-1]+str(count)
#                     count=1
#             lenght+=orgstr[i]+str(count)
#         else:
#             i=0
#             lenght+=orgstr[i]+str(count)
#         print(lenght)
# output=Student()
# orgstr=input("enter the string:")
# print("orginal string is:",orgstr)
# output.fre_count(orgstr)




with open("C:\\Users\\admin\\Desktop\\abc.txt", "r") as txt_file:
  new_data = list(set(txt_file))
  # new_data=set(txt_file)
  print(new_data)


# lines_seen = set()
# with open("C:\\Users\\admin\\Desktop\\abc.txt", "r+") as f:
#     d = f.readlines()
#     f.seek(0)
#     for i in d:
#         if i not in lines_seen:
#             f.write(i)
#             lines_seen.add(i)
#     f.truncate()
#     print(lines_seen)

