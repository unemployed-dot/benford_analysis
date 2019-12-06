"""
Created on Thu Dec  5 12:44:54 2019

@author: Unemployed
"""

import sys
import math
from collections import defaultdict
import matplotlib.pyplot as plt

#Collection module provides specialized alternatives to Python containers, 
#will be used to create a dictionary in which we will insert the first digits
#Benford's law percentages for leading digit 1-9

#Defaultdict create a dictionary with the first digit

#BENFORD array contains the percentage that every first digit from 1 to 9 has

BENFORD=[30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

def load_data(filename):
    """Open a text file and return a list of strings"""

#With function open and clode filename

    with open(filename) as f:
        return f.read().strip().split('\n')

#Counting first digit

def count_first_digits(data_list):
    
    #data_list is the string returned from load_data function
    
    first_digits=defaultdict(int) #default value of int is 0
    
    #In first_digits we will create a dictionary.
    
    for sample in data_list:
        #IMO if cycle controls that the text file is not empty, then we try to 
        #convert what is in the file using int() command.
        if sample=="":
            continue
        try:
            int(sample)
        except ValueError as e:
            print(e, file=sys.stderr)
            print("Samples must be integers. Exiting", file=sys.stderr)
            sys.exit(1)
        first_digits[sample[0]]+=1
        
        #data_cout can order the element in first_digits string
        
    data_count=[v for (k,v) in sorted(first_digits.items())]
    total_count=sum(data_count)
    
    #data_count orders values based on the keys.
    
    data_pct=[(i/total_count)*100 for i in data_count]
    return data_count, data_pct, total_count

def get_expected_counts(total_count):
    return[round(p*total_count)/100 for p in BENFORD]
    
def chi_square_test(data_count, expected_count):
    chi_square_stat=0
    #Zip function create a dictionary using data_count elements as keys and 
    #expected_data as values of the dictionary
    for data, expected in zip(data_count, expected_count):
        chi_square=math.pow(data-expected, 2)
        chi_square_stat+= chi_square/expected
    print("\nChi Squared Test Statistic: {:.3f}".format(chi_square_stat))
    print("Critical value at P-value of 0.05 is 15,51")
    
    return chi_square_stat < 15.51

def bar_chart(data_pct):
    fig, ax=plt.subplots()
    
    index=[i+1 for i in range(len(data_pct))]
    
    fig.canvas.set_window_title('Percentage First Digits')
    ax.set_title('Data vs Benford Values',fontsize=15)
    ax.set_ylabel('Frequency (%)', fontsize=16)
    ax.set_xticks(index)
    ax.set_xticklabels(index, fontsize=14)
    
    rects=ax.bar(index, data_pct, width=0.95, color='black',label='Data')
    
    for rect in rects:
        height=rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2,height,'{:0.1f}'.format(height),ha='center',va='bottom', fontsize=13)
        
        ax.scatter(index, BENFORD, s=150, c='red',zorder=2,label='Benford')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.legend(prop={'size':15}, frameon=False)

        plt.show()
        
def main():
    while True:
        filename=input("\nName of file with COUNT data: ")
        try:
            data_list=load_data(filename)
        except IOError as e:
            print("{}. Try again.".format(e), file=sys.stderr)
        else:
            break
    data_count, data_pct, total_count=count_first_digits(data_list)
    expected_counts=get_expected_counts(total_count)
    print("\nobserved counts ={}".format(expected_counts),"\n")
    
    print("First Digit Probabilities:")
    for i in range(1,10):
        print("{}: observed: {:.3f} expected: {:.3f}".
              format(i, data_pct[i-1]/100,BENFORD[i-1]/100))
    if chi_square_test(data_count, expected_counts):
        print("Observed distributions matches expected distributions")
    else:
        print("Observed distributions does not match expected", file=sys.stderr)
    bar_chart(data_pct)
    
    
if __name__=='__main__':
    main()
