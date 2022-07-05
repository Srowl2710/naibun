import numpy as np
import itertools as it
import pandas as pd

#データの読み込み
csv_input = pd.read_csv(filepath_or_buffer="../data/温度0℃/210922A_soc100_t0.csv")
print(csv_input.size)