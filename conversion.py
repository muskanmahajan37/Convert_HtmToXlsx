
# Importing pandas 
import pandas as pd 
# Importing os module
import os

  
path=os.getcwd()  
  
# The webpage URL whose table we want to extract 
url = f"{path}\\SQLAExport.htm"
  
# Assign the table data to a Pandas dataframe 
table = pd.read_html(url)[0] 
  
# Store the dataframe in Excel file 
table.to_excel(f"{path}\\data.xlsx") 



