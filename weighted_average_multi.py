'''
    Jessica Wen
    June 29, 2022
     
     To run: change lines, 13, 14, 22 (if needed), 42, 43, 48
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plot = ['MODULUS', 'HARDNESS']
color = ['red', 'orange', 'blue', 'green', 'purple', 'cyan', 'maroon', 'limegreen', 'royalblue', 
            'gold', 'tomato', 'plum', 'peru', 'crimson', 'chocolate', 'teal', 'wheat', 'deeppink', 
            'lawngreen', 'orchid', 'fuchsia', 'sienna', 'olivedrab', 'powderblue', 'indigo', 'wheat',
            'greenyellow', 'sienna', 'forestgreen', 'lightblue', 'seagreen', 'lavender', 'plum', 
            'darkmagenta', 'darkslateblue', 'thistle', 'pink', 'slategrey', 'lime', 'orangered']

num_test = 10 #number of tests conducted on a sample determines the number of files
f_name = 'wavg_alltests_X-125-K_600_r'
path_save = "/Users/jessicawen/Documents/VSCode/Python/QtzIndent/data/rotate_600_adj/figures/" #copy path

for p in plot: 
    label = []
    color_count = 0
    for n in range(0, num_test * 10, 10):
        if p == 'MODULUS':
            filename = f_name + str(n) + '_mod.csv'
        elif p == 'HARDNESS': 
            filename = f_name + str(n) + '_hard.csv'
        df = pd.read_csv(filename, skiprows=[1])
        sns.lineplot(data = df, x = 'LOAD', y = p, color = color[color_count], estimator = 'max')
        label.append(str(n) + ' degrees')
        color_count += 1
    
    if p == 'MODULUS':
        plt.xlabel("Load [nM]")
        plt.ylabel("Modulus [GPa]")
        plt.legend(label, loc = 2, bbox_to_anchor = (1,1), markerscale=5, fontsize = 5)
        plt.title('X_125-K Rotation' + ": Load vs. Modulus")
        plt.ylim(0, 150)
        fig_name = path_save + "comp_rot_modulus_fig2.png"

        #plt.show() #pick either show or save
        #plt.savefig(fig_name, format="png", bbox_inches='tight', dpi=200)
        plt.show() #need this when using savefig to override error
  
    elif p == 'HARDNESS':
        plt.xlabel("Load [nM]")
        plt.ylabel("Hardness [GPa]")
        plt.legend(label, loc = 2, bbox_to_anchor = (1,1), markerscale=5, fontsize = 5)
        plt.title('X_125-K Rotation' + ": Load vs. Hardness")
        plt.ylim(0, 20)
        fig_name = path_save + "comp_rot_hardness_fig2.png"

        plt.show() #pick either show or save
        #plt.savefig(fig_name, format="png", bbox_inches='tight', dpi=200)
