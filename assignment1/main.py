import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import re

ciphertext = """CKCLBAELDK DGJ LFNSMBCA CGQEGCCAI JCUCKFS DGJ LACDBC SAFJMLBI BHDB LHDGQC BHC
OFAKJ DGJ NDVC FMA KEUCI CDIECA BHC LCKK SHFGCI OC JCSCGJ FG BHC LFNSMBCAI MICJ EG
GDBEFGDK ICLMAEBR DGJ BHC CKCLBAELDK IRIBCNI BHDB NDVC FMA LDAI FSCADBC OCAC DKK
LACDBCJ TR CKCLBAELDK DGJ LFNSMBCA CGQEGCCAI DB OSE OC VCCS BHDB SAFQACII
NFUEGQ PFAODAJ OEBH FMA EGGFUDBEUC ACICDALH DGJ FMB-FP-BHC TFY DSSAFDLHCI BHC
JCSDABNCGB FP CKCLBAELDK DGJ LFNSMBCA CGQEGCCAEGQ DB OSE LHDKKCGQCI IBMJCGBI
BF SMIH BHCNICKUCI BF MGJCAIBDGJ IFLECBRI DGJ BCLHGFKFQRI LFNSKCY EIIMCI EG D
TAFDJCA LFGBCYB BHDG OHDBI EG PAFGB FP BHCN OC ODGB FMA IBMJCGBI OHCBHCA BHCR
DAC CDAGEGQ DG MGJCAQADJMDBC NEGFA FA D JFLBFADBC BF BDLVKC IFLECBRI NFIB
SACIIEGQ SAFTKCNI DGJ MGLFUCA GCO ODRI FP IFKUEGQ BHCN OHCBHCA EBI JCUCKFSEGQ
IRIBCNI BHDB LDG KFLDBC PEACPEQHBCAI EG BHC NEJJKC FP D TMAGEGQ TMEKJEGQ FA
LACDBEGQ GCMAFSAFIBHCBELI BHDB KFFV DGJ PMGLBEFG KEVC GDBMADK KENTI FMA
PDLMKBR DGJ IBMJCGBI DAC DB BHC PAFGB CJQC FP ACNDAVDTKC EGGFUDBEFG OHEKC
DJUDGLEGQ BCLHGFKFQECI EI DB FMA LFAC OC DKIF BDVC HMNDG LFGGCLBEFGI UCAR
ICAEFMIKR EG CLC OC SAEJC FMAICKUCI FG BHC PDNEKR-KEVC DBNFISHCAC OC LMKBEUDBC;
PDLMKBR IBMJCGBI DGJ IBDPP CGLFMADQC CDLH FBHCAI CUCAR IMLLCII DGJ DAC BHCAC PFA
BHC LHDKKCGQCI TFBH EG BHC LKDIIAFFN DGJ EG KEPC"""

englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

frequencies = dict()
for character in ciphertext:
    if not character.isalpha():
        continue
    frequencies[character] = frequencies[character] + 1 if character in frequencies.keys() else 1
    
plt.bar(*zip(*frequencies.items()))
plt.show()

for freq in frequencies:
    frequencies[freq] = frequencies[freq] / len(re.sub(r'[^a-zA-Z]', '', ciphertext))
        
sorted_cipher_frequencies = dict(sorted(frequencies.items(), key=lambda i: i[1], reverse=True))
sorted_eng_frequencies = dict(sorted(englishLetterFreq.items(), key=lambda i: i[1], reverse=True))



plt.bar(*zip(*sorted_cipher_frequencies.items()))
plt.show()

plt.bar(*zip(*sorted_eng_frequencies.items()))
plt.show()

key = ['E', 'T', 'A', 'N', 'O', 'R', 'S', 'I', 'C', 'L', 'H', 'D', 'U', 'M', 'P', 'G', 'W', 'F', 'V', 'Y', 'K', 'B', 'X']
cipherCharsByFreq = list(sorted_cipher_frequencies.keys())

print(cipherCharsByFreq)
print(key)

decoded = ''
for c in ciphertext:
    if not c.isalpha():
        decoded += c
        continue
    charFreqIndex = cipherCharsByFreq.index(c)
    decodedChar = key[charFreqIndex]
    decoded += decodedChar


print(decoded)