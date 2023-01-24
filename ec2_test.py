
import pandas as pd
import random

print("Starting...")
# Create a random pandas dataframe
df = pd.DataFrame({"A": [random.randint(0,100) for i in range(10)],
                  "B": [random.randint(0,100) for i in range(10)],
                  "C": [random.randint(0,100) for i in range(10)]})
print(df)
# Save the dataframe as a csv file
#df.to_csv('output.csv', index=False)
df.to_csv('s3://sim-project/Project_0001/output/output.csv', index=False)
print("File saved successfully")
