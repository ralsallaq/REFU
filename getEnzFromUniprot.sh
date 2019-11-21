geneECsFile=$1
if [ ! -z $2 ]; then
    outputDir=$2
    if [ ! -d $outputDir ]; then
        mkdir $outputDir
    fi
else
    outputDir="./"
fi

nGenes=$(cat $geneECsFile|wc -l)
for ((i=1;i<=nGenes;i++)); do
    gene=`head -$i $geneECsFile|tail -1|column -t|cut -f 1 -d " "`
    ecs=`head -$i $geneECsFile|tail -1|column -t|cut -f 3 -d " "`
    echo "retrieving $gene --> $ecs"
    python getEnzFromUniprot.py -ec "$ecs" -o "$gene".fasta -r true -od $outputDir
    wait
    rm -f temp.xml
    echo "number of sequences retrieved = "$(grep '^>' "$outputDir"/"$gene".fasta|wc -l)
done
