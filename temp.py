import os

dict = {}
keys = []

out_file = open("temp.txt","w+")
outstring = """
        <tr><td class="transcript">%s</td><td class="transcript">%s</td></tr>
        <tr><td><audio controls><source src="%s"></audio></td> <td><audio controls><source src="%s"></audio></td></tr>
"""

for r, d, f in os.walk("."):
  for file in f:
    if '.wav' in file:
        temp_file = file[:-4]
        original = temp_file.split("_")[4]
        adv_pred = temp_file.split("_")[5]
        typ = temp_file.split("_")[1]
        dict[(original,adv_pred,typ)] = os.path.join(r, file)[2:]
        if (typ == "std"):
            keys.append((original,adv_pred))
for x in keys:
    out_file.write(outstring%(x[0],x[1],dict[(x[0],x[1],'std')],dict[(x[0],x[1],'adv')]))
