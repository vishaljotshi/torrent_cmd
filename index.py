import re,gzip,urllib2,webbrowser,sys
from colorama import Fore,Back,Style
import colorama,sys,os
from StringIO import StringIO

colorama.init()
WH=Fore.WHITE
GR=Fore.LIGHTBLACK_EX
BL=Fore.LIGHTBLUE_EX
CY=Fore.CYAN
YE=Fore.YELLOW
RE=Fore.LIGHTRED_EX
GRE=Fore.LIGHTGREEN_EX

try:
    if sys.argv[1] == '-l':
        rinp=raw_input("Enter search term : ")
        try:
            req=urllib2.urlopen("https://kickass.to/usearch/"+ rinp +"/")
            buf=StringIO(req.read())
            fp=gzip.GzipFile(fileobj=buf).read()
        except:
            print RE+"[-]"+ GR+" No torrent found for this query!"+WH
            print
            os._exit(0)



        links=re.findall(r'<a\shref\=\"(.*)\"\sclass\=\"cellMainLink\">(.*)<\/a>[\r\n.]*.*[\r\n.]*.*[\r\n.]*.*[\r\n.]*.*[\r\n.]*.*>(.*)<span>(.*)<\/span>.*[\r\n.]*.*[\r\n.]*.*>(.*)&nbsp;(.*)<\/td>[\r\n.]*.*>(.*)<\/td>', fp)
        i=0
		#with magnet regular expression :
		# <a\shref\=\"(.*)\"\sclass\=\"cellMainLink\">(.*)<\/a>[\r\n.]*.*[\r\n.]*.*[\r\n.]*.*[\r\n.]*.*[\r\n.]*.*>(.*)<span>(.*)<\/span>.*[\r\n.]*.*[\r\n.]*.*>(.*)&nbsp;(.*)<\/td>[\r\n.]*.*>(.*)<\/td>[\r\n.]*.*[\r\n.]*.*[\r\n.]*.*[\r\n.]*.*[\r\n.]*.*[\r\n.]*.*magnet': '(.*)' \}
		# Last group is of magnetic link :)
        for l in links:
            a=l[1]
            if "strong" in l[1]:
                b=l[1].replace('<strong class="red">','')
                a=b.replace('</strong>','')
            if i!=1:    
                print GR+'['+CY+str(i)+GR+'] >> ',WH+a+GR,"Size:",WH+l[2],l[3]+GR,l[4],l[5],"Seeds:",Fore.YELLOW+l[6]+WH
                i += 1
        #automatically downloading the torrent
                print
                maglnk= "https://kickass.to"+ links[0][0]
                print GRE+"[+]"+WH+" Fetching magnetic link...."
                req=urllib2.urlopen(maglnk)
                buf=StringIO(req.read())
                fp=gzip.GzipFile(fileobj=buf).read()

                mag_lnk=re.findall(r'title="Magnet link" href="(.*)"\sclass="',fp)
                print GRE+"[+]"+WH+" Magnet Link fetched!"
                print GRE+"[+]"+WH+" Opening Link in torrent..."
                webbrowser.open(mag_lnk[0])
                os._exit(0)


        
    if sys.argv[1] == '-h':
        print "Usage: "+sys.argv[0]+" -l\n\n\t Turns on \'I am feeling lucky\' mode and auto downloads the first torrent\n\t file from search results\n\t Useful when downloading serials."
        os._exit(0)
except:
    print

print CY+"\t\tEasy torrent downloader by vishal jotshi MVJ\n"+GR+"\t\t\thttp://facebook.com/jotshi"+WH
def search():
    rinp=raw_input("Enter search term : ")
    try:
        req=urllib2.urlopen("https://kickass.to/usearch/"+ rinp +"/")
        buf=StringIO(req.read())
        fp=gzip.GzipFile(fileobj=buf).read()
    except:
        print RE+"[-]"+ GR+" No torrent found for this query!"+WH
        print
        return 0
    


    links=re.findall(r'<a\shref\=\"(.*)\"\sclass\=\"cellMainLink\">(.*)<\/a>[\r\n.]*.*[\r\n.]*.*[\r\n.]*.*[\r\n.]*.*[\r\n.]*.*>(.*)<span>(.*)<\/span>.*[\r\n.]*.*[\r\n.]*.*>(.*)&nbsp;(.*)<\/td>[\r\n.]*.*>(.*)<\/td>', fp)
    i=0
    for l in links:
        a=l[1]
        if "strong" in l[1]:
            b=l[1].replace('<strong class="red">','')
            a=b.replace('</strong>','')
            
        print GR+'['+CY+str(i)+GR+'] >> ',WH+a+GR,"Size:",WH+l[2],l[3]+GR,l[4],l[5],"Seeds:",Fore.YELLOW+l[6]+WH
        i += 1


    inp=raw_input("\n\nEnter index number( OR e-> exit; s-> search again): ")
    try:
        if inp=='s':
            search()
            return 1
        if inp=='e':
            return 1
        maglnk= "https://kickass.to"+ links[int(inp)][0]
    except:
        print RE+"[-]"+ GR+" Please select the valid index."+WH
        print
        return 0
    print GRE+"[+]"+WH+" Fetching magnetic link...."
    req=urllib2.urlopen(maglnk)
    buf=StringIO(req.read())
    fp=gzip.GzipFile(fileobj=buf).read()

    mag_lnk=re.findall(r'title="Magnet link" href="(.*)"\sclass="',fp)
    print GRE+"[+]"+WH+" Magnet Link fetched!"
    print GRE+"[+]"+WH+" Opening Link in torrent..."
    webbrowser.open(mag_lnk[0])
    return 1

    
flag=search()
while flag!=1:
    flag=search()
    
