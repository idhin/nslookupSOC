import subprocess

with open('ip.txt') as i, open('nslookup.txt', 'w') as o:
   for line in i:
     if line.strip(): # skips empty lines
        proc = subprocess.Popen(["nslookup", line.strip()],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        o.write('{}\n'.format(proc.communicate()[0]))

print('Done')