'''
    Jessica Wen
    June 29, 2022
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plot = ['MODULUS', 'HARDNESS']
color_list = ['red', 'orange', 'blue', 'green', 'purple', 'cyan', 'maroon', 'limegreen', 'royalblue', 
                'gold', 'tomato', 'plum', 'peru', 'crimson', 'chocolate', 'teal', 'wheat', 'deeppink', 
                'lawngreen', 'orchid', 'fuchsia', 'sienna', 'olivedrab', 'aqua', 'indigo']


samples_and_rm = {'X-41-L': [2, 3, 11],
           'X-41_L_rot30': [2, 3, 6, 7]}
num_test = [25, 25]
path_save = "/Users/jessicawen/Documents/VSCode/Python/QtzIndent/data/X-41-L_rotate/figures/" #copy path

samples = list(samples_and_rm.keys())

for p in plot:
    label = []
    for s in samples: #s = the sample name
        n_test = num_test[int(samples.index(s))]
        c = color_list[int(samples.index(s))]
        rm = samples_and_rm.get(s)
        for n in range(n_test):
            if n + 1 not in rm:
                filename = s + '_Test' + str(n+1) + '.CSV'
                df = pd.read_csv(filename, skiprows=[1])
                sns.scatterplot(data = df, x = 'LOAD', y = p, s= 1, color = c)
                label.append(filename[:-4])
    
    if p == 'MODULUS':
        plt.xlabel("Load [nM]")
        plt.ylabel("Modulus [GPa]")
        plt.legend(label, loc = 2, bbox_to_anchor = (1,1), markerscale=5, fontsize = 5)
        plt.title("Load vs. Modulus")
        #fig_name = path_save + "X-41-L_rotatecompare_modulus_fig.png"

        plt.show() #pick either show or save
        #plt.savefig(fig_name, format="png", bbox_inches='tight', dpi=200)
        #plt.show() #need this when using savefig to override error
    
    elif p == 'HARDNESS':
        plt.xlabel("Load [nM]")
        plt.ylabel("Hardness [GPa]")
        plt.legend(label, loc = 2, bbox_to_anchor = (1,1), markerscale=5, fontsize = 5)
        plt.title("Load vs. Hardness")
        fig_name = path_save + "X-41-L_rotatecompare_hardness_fig.png"

        plt.show() #pick either show or save
        #plt.savefig(fig_name, format="png", bbox_inches='tight', dpi=200)
