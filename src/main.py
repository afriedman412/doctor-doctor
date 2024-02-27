from setup import analyzer
import pandas as pd

path = "src/pdf/cary_testo.pdf"  # Use the PDF in the sample folder
df = analyzer.analyze(path=path)
df.reset_state()
dp = next(iter(df))

new_table = dp.tables[0].csv
pd.DataFrame(new_table).to_csv("new_table.csv")
# with open("new_table.csv", "a+") as f:
#     f.write(new_table)
