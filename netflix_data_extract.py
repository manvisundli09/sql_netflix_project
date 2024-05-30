import pandas as pd 
import sqlalchemy as sal

# Load data into a DataFrame
df = pd.read_csv('netflix_titles.csv')

# MySQL Connection
engine = sal.create_engine('mysql://root:mysql@sqlproject/sqlproj')

# Establish connection
conn = engine.connect()

# Write DataFrame to MySQL
df.to_sql('netflix_raw', con=conn , index=False, if_exists='append')

# Close connection
conn.close()

# Display DataFrame
print(df.head())

# Filter DataFrame by show_id
print(df[df['show_id'] == 's5023'])

# Find maximum length of descriptions
print(max(df['description'].dropna().str.len()))

# Find NaN values count
print(df.isna().sum())
