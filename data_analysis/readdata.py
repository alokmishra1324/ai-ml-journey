import pandas as pd

from io import StringIO

Data = '{"employee_name" : "James" , "email" : "james@email.com" , "job_profile" : [{"title1" : "Team Lead" , "title2" : "Sr. Developer"}]}'
string_df = pd.read_json(StringIO(Data))
print(string_df)


json_data = string_df.to_json()
print(json_data)

json_ind_data = string_df.to_json(orient='index')
print(json_ind_data)

json_records = string_df.to_json(orient='records')
print(json_records)

df = pd.read_csv("wine.csv")
print(df.head())

df.to_csv("wine2.csv")

url = "https://www.fdic.gov/bank-failures/failed-bank-list"
df2 = pd.read_html(url)
print(df2[0])

url1 =  "https://en.wikipedia.org/wiki/Mobile_country_code"


# df3 = pd.read_html(url1 , match = "Country" , header=0 )

df4 = pd.read_excel('sample_data.xlsx')
print(df4)

df4.to_pickle(df4)

pd.read_pickle(df4)
