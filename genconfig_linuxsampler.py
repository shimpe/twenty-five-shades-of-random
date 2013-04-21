import os.path
import sys

def getInstallPath():
    thePath = os.path.dirname(sys.argv[0])
    if thePath:
        thePath += os.sep
    else:
        thePath = "./"
    return os.path.abspath(thePath)

if __name__ == "__main__":
    print "INSTALLATION PATH: getInstallPath()"
    print "{0}/synthconfig/linuxsampler.lscp".format(getInstallPath())

    with open("{0}/synthconfig/linuxsampler.lscp.template".format(getInstallPath()), "r") as f:
      lines = f.readlines()

    with open("{0}/synthconfig/linuxsampler.lscp".format(getInstallPath()), "w") as f:
      for l in lines:
        l = l.replace("#####", getInstallPath())
        f.write(l)

