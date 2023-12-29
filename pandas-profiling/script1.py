import pandas as pd
from ydata_profiling import ProfileReport
df = pd.read_csv('train.csv')
prof = ProfileReport(df)
prof.to_file(output_file = 'output.html')
