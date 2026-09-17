import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

diretorio = os.getenv("DIRETORIO")

alunos = pd.read_csv(diretorio + "alunos.txt", sep =";")

print(alunos)