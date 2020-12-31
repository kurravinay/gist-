import pandas as pd
def write_parquet_file():
    df = pd.read_csv('username-password-recovery-code.csv')
    df.to_parquet('username-password-recovery-code.parquet')
write_parquet_file()
