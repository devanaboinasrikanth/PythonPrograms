class String:
    def reverse_string(self,str):
        str1 =""
        for i in str:
            str1 = i + str1
        return str1
res=String()
str = input("enter the string:")
print("orginal string is:", str)
print("after reversing string is:", res.reverse_string(str))


