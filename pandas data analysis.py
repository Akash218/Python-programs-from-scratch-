import pandas as pd
CLASS_A={'names':['aravind','anoop','arjun','bala','kalki','vishnu','chandru','kamesh','krishna','jerold','ashok'],'marks in english':[78,82,76,92,88,86,77,68,65,95,79],'marks in tamil':[86,77,68,65,95,92,88,86,77,68,90],'marks in maths':[79,80,90,82,83,65,95,92,88,86,77],'marks in science':[76,88,87,69,70,79,80,90,82,83,65],'marks in social':[88,87,89,90,91,87,69,70,79,80,90]}
df1=pd.DataFrame(CLASS_A)
#print(df.head(5))
#print(df.tail(4))
#print(df.shape[0])
#print(df.info)
#print(df.index)
#print(df.describe())
#print(df.mean)
CLASS_B={'names':['sridhar','sriram','tamil','nithish','sathish'],'marks in english':[77,98,79,90,80],'marks in tamil':[78,79,78,76,69],'marks in maths':[79,89,80,70,98],'marks in science':[78,87,98,89,70],'marks in social':[90,80,70,96,95]}
df2=pd.DataFrame(CLASS_B,index=range(11,16))
merge=pd.merge(df1,df2)
#print(merge)
add=pd.concat([df1,df2])
print(add)
slicing=df1.loc([3:7],[2:5])
print(slicing)