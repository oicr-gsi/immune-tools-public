#! /usr/bin/env python3

import csv
import os
import sys

# Check status of SWISNF genes for CAPTIV-8
# Conservative check; any non-silent mutation is flagged as potential LOF

if len(sys.argv)!=2:
    print("Usage: evaluate_swisnf.py $PATH_TO_DJERBA_REPORT_DIR")
    sys.exit(1)

report_dir = sys.argv[1]
cna_path = os.path.join(report_dir, 'data_CNA.txt')
mut_path = os.path.join(report_dir, 'data_mutations_extended.txt')
if not (os.access(cna_path, os.R_OK) and os.access(mut_path, os.R_OK)):
    print("Expected files data_CNA.txt and data_mutations_extended.txt not readable, check input directory")
    sys.exit(1)

genes = ['SMARCB1', 'SMARCA4', 'ARID1A', 'ARID1B', 'PBRM1']
potential_lof = False

print("Evaluating {0}... ".format(cna_path))
with open(cna_path) as cna_file:
    reader = csv.reader(cna_file, delimiter="\t")
    first = True
    for row in reader:
        if first:
            first = False
            continue
        gene = row[0]
        status = int(row[1])
        if gene in genes and status <= -2:
            print("Deletion of {0}: {1}".format(gene, status))
            potential_lof = True
print("done.")

print("Evaluating {0}... ".format(mut_path))
with open(mut_path) as mut_file:
    reader = csv.reader(mut_file, delimiter="\t")
    first = True
    for	row in	reader:
        if first:
            first = False
            continue
    gene = row[0]
    var_class = row[8]
    if gene in genes and var_class != 'Silent':
        print("Non-silent mutation of {0}: {1}".format(gene, var_class))
        potential_lof = True
print("done.")

if potential_lof:
    print("Potential LOF of SWISNF genes detected.")
else:
    print("Potential LOF of SWISNF genes was NOT detected.")
