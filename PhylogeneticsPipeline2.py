import os
import sys
import glob
import subprocess
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Phylo

in_dir="/scratch/bella7/BellBB485/Week06/PhylogeneticsPipeline_OUT/"

in_fullpath = glob.glob(in_dir+"*.treefile")

counter12=0
counter13=0
counter23=0
unknown=0

#Read in the tree and store as phylo object
for tree in in_fullpath:
    temp_tree = Phylo.read(tree, "newick")
    #print(temp_tree)


#Loop through the tips in the tree to find which one contains Es (the outgroup)
    for tip in temp_tree.get_terminals():
        if "Es_" in tip.name:
            es_tip = tip
            #Stop the loop once we found the correct tip
            break

    #Root the tree by the outgroup taxon
    temp_tree.root_with_outgroup(es_tip)
        
    #Get a list of all terminal (aka tips) branches
    all_terminal_branches = temp_tree.get_terminals()


    #Loop through the branches and store the names of the tips of each
    for t in all_terminal_branches:
        if "Bs_" in t.name:
            Bs_temp=t
        elif "Cr_" in t.name:
            Cr_temp=t
        elif "At_" in t.name:
            At_temp=t
        else:
            out_temp=t

    #Make lists of pairs of branches, so that we can ask which is monophyletic
    P1_and_P2=[Bs_temp, Cr_temp]
    P1_and_P3=[Bs_temp, At_temp]
    P2_and_P3=[Cr_temp, At_temp]
        

    #Use series of if/else statements to ask which pair in monophyletic
    if bool(temp_tree.is_monophyletic(P1_and_P2)):
        counter12+=1
    elif bool(temp_tree.is_monophyletic(P1_and_P3)):
        counter13+=1
    elif bool(temp_tree.is_monophyletic(P2_and_P3)):
        counter23+=1
    else:
        unknown+=1

print(f"B. str and C. rub sister: {counter12}")
print(f"A. tha and B. str sister: {counter13}")
print(f"A. tha and C. rub sister: {counter23}")
print(f"Unknown topologies: {unknown}")
