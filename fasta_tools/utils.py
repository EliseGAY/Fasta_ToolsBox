""" Modules to play with fasta files """

#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# """ 
# Author : Elise Gay (EPHE, MNHN)
# Modules to parse and format fasta file
# """

#------------------------#
# Import modules
#------------------------#
import sys
import re

#------------------------#
# import class
#------------------------#

from .SeqMetric import Seq

#------------------------#
#------------------------#
# Split fasta
#------------------------#
#------------------------#

def split_fasta(fasta_file, nb_seq):
    """
    Usage
    ------
    Split fasta file in 'n' fasta file with 'x' sequences
    Launch the function with 2 arguments : yourfile.fasta and nb_seq
    Python verion 3.6

    Arguments
    ---------
    fasta.file : PATH/to_your/fasta.file
    nb_seq : Number of seqeunces required in each fasta file

    command line
    -------------
    Fasta_Tools.subset_fasta(yourfile.fasta, nb_seq)

    output : fasta files numeroted from 1 to 'x' will be created and will contain 'nb_seq' sequence in it
    --------

    Features to fix
    -----------------
    note : if limit we want to split fasta in file with 2 sequences
    round 1 = fasta file "1" with 2 sequence
    round 2 = compteur = 0 but the third seq is already written in the fasta file "2"
    So "compteur" variable will be = 1 then = 2 and 2 sequences will be written in addition.
    the total number of sequences in the file "2" in the round 2 will be = 3
    """
    #----------------------------#
    # read and initiate variable
    #----------------------------#

    fasta_file = open(fasta_file, "r")
    filin = open("1", "w")
    compteur = 0
    nom = 1
    nb_seq=int(nb_seq)

    #----------------------------#
    # Split fasta file
    #----------------------------#

    for seq in fasta_file :
        if ">" in seq:
            compteur += 1
        if compteur <= 2:
            filin.write(seq)
        if compteur > 2:
            filin.close()
            nom +=1
            f = str(nom)
            filin = open(f, "w")
            filin.write(seq)
            compteur = 0
    fasta_file.close()
    filin.close()

#------------------------#
#------------------------#
# Dictionnary
#------------------------#
#------------------------#

def fasta_dict(fasta_file):
    """
    Usage
    ------
    Create dictionnary of Key=sequence_ID and value=Sequences
    Launch the function with 1 argument : yourfile.fasta
    Python verion 2.7

    Arguments
    ---------
    fasta.file : PATH/to_your/fasta.file

    command line
    -------------
    Fasta_Tools.fasta_dict(fasta.file)

    output : Dictionnary type variable
    --------
    """
    #----------------------------#
    # read and initiate variable
    #----------------------------#

    dico_fasta = {}
    seq = []
    join_seq = []
    fasta_file = open(fasta_file, "r")

    for ligne in fasta_file:
        ligne = ligne.replace("\n", "")
        if re.search('^>', ligne):
            nom=ligne[1:]
            seq = []
        else :
            seq.append(ligne)
            join_seq = "".join(seq)
            dico_fasta[nom] = join_seq

    return dico_fasta

#------------------------#
#------------------------#
# Subset seq from ID list
#------------------------#
#------------------------#

def Select_Seq(fasta_file, ID_list, output_name):
    """
    Usage
    ------
    Subset fasta file from an ID list of sequence
    Launch the function with 2 arguments : yourfile.fasta , ID_list
    Python verion 3.6

    Arguments
    ---------
    fasta.file : PATH/to_your/fasta.file
    ID_list : ["ID1", "ID2"] list of string
    output_name : "name.fasta", string

    command line
    -------------
    Fasta_Tools.Select_Seq(fasta.file, ID_list)

    output : Fasta file written in your directory with subset of sequences
    --------
    """

    #----------------------------#
    # read and initiate variable
    #----------------------------#

    # format ID string, remove '\n'
    ID_final=[]
    for ID in ID_list:
        ID_final.append(ID.replace("\n", ""))
    print ("your list Id contains",len(ID_final),"ID")

    # creation fichier fasta avec les id fournis
    fasta = open(str(output_name), "w")
    # create dict from fasta file
    dico_fasta=fasta_dict(fasta_file)
    for i in ID_final:
        if i in dico_fasta.keys():
           fasta.write(">"+i)
           fasta.write("\n")
           fasta.write(dico_fasta[i])
           fasta.write("\n")
    fasta.close()


#-------------------------------------#
#-------------------------------------#
# Append name in fasta file
#-------------------------------------#
#-------------------------------------#

def add_fasta_name(fasta_file, name_file, output_name):
    """
    Usage
    ------
    Add attribute to fasta ID and return fasta file with complete ID
    Launch the function with 2 arguments : yourfile.fasta , ID_file
    Avoid redundancy : if an ID in the first fasta file is present in several new_ID only
    the first occurence is selected.
    In the case of same exon coordinates present in several transcript ID for instance

    Python verion 3.6 / 2.7

    Method :
    --------
    search each subtring of the current fasta ID in a list of new ID.
    If subtring exist in new ID it create an new element in dictionnary  {name_seq : seq}
    Write a new fasta file with complete seq name

    Arguments
    ---------
    fasta.file : PATH/to_your/fasta.file
    ID_list : PATH/to_your/ID_file (one name in each line)
    output_name : "name.fasta", string

    command line
    -------------
    Fasta_Tools.add_fasta_name(fasta.file, ID_file, output_name)

    output : Fasta file written in your directory with same sequence but new ID
    -----
    """

    #----------------------------#
    # read and initiate variable
    #----------------------------#

    # create dictionary of all seqeunce with their ID
    dict_seq=fasta_dict(fasta_file)
    # initiate a new dict
    dict_full={}

    # read the new ID file
    full_name_file=open(name_file, 'r')
    full_name_lines=full_name_file.readlines()
    print ("your list of new ID contains",len(full_name_lines),"ID")

    # initiate seq name
    idx_rep="none"

    #------------------------------------------------#
    # get first index in full_name list contains keys
    #------------------------------------------------#
    for key in dict_seq.keys():
        idx_rep="none"
        for full_ID in full_name_lines :
            if str(key) in str(full_ID) and idx_rep=="none" :
                idx_rep="yes"
                dict_full[full_ID]=dict_seq[key]
                break
            else:
                continue

    print("new dict contains",len(dict_full),"values")

    # write new fasta file
    fasta_out=open(str(output_name), "w")
    for key in dict_full.keys():
        fasta_out.write(key)
        fasta_out.write(dict_full[key])
        fasta_out.write('\n')

    fasta_out.close()
    
#-------------------------------------#
#-------------------------------------#
# Remove duplicates value (but uniq key)
# in dicionnary
#-------------------------------------#
#-------------------------------------#

def remove_dup(fasta_file, output_fasta):
    """
    Usage
    ------
    Remove dupicated nucleiq seqeuence in fasta file
    Example : exon file with same sequence but annotated in different transcript variant in the ">ID"
    Launch the function with 1 argument : yourfile.fasta
    Dependency : fasta_dict(fasta_file) function
    Python verion 2.7

    Warnings
    --------
    If your sequences have, by chance, the same size and are composed only of "N" or have the same sequences but are not from redundancy, they will be discarded too

    Arguments
    ---------
    fasta.file : PATH/to_your/fasta.file

    command line
    -------------
    Fasta_Tools.remove_dup(fasta.file, output_fasta.file)

    output : Fasta file with the first occurence of each duplicated sequences only
    --------
    """
    # initiate an empty dictionnary
    result = {}
    # create a dictionnary for your fasta file
    dict_seq=fasta_dict(fasta_file)

    # loop on your full dict and write the key, value in the empty one only if the value is not already present
    for key,value in dict_seq.items():
        if value not in result.values():
            result[key] = value

    # write the new dictionnary with uniq values in a new fasta file
    fastout=open(str(output_fasta), 'w')
    for key in result.keys():
        fastout.write(">"+key+"\n"+result[key]+"\n")
    fastout.close()

def get_N_percent(fasta_file, output_file, sample_name=None):
    """
    Usage
    ------
    Count number of "N" or "n" character in fasta sequence
    Launch the function with 3 argument : yourfile.fasta, output_file, sample_name (optional)
    Dependency : fasta_dict(fasta_file) function
    Python verion 2.7 + 3.6

    Arguments
    ---------
    fasta.file : PATH/to_your/fasta.file
    output_file : txt file , with seq_id, sample name and N percent for each sequence by row
    sample_name : string, name of the sample (optional)

    command line
    -------------
    Fasta_Tools.get_N_percent(fasta.file,  output_file, sample_name)

    output : ID percent_N in a file
    --------
    """

    dict_seq = fasta_dict(fasta_file)

    with open(output_file, "w") as out:
        out.write(f"seq_id\t{sample_name}\n")

        for seq_id, sequence in dict_seq.items():

            s = Seq(seqType="consensus", seq=sequence, Ind=sample_name)
            nper = s.get_Nper()

            out.write(f"{seq_id}\t{nper}\n")
