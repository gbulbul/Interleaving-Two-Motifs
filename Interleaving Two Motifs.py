# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 00:53:11 2024

@author: gbulb
"""

class find_supersequence:
    def find_superstring(string1,string2):
        STRING_nonmatches=''
        for i in range(len(string2)):    
            if string1[i+1]==string2[i]:
               STRING_nonmatches+=string1[:i+2] #AT    
               if string1[i+3:]!=string2[i+1:]:
                    STRING_nonmatches+=string2[i+1:]+''+string1[i+4:] #GCATAGAT
                    return print(STRING_nonmatches) 
       
if __name__=="__main__":
    string1='ATCTGAT'
    string2='TGCATA'
    find_supersequence.find_superstring(string1,string2)

       
            
    