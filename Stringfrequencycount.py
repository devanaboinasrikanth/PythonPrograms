class Student:
    def fre_count(self,orginalstring):
        count=1
        lenght=''
        if len(orginalstring)>1:
            for i in range(1,len(orginalstring)):
                if(orginalstring[i-1]==orginalstring[i]):
                    count+=1
                else:
                    lenght+=orginalstring[i-1]+str(count)
                    count=1
            lenght+=orginalstring[i]+str(count)
        else:
            i=0
            lenght+=orginalstring[i]+str(count)
        print(lenght)
output=Student()
orginalstring=input("enter the string:")
print("orginal string is:",orginalstring)
output.fre_count(orginalstring)




