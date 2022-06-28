import pandas as pd
import plotly.express as px

xlsx = pd.ExcelFile('names.xlsx')
df = pd.read_excel(xlsx, 'Sheet6')

#print (df)

names = list(df.iloc[:, 0])
print (names)
years = list(df.head().columns)
years.remove('Year')
print (years)

import itertools

example = pd.DataFrame(list(itertools.product(names,years)), columns=['Names','Years'])
example["Rank"] = ""
example["Gender"] = ""
l = 0

for i in (names):
    for j in (years):
        if i in ['Olivia', 'Emma', 'Charlotte', 'Amelia', 'Ava', 'Sophia', 'Isabella', 'Emily', 'Madison', 'Abigail', 
             'Hannah', 'Alexis', 'Ashley', 'Alexis', 'Ashley', 'Sarah', 'Samantha', 'Jessica', 'Amanda', 'Brittany', 
             'Jennifer', 'Melissa', 'Amy', 'Heather', 'Angela', 'Michelle', 'Kimberly', 'Lisa', 'Mary', 'Susan',
             'Karen', 'Patricia', 'Linda', 'Donna', 'Debra', 'Deborah', 'Barbara', 'Sandra', 'Carol', 'Judith', 'Betty',
             'Shirley', 'Dorothy', 'Joan', 'Helen', 'Margaret', 'Ruth']:
            gender = "Female"
        else:
            gender = "Male"
        example.at[l, 'Gender']=gender
        example.at[l, 'Rank']=df.iloc[names.index(i),years.index(j)+1]
        l+=1
print (example)
example = example.loc[example["Rank"] != 6]
example = example.sort_values(by = ['Gender', 'Years'], ascending = [True, False])
print (example)

fig = px.histogram(example, x=example.Names, y=example.Rank, animation_frame=example.Years, range_y=[0,6],
                   color="Gender")
fig.write_html("fig.html")
