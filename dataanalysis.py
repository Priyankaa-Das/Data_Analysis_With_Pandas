import pandas as pd
import matplotlib as plt

df = pd.read_csv('data.csv')

print(df.head())                                                    #Display the first few rows of the dataframe
print(df.tail())                                                    #Display the last few rows of the dataframe

print(df.describe())                                                #Describe each data,get descriptive statistics for all numerical column

mv=df.isnull().sum()                                                #find missing values in each column
print("Missing values in each coulmn:\n",mv)                       

avg=df['Age'].mean()                                                #calculating the average of a column
print(f"Average of age:{avg}")

uv = df['Age'].nunique()                                            #counts the unique values
print(f"unique values:{uv}")

eng_emp = df[df['Department'] == 'Engineering']                     #filters the rows based on condition,eg.filter all employees from engineering Department
print(eng_emp)

max_salary = df['Salary'].max()                                     #finds the maximum salary
max_salary_emp=df[df['Salary'] == max_salary]
print("Highest paid employee:\n",max_salary_emp)                    #find the employee with the highest salary

min_salary = df['Salary'].min()                                     #finds the minimum salary
min_salary_emp = df[df['Salary'] == min_salary]
print("Employee(s) with the minimum salary:\n", min_salary_emp)

dep_count = df['Department'].value_counts()                         #count frequency from each value
print("Number of employees in each department: \n",dep_count)

sort = df.sort_values(by='Age',ascending=False)                     #sort the data by column in descending order
print("Senior to junior employee:\n",sort)       

sort = df.sort_values(by='Age', ascending=True)                     # Sort the data by column in ascending order
print("Junior to senior employee:\n", sort)

df['Experience'] = df['Age'].apply(lambda x: 'Senior' if x >= 30 else 'Junior')     #adds a new column
print("Data with Experience column:\n",df)

#data visualization
#plotting a pie chart
plt.figure(figsize=(8,6))                                                          
plt.pie(dep_count,labels=dep_count.index,autopct='%1.1f%%',startangle=140)
plt.title('Department Distribution')
plt.show()

#plotting a bar chart
plt.figure(figsize=(8, 6))  
plt.bar(dep_count.index, dep_count.values, color='skyblue', edgecolor='black')
plt.xlabel('Departments')                               
plt.ylabel('Number of Employees')
plt.title('Department Distribution')
plt.show()
