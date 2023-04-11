#! /usr/bin/env bash
set -eo pipefail
if [ -z "$1" ]; then
    echo "Usage: tmb_for_captiv8.sh \$PATH_TO_MAF_FILE"
    exit 1
fi
if [ -n "$MODULESHOME" ]; then
    module load bcftools
fi
MUTATIONS=`bcftools view -f 'PASS' $1 | grep -cv '^#'`
MUTATION_RATE=`echo $MUTATIONS/3095978588 | bc -l` # mutation count / genome size
TMB=`echo $MUTATION_RATE*1000000 | bc -l`
echo $TMB
