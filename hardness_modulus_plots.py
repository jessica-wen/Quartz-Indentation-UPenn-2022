""" Jessica Wen
    June 20, 2022
    Water Content in Quartz Indentation, RORD, UPenn
    Plots load vs modulus and load vs hardness as two different figures on one png file
    To start, change directory to the folder containing the test csv files
    Need to change lines 14, 17 and 66 for each sample
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

num_test = 25 #number of tests conducted on a sample determines the number of files
for n in range(num_test):
    #filename = 'X-41_F_test3_Test1.CSV' #for one file
    sample = 'X-116-F'
    filename = sample + '_Test' + str(n+1) + '.CSV'
    df = pd.read_csv(filename) #read file to get the first row that contatins units
    units = df.iloc[0] #this is a dicionary that contains units

    df = pd.read_csv(filename, skiprows=[1]) #read to skip unit row
    
    #contains the data that will be plotted
    modulus = df['MODULUS'] 
    hardness = df['HARDNESS']
    load = df['LOAD']

    #units for the above measurements
    modulus_unit = units['MODULUS']
    hardness_unit = units['HARDNESS']
    load_unit = units['LOAD']

    fig, ax = plt.subplots(2, figsize=(10, 6))
    title = sample + ": Load vs Modulus and Hardness"
    ax[0].title.set_text(title)

    #plot 1: load vs modulus
    x_1 = load
    y_1 = modulus
    color_1 = 'blue'
    variable_1 = "Modulus"
    ax[0].scatter(x_1, y_1, c = color_1, s = 1, label = variable_1)

    #plot 2: load vs hardness
    y_2 = hardness
    color_2 = 'orange'
    variable_2 = 'Hardness'
    ax[1].scatter(x_1, y_2, c = color_2, s = 1, label = variable_2)
    #title_2 = sample + ": Load vs Hardness"
    #ax[1].title.set_text(title_2)

    x_label = "Load (" + load_unit + ")"
    y1_label = "Modulus (" + modulus_unit + ")"
    y2_label = "Hardness (" + hardness_unit + ")"

    ax[0].set_xlabel(x_label)
    ax[0].set_ylabel(y1_label)
    ax[1].set_xlabel(x_label)
    ax[1].set_ylabel(y2_label)

    #plt.tight_layout()
    #plt.title(title) #figure how to show at top of image
    #plt.legend(loc = 'upper right')
    #plt.show()

    #save figures as png and put in folder called figures
    file = filename[:-4] #remove .csv
    path_save = "/Users/jessicawen/Documents/VSCode/Python/QtzIndent/data/X-116-F/tests/figures/" #copy path
    fig_name = path_save + file + "_figure.png"
    plt.savefig(fig_name, format="png", bbox_inches='tight', dpi=200)
    
    print("done" + str(n+1))