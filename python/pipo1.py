import subprocess

output = subprocess.check_output("python -mpip list --outdated --format freeze",
                                 universal_newlines=True)
pkgs = []
for line in output.splitlines():
    pkgs.append(line[:line.index('=')])

subprocess.call("python -mpip install -U " + ' '.join(pkgs)])	 #space after -U
