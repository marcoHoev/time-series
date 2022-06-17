import time
import subprocess as sub
import os

exp_running = 'project1/experiments.py'
count = 0

time.sleep(1)
print('Hello this is the saver!')

while True:
    process = sub.run(['pgrep', '-af', 'python'], stdout=sub.PIPE, stderr=sub.PIPE)
    time.sleep(10)
    if exp_running in process.stdout.decode():
        pass
    else:
        #os.system('conda activate ts')
        os.system(f'nohup python {exp_running} &')
        print('Restarted script.')
        count += 1
        
    print('Experiments running. Sleeping for 60s.')
    time.sleep(60)