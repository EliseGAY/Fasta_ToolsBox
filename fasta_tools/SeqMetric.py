# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 10:13:31 2025

@author: elise
"""
# """ 
# Author : Elise Gay (EPHE, MNHN)
# 2025
# Seq class to compute metrics on fasta sequence
# """

class Seq:
    def __init__(self, seqType, seq, Ind):
        
        self.scaf = None
        self.start = None
        self.end = None
        self.gene_id = None
        self.seq = str(seq)
        self.Nper = None
        self.Seqlen = None
        self.seqType = str(seqType)
        self.Ind = str(Ind)
        
    def length(self):
        self.Seqlen=len(self.seq)
        return self.Seqlen
     
    def get_Nper(self):
        Ncount=self.seq.upper().count("N")
        self.Nper=float(Ncount)/float(self.length())*100
        return self.Nper
        
    def __str__(self):
        return ("scaf = {}, start = {}, end = {}, gene_id = {}, seq = {}, Nper = {}, Seqlen = {}, seqType = {}, Ind= {}" ).format(self.scaf, self.start, self.end, self.gene_id, self.seq, self.Nper, self.Seqlen, self.seqType, self.Ind)

    def __len__(self):
        return ("scaf = {}, start = {}, end = {}, gene_id = {}, seq = {}, Nper = {}, Seqlen = {}, seqType = {}, Ind= {}" ).format(self.scaf, self.start, self.end, self.gene_id, self.seq, self.Nper, self.Seqlen, self.seqType, self.Ind)

    def coor(self):
        
        return f"Hello, {self.name}!"
    
    def name(self):
        return f"Hello, {self.name}!"
