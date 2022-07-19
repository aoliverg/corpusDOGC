#    downloadDOGC.py
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

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from random import randint
from time import sleep
import argparse
import os

parser = argparse.ArgumentParser(description='A program for downloading DOGC articles.')
parser.add_argument('--nummin', action="store", dest="nummin", type=int, help='The lower article number.',required=True)
parser.add_argument('--nummax', action="store", dest="nummax", type=int, help='The maximum article number.',required=True)
parser.add_argument('--outdirCAT', action="store", dest="outputdirCAT", help='The output directory for Catalan.',required=True)
parser.add_argument('--outdirSPA', action="store", dest="outputdirSPA", help='The output directory for Spanish.',required=True)


args = parser.parse_args()

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('./chromedriver',options=chrome_options)

if not os.path.exists(args.outputdirCAT):
    os.makedirs(args.outputdirCAT)
    
if not os.path.exists(args.outputdirSPA):
    os.makedirs(args.outputdirSPA)


for num in range(args.nummin,args.nummax+1):
    print("NUM",num)
    urlCAT="https://dogc.gencat.cat/ca/document-del-dogc/?documentId="+str(num)
    urlSPA="https://dogc.gencat.cat/es/document-del-dogc/?documentId="+str(num)
    driver.get(urlCAT)
    sleep(randint(3,6))
    fileout=args.outputdirCAT+"/"+str(num)+"-ca.html"
    with open(fileout, "w") as f:
        f.write(driver.page_source)
        
    driver.get(urlSPA)
    sleep(randint(3,6))
    fileout=args.outputdirSPA+"/"+str(num)+"-es.html"
    with open(fileout, "w") as f:
        f.write(driver.page_source)
driver.close()
