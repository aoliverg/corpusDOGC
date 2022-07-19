#    DOGCtextDIR.py
#    Copyright (C) 2022  Antoni Oliver
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import codecs
import sys
from bs4 import BeautifulSoup
import os
import argparse

def DOGC2text(arxiu):
    textList=[]
    entrada=codecs.open(infile,"r",encoding="utf-8")
    html="\n".join(entrada.readlines())
    if not html.find("No s’ha trobat cap document amb aquest ID.")>-1:
        #<div id="fullText" class="wrapper-document">
        soup = BeautifulSoup(html, 'html.parser')
        fulltext = str(soup.find_all('div',attrs={'id': 'fullText', 'class': 'wrapper-document'})[0])
        soupFT = BeautifulSoup(fulltext, 'html.parser')
        try:
            title=soupFT.find_all('h1')[0]
            print("TITLE:",title.text)
            textList.append(title.text)
        except:
            pass
        try:
            textBrut=soupFT.find_all('p')
            for t in textBrut:
                textList.append(str(t.text))
        except:
            pass
        text="\n".join(textList)
    else:
        text=""
    return(text)
    

parser = argparse.ArgumentParser(description='A program to convert all DOGC html files in a given directory to text.')
parser.add_argument('--dirin', action="store", dest="dirin", help='The input directory containing the html files.',required=True)
parser.add_argument('--dirout', action="store", dest="dirout", help='The output directory.',required=True)
args = parser.parse_args()

inDIR=args.dirin
outDIR=args.dirout

if not os.path.exists(outDIR):
    os.makedirs(outDIR)


for file in os.listdir(inDIR):
    infile=os.path.join(inDIR, file)
    outfile=os.path.join(outDIR, file).replace(".html",".txt")
    print(infile,outfile)
    try:
        sortida=codecs.open(outfile,"w",encoding="utf-8")
        text=DOGC2text(infile).strip()
        if len(text)>0:
            sortida.write(text+"\n")
            sortida.close()
    except:
        print("ERROR",sys.exc_info()[0])
