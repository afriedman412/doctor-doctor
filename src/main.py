from setup import analyzer

path = "cary_testo.pdf"  # Use the PDF in the sample folder
df = analyzer.analyze(path=path)
df.reset_state()
dp = next(iter(df))

new_table = dp.tables[0].csv
with open("new_table.csv") as f:
    f.write(new_table)
