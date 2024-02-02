## Lab Exercise - Python Libraries and Packages
##Part 1 – Implement Basic Data Structures using Numpy, Pandas
import numpy as np
import pandas as pd
l1=[7,21,20,28]
l2=[1,2,3,4]
print(type(l1))
arr1=np.array(l1)
arr2=np.array(l2)
r1=arr1+arr2
r2=arr1-arr2
r3=arr1*arr2
r4=arr1/arr2
r5=arr1**arr2
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print("Sine:",np.sin(arr1))
print("Natural logarithm:",np.log(arr1))
print("Base-10 logarithm:",np.log10(arr1))
print("Base-2 logarithm:",np.log2(arr1))
print("Exponential:",np.exp(arr1))


#Part 2 – Visualization of Data using matplotlib, pyplots Packages
people=['Abhi','Shiva','Prabha','Abhilash']
age=[19,45,39,21]
weight=[48,88,65,90]
height=[170,172,166,180]
import matplotlib.pyplot as plt
plt.scatter(weight,height)
plt.title("Relationship between weight and height of patients")
plt.ylabel("Height in meters")
plt.xlabel("Weight of patients in Kgs")
plt.show()

plt.figure(figsize=(4,4))
plt.title("People's weight in kgs",fontsize=16,fontstyle='italic')
plt.bar(x=people,height=weight,width=0.6,color='orange',edgecolor='k',alpha=0.6)
plt.xlabel("People",fontsize=15)
plt.ylabel("Weight (in Kgs)",fontsize=15)
plt.show()

import numpy as np
plt.figure(figsize=(7,5))
plt.hist(weight,color='red',edgecolor='k',alpha=0.75,bins=5)
plt.xlabel("weight in Kgs",fontsize=15)
plt.show()


# Part 3 – Access Data from Various Data Sources using builtin Function of Numpy, Pandas
import numpy as np
import pandas as pd
df1=pd.read_table("LAB-01-text.txt")
df1
data2=pd.read_csv("LAB-01-text.csv")
data2
data3=pd.read_excel("Height_weight.xlsx")
data3

