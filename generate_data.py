import pandas as pd
import random
import numpy as np

id_1 = 8177  # change to first student id
id_2 = 8179  # change to second student id
id_3 = 8211  # change to third student id "leave 0000 if team of 2"
random_seed = id_1 + id_2 + id_3
random.seed(random_seed)

data_path = r"Data.csv"
output_path = r"your_data.csv"

# Load the dataset
all_data = pd.read_csv(data_path) 
all_columns = all_data.columns.tolist()

target_column = 'smoking'  
all_columns.remove(target_column)
selected_columns = random.sample(all_columns, 12)

selected_columns += [ target_column]
print(selected_columns)
sample_df = all_data[selected_columns].copy()

sample_df.to_csv(output_path, index=False)  


