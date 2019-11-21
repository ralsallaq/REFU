
# Retrieving Enzyme Fasta from Uniprot (REFU)

REFU is a utility for retrieving protein fasta files for enzymes or genes using the enzyme code (EC number)

## Getting Started

```
1. prepare a text file with two columns (tab delimited) the first column is the gene name and the second is the corresponding EC number(s) separated by comma (e.g. see  example_gene_EC.txt)  
2. clone REFU:
    git clone https://github.com/ralsallaq/REFU.git
3. move the text file you just prepared to the REFU directory (say you named it gene_EC.txt)
    mv gene_EC.txt REFU
4. change directory to REFU
    cd REFU
5. simply run: 
   ./getEnzFromUniprot.sh gene_EC.txt /path/to/output/directory
6. this will retrieve a fasta file for each gene and save it as (geneName).fasta (e.g. AKR1D1.fasta) under the output directory provided (which will be created if it does not exist)  
   
```


### Prerequisites

* **python >=2.7
* **requests library



### Installing

clone the repository to a desired directory

```
git clone https://github.com/ralsallaq/REFU.git
```

## Authors

* **Ramzi Alsallaq

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Fitching uniprot records using python: https://www.ebi.ac.uk/proteins/api/doc/#!/proteins/search 
