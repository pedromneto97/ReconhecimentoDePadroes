# python feature_extraction.py --image_dir ./imagens/ --output_labels=labels.txt --features ./saida.csv

import pandas as pd

s = ''

for i in range(2048):
    s += str(i) + ","

s += "class\n"

with open('saida2.csv', 'w') as f:
    f.write(s)
    with open('saida.csv', 'r') as arq:
        f.write(arq.read())

df2 = pd.read_csv('saida2.csv')
print(df2.head())
