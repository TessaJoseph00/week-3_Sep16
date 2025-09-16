import pandas as pd
import numpy as np

#1.
def fib(n):
    """
    Return the nth Fibonacci number using recursion.
    The sequence starts with 0 and 1, and each number is the sum 
    of the two numbers before it.
    Parameters:
        n (int): Position in the Fibonacci sequence 
    Returns:
        int: The nth Fibonacci number.
    """
    # Base case: first number is 0
    if n == 0:
        return 0
    # Base case: second number is 1
    elif n == 1:
        return 1
    # Recursive case: sum of the two previous numbers
    else:
        return fib(n - 1) + fib(n - 2)
print("\n1. ")
print("n=5 ->",fib(5))
print("n=9 ->",fib(9))

#2.
def to_binary(n):
    """
    Convert an integer to its binary representation using recursion.
    Parameters:
        n (int): Non-negative integer to convert.
    Returns:
        str: Binary representation of n.
    """
    # Base cases
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    # Recursive step: binary of quotient + remainder
    return to_binary(n // 2) + str(n % 2)

print("\n2. ")
print("n=2  ->",to_binary(2)) 
print("n=12 ->",to_binary(12))

#3a.
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

def task_1():
    """
    Returns a list of all column names sorted by missing values  
    Removing whitespaces and convert into lowercase for gender column
    """
    
    #Removing whitespaces and convert into lowercase for gender
    df_bellevue['gender'] = df_bellevue['gender'].str.lower().str.strip()
    
    # Count missing values in each column and sort
    sorted_columns = df_bellevue.isnull().sum().sort_values()
    
    # Print missing values count in each column
    print("\n3a. Missing values per column:")
    print(sorted_columns)
    
    # Return list of column names in order of missing values
    return sorted_columns.index.tolist()

column_list = task_1()
print("\nList of columns sorted by missing values:", column_list)

#3b.
def task_2():
    """
    Returns a dataframe with two columns:
    - year: the year of each entry
    - total_admissions: total number of entries (immigrant admissions) for that year
    """
    # Ensure date_in is a datetime column
    df_bellevue['date_in'] = pd.to_datetime(df_bellevue['date_in'])
    
    # Extract year from date_in
    df_bellevue['year'] = df_bellevue['date_in'].dt.year
    
    # Group by year and count entries
    total_admissions = df_bellevue.groupby('year').size().reset_index(name='total_admissions')
  
    print("\n3b.")
    print(total_admissions)
    
    return total_admissions

df_yearly = task_2()

#3c.
def task_3():
    """
    Returns a series with
    Index: gender (m or w), 
    Values: average age for each gender
    """
    #Removing whitespaces and convert into lowercase for gender
    df_bellevue['gender'] = df_bellevue['gender'].str.lower().str.strip()
    
    # Group by gender and calculate average age
    mean_age_gender = df_bellevue.groupby('gender')['age'].mean()
    
    # Filter only valid genders
    mean_age_gender = mean_age_gender[mean_age_gender.index.isin(['m', 'w'])]
    
    
    print("\n3c.")
    print(mean_age_gender)
    
    return mean_age_gender

gender_avg_age = task_3()

#3d.
def task_4():
    """
    Returns the 5 most common professions in order of prevalence
    """
    # Checking for missing or blank values
    if df_bellevue['profession'].isnull().any() or (df_bellevue['profession'].str.strip() == '').any():
        print("Some profession entries are missing or blank")

    #Removing whitespaces and convert into lowercase for profession column
    df_bellevue.loc[:, 'profession'] = df_bellevue['profession'].str.strip().str.lower()

    # Getting the count of each profession
    top_5_professions = df_bellevue['profession'].value_counts().head(5).index.tolist()

    return top_5_professions
    
print("\n3d.")
print("Top 5 professions:", task_4())