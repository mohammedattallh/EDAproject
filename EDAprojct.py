import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import sqlite3 


def load_dataset(data_path):
    if data_path.endswith('.csv'):
      
        data = pd.read_csv(data_path)
        return data
    elif data_path.endswith('.xlsx') or data_path.endswith('.xls'):
       
        data = pd.read_excel(data_path)
        return  data
    elif data_path.endswith('.db') or data_path.endswith('.sqlite') or data_path.endswith('.db3'):
        query_table = input(' please enter your table ')
       
        conn = sqlite3.connect(data_path)
        query = f'SELECT * FROM {query_table}'
        data = pd.read_sql(query, conn)
        return data
    else:
        raise ValueError('Unsupported file format.')


def dimensions_data(data ):
    rowstr,rowend  = int(input('enter order  rows : '))    
    data = data.loc[rowstr,rowend]
    while True :
        try:
            colstr ,colend = int(input('enter index  columns : '))
            data = data.iloc[colstr:colend] 
        except ValueError:
               print('please enter index columns')
        else:
            break

def preprocess_data(data):
  
        for column in data.columns:
             column1 = str(column)
             if data[column1].isna().sum() > 0:
                 print(f'column {column1} include {data[column1].isna().sum()} null')
                 null_answer = input('do you want to drop or fill null : ')
                 if null_answer == 'drop':
                      data = data.dropna()
                      return data
                      
                 elif null_answer == 'fill':
                      data[column1] = data[column1].fillna(data[column1].mean()) 
                      return data
                 else:
                      print('please enter fill or drop ')
            

def generate_visualizations(data):
     for column in data.columns:
        column2 = str(column)
        if data[column2].dtype == 'object':
            print(f'{column2} is object')
            plot = input ('please enter  bar or pie : ')
           
            figs1= int(input(('please enter dimensions figure : ')))
            figs2= int(input(('please enter dimensions figure : ')))
            plt.figure(figsize=(figs1,figs2))
            data[column2].value_counts().plot(kind=plot)
            plt.title(f'Countplot of {column}')
            plt.show()

        if data[column2].dtype == 'float64':
            print(f'{column2} is float')
            plot = input ('please enter hist or pie or bar : ')
            
            figs3= int(input('please enter dimensions figure : '))
            figs4= int(input('please enter dimensions figure : '))
            plt.figure(figsize=(figs3,figs4))
            data[column2].value_counts().plot(kind=plot)
            plt.title(f'Countplot of {column}')
            plt.show()
            
        if data[column2].dtype == 'int64':
            print(f'{column2} is int ')
            plot = input ('please enter hist or pie or bar  : ')
            figs5= int(input('please enter dimensions figure : '))
            figs6= int(input('please enter dimensions figure : '))
            plt.figure(figsize=(figs5,figs6))
            data[column2].value_counts().plot(kind=plot)
            plt.title(f'Countplot of {column}')
            plt.show()    
            
        

data_path = input('please enter path dataset : ')

load_dataset= load_dataset(data_path)
dimensions_data=  dimensions_data( load_dataset)

preprocess_data=preprocess_data( dimensions_data)

generate_visualizations(preprocess_data)








