import time
import subprocess as sub
import os

exp_running = 'experiments_all.py'

time.sleep(1)
print('Hello this is the exp_wrapper!')

while True:
   process = sub.run(['pgrep', '-af', 'python3'], stdout=sub.PIPE, stderr=sub.PIPE)
   time.sleep(10)
   if exp_running in process.stdout.decode():
       pass
   else:
       os.system('nohup python3 experiments_all.py &')
       print('Restarted script.')

   print('Experiments running. Sleeping for 60s.')
   time.sleep(60)