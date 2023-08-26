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

num_test = 23 #number of tests conducted on a sample determines the number of files
sample = 'X-116-F'
path_save = "/Users/jessicawen/Documents/VSCode/Python/QtzIndent/data/X-116-F/tests/figures/" #copy path

for p in plot: 
    label = []
    for n in range(num_test):
        #if n != 11: #remove the outlier test by n = test# - 1
        #if n != 18 and n != 7 and n != 1:
            #filename = 'basic_test.CSV'
            filename = sample + '_Test' + str(n+1) + '.CSV'
            #df = pd.read_csv(filename) #read file to get the first row that contatins units
            #units = df.iloc[0] #this is a dicionary that contains units
            df = pd.read_csv(filename, skiprows=[1])
            sns.scatterplot(data = df, x = 'LOAD', y = p, s= 1, color = color[n])
            label.append("Test #" +str(n+1))
    
    if p == 'MODULUS':
        plt.xlabel("Load [nM]")
        plt.ylabel("Modulus [GPa]")
        plt.legend(label, loc = 2, bbox_to_anchor = (1,1), markerscale=5, fontsize = 5)
        plt.title(sample + ": Load vs. Modulus")
        plt.ylim(0, 140)
        fig_name = path_save + "alltest_modulus_fig.png"

        plt.show() #pick either show or save
        #plt.savefig(fig_name, format="png", bbox_inches='tight', dpi=200)
        #plt.show() #need this when using savefig to override error
  
    elif p == 'HARDNESS':
        plt.xlabel("Load [nM]")
        plt.ylabel("Hardness [GPa]")
        plt.legend(label, loc = 2, bbox_to_anchor = (1,1), markerscale=5, fontsize = 5)
        plt.title(sample + ": Load vs. Hardness")
        plt.ylim(0, 20)
        fig_name = path_save + "alltests_hardness_fig.png"

        plt.show() #pick either show or save
        #plt.savefig(fig_name, format="png", bbox_inches='tight', dpi=200)
