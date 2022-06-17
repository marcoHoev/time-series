import os
import pickle

tmp = os.getcwd()
os.chdir('..')
dir = os.path.join(tmp, 'models/proj1/Entrecampos')

complete_dict = {}
tuple_list = []

for file in os.listdir(dir):
    filename = os.fsdecode(file)
    with open(os.path.join(dir, filename), 'rb') as f:
        data_dict = pickle.load(f)
        for key, value in data_dict.items():
            if key not in complete_dict:
                complete_dict[key] = value

for key, value in complete_dict.items():
    tuple_list.append((value, key))

print(len(tuple_list))

ordered_list = sorted(tuple_list)

for i in range(9):
    print(ordered_list[i])

# get latex code
for model in ordered_list:
    if '3' in model[1]:
        continue
    p0,q0,p1,q1 = model[1].split(',')

    print(f'{p0} & {q0} & {p1} & {q1} & {model[0][0]} & {model[0][1]} \\\\')


#best_key = min(complete_dict, key=lambda key: complete_dict[key][0])
#print(complete_dict[best_key])