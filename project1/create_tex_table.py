import os
import pickle
import itertools

tmp = os.getcwd()
os.chdir('..')
tmp = os.getcwd()

# only necessary if experiments were killed inbetween. Currently only needed for Entrecampos
def getCompleteDict(dir):
    complete_dict = {}
    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        with open(os.path.join(dir, filename), 'rb') as f:
            data_dict = pickle.load(f)
            for key, value in data_dict.items():
                if key not in complete_dict:
                    complete_dict[key] = value
    return complete_dict

def getDict(dir, id):
    names = ['Antas-Espinho', 'Entrecampos', 'Estarreja', 'Laranjeiro-Almada', 'Mem-Martins', 'Paio-Pires', 'Restelo', 'Sobreiras-Porto', 'VNTelha-Maia']
    with open(os.path.join(dir, names[id], '2_2_2_2.pkl'), 'rb') as f:
        data = pickle.load(f)
    return data

dir_entre = os.path.join(tmp, 'models/proj1/Entrecampos')
entre = getCompleteDict(dir_entre)

dir = os.path.join(tmp, 'models/proj1')
antas = getDict(dir, 0)
estar = getDict(dir, 2)
laran = getDict(dir, 3)
mem = getDict(dir, 4)
paio = getDict(dir, 5)
rest = getDict(dir, 6)
sobre = getDict(dir, 7)
vnt = getDict(dir, 8)

dicts = [antas, entre, estar, laran, mem, paio, rest, sobre, vnt]

p_list = list(range(0,3))
q_list = list(range(0,3))
P_list = list(range(0,3))
Q_list = list(range(0,3))

for p,q,P,Q in itertools.product(p_list, q_list, P_list, Q_list):
    key = f'{p},{q},{P},{Q}'
    bic_list = []
    for data in dicts:
        if key in data:
            bic = data[key]
        else:
            bic = 0.0
        bic_list.append(bic)
    print(f'{p} & {q} & {P} & {Q} & {bic_list[0]:.2f} & {bic_list[1]:.2f} & {bic_list[2]:.2f} & {bic_list[3]:.2f} & {bic_list[4]:.2f} & {bic_list[5]:.2f} & {bic_list[6]:.2f} & {bic_list[7]:.2f} & {bic_list[8]:.2f}   \\\\')