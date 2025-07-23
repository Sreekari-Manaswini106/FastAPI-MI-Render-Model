import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib #job libraryto make pkl file

#creating data
data={
    "Math":[78,45,90,35,65,82,20,40,55,92],
    "Science":[69,40,95,30,70,75,20,45,60,98],
    "English":[72,79,88,25,60,85,28,50,58,93],
    "Result":["pass","fail","pass","fail","pass","pass","fail","fail","pass","pass"]
}

df=pd.DataFrame(data)
df['Result']=df["Result"].map({"pass": 1,"fail": 0})
print(df)

#feratures of label
x=df[["Math","Science","English"]]
y=df["Result"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

#train model
model=LogisticRegression()
model.fit(x_train,y_train)

#save dump(pkl)
joblib.dump(model,"model.pkl")