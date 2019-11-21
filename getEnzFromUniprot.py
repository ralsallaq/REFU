import requests, sys
import xml.etree.ElementTree as ET
import argparse

def main():
    parser = argparse.ArgumentParser(description='Retrieving Enzyme Fasta file From Uniprot (REFU) using the EC numbers of the enzymes')
    parser.add_argument('--EC', '-ec', help='input EC numnbers seperated by a comma', required=True)
    parser.add_argument('--size', '-s', help='number of records to keep, default all', default=-1)
    parser.add_argument('--reviewed', '-r', help='keep only reviewed records if true, default "true"', default="true")
    parser.add_argument('--outF', '-o', help='name of output fasta file', default="output.fasta")
    parser.add_argument('--outD', '-od', help='full path to output directory', default="./")
    args = parser.parse_args()
   
    ec_numbers=",".join([e.strip() for e in args.EC.split(",")]) #comma seperated (no space)
    size = args.size
    review_status = args.reviewed
    outF=args.outF
    outD=args.outD
    
    #this is from this website https://www.ebi.ac.uk/proteins/api/doc/#!/proteins/search, where you can fill the form to get what ec, reviewed (or not), ..etc
    requestURL = "https://www.ebi.ac.uk/proteins/api/proteins?offset=0&size="+str(size)+"&reviewed="+review_status+"&ec="+str(ec_numbers)
    #print(requestURL)
    
    r = requests.get(requestURL, headers={ "Accept" : "application/xml"})
    
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    
    responseBody = r.text
    with open("temp.xml","wt") as xmlfh:
        xmlfh.write(responseBody)
    
    root = ET.parse("temp.xml").getroot()
    
    ids=[]
    seqs=[] 
    for entry in root.findall("{http://uniprot.org/uniprot}entry"):
        entry_ids=[]
        for child in entry.getchildren():
            if child.tag=='{http://uniprot.org/uniprot}sequence':
                seqs.append(child.text)
            if child.tag=='{http://uniprot.org/uniprot}accession':
                entry_ids.append(child.text)
        ids.append(",".join(entry_ids))
    
    with open(outD+"/"+outF,"wt") as out_hdl:
        for ttl, seq in zip(ids,seqs):
            out_hdl.write(">%s\n%s\n" % (ttl, seq))

if __name__ == '__main__':
    main()
