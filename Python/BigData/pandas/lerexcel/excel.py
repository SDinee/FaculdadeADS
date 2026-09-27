import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

diretorio = os.getenv("DIRETORIO")

vendas = pd.read_excel(diretorio + "vendas.xlsx")

print(vendas)