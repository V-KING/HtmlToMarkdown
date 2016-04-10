# but cannot be order list
import os

def ListFilesToTxt(_dir,file,wildcard,recursion):
    exts = wildcard.split(" ")
    files = os.listdir(_dir)
    for name in files:
        fullname=os.path.join(_dir,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion)
        else:
            for ext in exts:
                if(name.endswith(ext)):
                    file.write(name + "\n")
                    break

def Test():
  _dir="./"
  outfile="fileLists.txt"
  wildcard = ".md"
  file = open(outfile,"w")
  if not file:
    print ("cannot open the file %s for writing" % outfile)

  ListFilesToTxt(_dir,file,wildcard, 1)
 
  file.close()


Test()

