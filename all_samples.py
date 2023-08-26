'''
    Jessica Wen
    June 29, 2022
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# samples = ['X-41_F_test3', 'X-41_L_rot30', 'X-41-L', 'X-116_A_rot30', 'X-116-A',
#             'X-116-F', 'X-116-F_test2', 'X-116-F_test3', 'X-125-J', 'X-125-J_rotated40',
#             'X-125-K', 'X-125-L']
# num_test = [20, 25, 25, 25, 25, 25, 25, 10, 25, 25, 25, 25] 

samples = ['X-41_F_test3', 'X-41_L_rot30', 'X-41-L', 'X-116_A_rot30', 'X-116-A',
           'X-116-F_test2', 'X-116-F_test3', 'X-125-J', 'X-125-J_rotated40',
           'X-125-K', 'X-125-L']
num_test = [20, 25, 25, 25, 25, 25, 10, 25, 25, 25, 25]

color_list = ['red', 'orange', 'blue', 'green', 'purple', 'cyan', 'maroon', 'olive', 
              'royalblue', 'gold', 'tomato', 'plum', 'peru', 'crimson', 'chocolate', 'teal', 'wheat', 
              'deeppink', 'lawngreen', 'orchid', 'fuchsia', 'sienna', 'limegreen', 'powderblue', 'indigo']

plot = ['MODULUS', 'HARDNESS']
path_save = "/Users/jessicawen/Documents/VSCode/Python/QtzIndent/data/all_test/figures/" #copy path
label = []

for p in plot: 
  for s in samples: #s = the sample name
      n_test = num_test[int(samples.index(s))]
      c = color_list[int(samples.index(s))]
      for n in range(n_test):
          filename = s + '_Test' + str(n+1) + '.CSV'
          df = pd.read_csv(filename, skiprows=[1])
          sns.scatterplot(data = df, x = 'LOAD', y = p, s= 1, color = c)
          label.append(s)
  if p == 'MODULUS':
    plt.xlabel("Load [nM]")
    plt.ylabel("Modulus [GPa]")
    plt.legend(label, loc = 2, bbox_to_anchor = (1,1), markerscale=5, fontsize = 5)
    plt.title("Load vs. Modulus")
    fig_name = path_save + "allsamples_modulus_fig.png"

    plt.show() #pick either show or save
    #plt.savefig(fig_name, format="png", bbox_inches='tight', dpi=200)
  
  elif p == 'HARDNESS':
    plt.xlabel("Load [nM]")
    plt.ylabel("Hardness [GPa]")
    plt.legend(label, loc = 2, bbox_to_anchor = (1,1), markerscale=5, fontsize = 5)
    plt.title("Load vs. Hardness")
    fig_name = path_save + "allsamples_hardness_fig.png"

    plt.show() #pick either show or save
    #plt.savefig(fig_name, format="png", bbox_inches='tight', dpi=200)