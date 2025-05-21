import os
import sys
import glob
import subprocess
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Phylo

# Store the path to the directory containing .fasta files
in_dir="/shared/forsythe/BB485/Week06/Brass_CDS_seqs/"

# Store the path to a new folder where we want to write the output
out_dir="/scratch/bella7/BellBB485/Week06/PhylogeneticsPipeline_OUT/"

# Get a list of all .fasta files in path
in_fullpath = glob.glob(in_dir+"*.fasta")

# Start a for loop to loop throuh each file name:
### Remove index on in_fullpath

for file in in_fullpath:
    new_file_path = file.replace(in_dir, out_dir)
    aln_cmd = 'mafft --auto --quiet '+file+' > '+new_file_path
    print(aln_cmd)
    os.system(aln_cmd)

#sys.exit()

out_fullpath = glob.glob(out_dir+"*.fasta")

# Start a for loop to infer iqtree
for file in out_fullpath:
    tree_command = f"iqtree -s {file} -m TEST -nt 24"
    print(tree_command)
    os.system(tree_command)
# 24 nodes
### Remove index on in_fullpath

#for file in in_fullpath[1:5]:

    # Loop through alligned .fast files and run iqtree on each

