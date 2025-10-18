nums=[1,2,3,1]
i,j=0,0
for i in range(len(nums)):
    print("i=",i)
    for j in range(i+1,len(nums)):
        print("j=",j)
        if nums[i]==nums[j]:
            print("nums[i]=",nums[i],"nums[j]=",nums[j])
            i+=1
            print("i=",i)
            j+=1
            print("j=",j)
        print("True")
print("False")
