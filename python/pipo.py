import os

pkgs = []
for line in os.popen("python -mpip list --outdated --format freeze"): # name==ver
    print(line)
    pkgs.append(line[:line.index('=')])

if pkgs:
    os.system("python -mpip install --upgrade " + ' '.join(pkgs)) #space after --upgrade
else:
    print("no packages outdated");
