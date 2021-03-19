import subprocess

with open('all_ids.txt') as f:
  data = f.readlines()
jobids = [jobid.strip() for jobid in data]

units = {'MB':1, 'GB':1e3, 'TB':1e6, 'PB':1e9}
records = []
for jobid in jobids:
  cmd = 'seff ' + jobid
  output = subprocess.run(cmd, capture_output=True, shell=True)
  lines = output.stdout.decode("utf-8").split('\n')
  for line in lines:
    if 'Memory Utilized:' in line:
      unit = line.split()[3]
      if (unit not in units): print(unit, jobid)
      util = float(line.split()[2]) * units[unit]
    if 'Memory Efficiency:' in line:
      unit = line.split()[5]
      if (unit not in units): print(unit, jobid)
      total = float(line.split()[4]) * units[unit]
  if (util > total): print(jobid, util, ">", total)
  records.append((jobid, util, total))

import csv
with open('jobid_mem_totalmem.csv', 'w') as csvfile:
  writer = csv.writer(csvfile, delimiter=',')
  for record in records:
    writer.writerow(record)
