import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

data = pd.read_csv("Worldcupmatches.csv")
df = pd.DataFrame(data)

#1.data analysis section
#i) printing no of rows and columns 
print(f"Number of Rows: {df.shape[0]}")     #shape function gives thd dimensions of the DataFrame ,
print(f"Number of Columns: {df.shape[1]}")  #it returns tuple where first element is no of rows and second is no of colunms 

#ii) Print Each Column Name
print("Column Names:\n")
print(df.columns)

#iii) Print Specific Range Using Slicing
print("printing rows 10 to 20\n")
print(df.iloc[10:21])


#iv) Summarization Statistics
print("printing describe function to show Statistical data\n")  #describe provides descrpitive statisyics of DataFrame numeric columns ,
print(df.describe())                                            #including min,standard deviation etc

#v) using min and max in particular column
print(f" home team goals max = {df["Home Team Goals"].max()}")  #max function is use to show maximum value in particular column
print(f" home team goals min = {df["Home Team Goals"].min()}")  #min function is use to show minimum value in particular column

### 2. Data Cleaning

#i) Check Missing Values
print("to check missing  values in ")
print(df.isnull().sum())    #isnull() is used to determine whwther there null valu is present or not in DataFrame 
                            #isnull().sum() is used to calculate total count of null value in DataFrame

#ii) Replace Missing Numerical Values with Mean or Median
# For numerical columns, replace missing values with mean
df.fillna(df["Home Team Goals"].mean(), inplace=True)
# you can use median function als0
df.fillna(df["Home Team Goals"].median(), inplace=True)

#iii) using cor() function 
numerical_df=df.select_dtypes(include="number")
corr_matrix = numerical_df.corr()
print(corr_matrix)

#3. Data Visualization

#i) Pairplot
sns.pairplot(df)
plt.title("pairplot")
plt.show()

#ii) Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.title("boxplot")
plt.legend(df)
plt.show()

#iii) Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("heatmap")
plt.show()

#iv) Barplot
plt.figure(figsize=(10, 6))
sns.barplot(x='Home Team Goals', y='Away Team Goals', data=df)
plt.title("barplot")
plt.xlabel='Home Team Goals'
plt.ylabel='Away Team Goals'
plt.show()

#v) Histogram
plt.figure(figsize=(10, 6))
df['Away Team Goals'].hist(bins=20)
plt.title("hitogram")
plt.show()

#vi) Distribution Plot
plt.figure(figsize=(10, 6))
sns.displot(df['Home Team Goals'])
plt.title("distribution plot")
plt.show()

#vii) Scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Home Team Goals', y='Away Team Goals', data=df)
plt.title("scattter plot")
plt.show()
