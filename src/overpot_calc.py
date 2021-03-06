""" This script calculates the pitting overpotential for each experiment"""

import pandas as pd

d = pd.read_csv("../data/corrpit.csv", sep="\t")

ec, ep = list(d.columns)[-2:]

d["npit_mV"] = d[ep] - d[ec]

with open("../results/corrpitover.csv", "w", newline='') as f:
    d.to_csv(f, sep='\t', index=False)
