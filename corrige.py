# python feature_extraction.py --image_dir ./imagens/ --output_labels=labels.txt --features ./saida.csv

import argparse
from os.path import splitext

import pandas as pd


def corrige(arquivo: str):
    arq = splitext(arquivo)
    if arq[1] != '.csv':
        print("O arquivo não é um .csv")
        return

    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        print("Arquivo inexistente!")

    s = ''
    for i in range(len(df.columns) - 1):
        s += str(i) + ","
    s += "class\n"
    novo_nome = arq[0] + '_corrigido' + arq[1]
    with open(novo_nome, 'w') as f:
        f.write(s)
        with open(arquivo, 'r') as arq:
            f.write(arq.read())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--csv',
        type=str,
        default='saida.csv',
        help='Arquivo de saída do feature_extraction'
    )
    FLAGS, unparsed = parser.parse_known_args()
    corrige(FLAGS.csv)
