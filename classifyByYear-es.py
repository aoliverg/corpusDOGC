import sys
import os
import re
import codecs
import shutil
import argparse

parser = argparse.ArgumentParser(description='A program for classifying Spanish DOGC articles by year.')
parser.add_argument('--dirin', action="store", dest="dirin", help='The input directory.',required=True)
args = parser.parse_args()


dirin=args.dirin


for r, d, f in os.walk(dirin):
    for file in f:
        try:
            fullname=os.path.join(dirin,file)
            lines=codecs.open(fullname,"r",encoding="utf-8").readlines()
            text="\n".join(lines)
            m = re.search(r'<li>Fecha del DOGC<br>([0-9][0-9])/([0-9][0-9])/([0-9][0-9][0-9][0-9])</li>',text)
            try:
                data=int(m.group(3))
                print(data)
                if data<1995: dirout="html-pre1995-es"
                else: dirout="html-"+str(data)+"-es"
                if not os.path.exists(dirout):
                    os.makedirs(dirout)
                pathin=os.path.join(dirin,file)
                pathout=os.path.join(dirout,file)
                print(pathin,"-->",pathout)
                shutil.move(pathin,pathout)
            except:
                print("ERROR:",sys.exc_info())

        except:
            print("ERROR",sys.exc_info())
            sys.exit()
                

                
            
