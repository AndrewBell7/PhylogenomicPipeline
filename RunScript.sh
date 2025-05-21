#!/bin/bash
#SBATCH --job-name=PhylogeneticsPipeline
#SBATCH --ntasks-per-node=24
#SBATCH --time=24:0:0
#SBATCH --output=PhylogeneticsPipeline.out
#SBATCH --error=PhylogeneticsPipeline.err
#SBATCH --mail-user=bella7@oregonstate.edu
#SBATCH --mail-type=END

python PhylogeneticsPipeline.py