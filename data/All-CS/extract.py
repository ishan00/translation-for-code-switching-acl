import json
import random
random.seed(0)

def strip_ne(sent):
	return sent.lower().replace('/ne/','')

def write_to_file(data, file):
	f = open(file, 'w')
	for ln in data:
		f.write('%s\n'%ln.strip())
	f.close()
	print ('Wrote %d lines to %s'%(len(data), file))

with open('All-CS.json','r') as f:
	data = json.load(f)

train_hi = []
train_cs = []

test_hi = []
test_cs = []

valid_hi = []
valid_cs = []

for i in range(len(data)):
	item = data[i]
	if item['split'] == 'train':
		mono = item['mono_raw']
		cs_sentences = [item['gold']] + item['mturk'] if 'gold' in item.keys() else item['mturk']
		for cs in cs_sentences:
			train_hi.append(mono)
			train_cs.append(strip_ne(cs))
	else:
		mono = item['mono_raw']
		cs = item['gold'] if 'gold' in item else item['mturk'][0]
		if item['split'] == 'valid':
			valid_hi.append(mono)
			valid_cs.append(strip_ne(cs))
		else:
			test_hi.append(mono)
			test_cs.append(strip_ne(cs))

shuffled_train_hi = []
shuffled_train_cs = []

idx = list(range(len(train_hi)))
random.shuffle(idx)

for i in idx:
	shuffled_train_hi.append(train_hi[i])
	shuffled_train_cs.append(train_cs[i])

write_to_file(shuffled_train_hi, 'hi.train')
write_to_file(valid_hi, 'hi.valid')
write_to_file(test_hi, 'hi.test')
write_to_file(shuffled_train_cs, 'en.train')
write_to_file(valid_cs, 'en.valid')
write_to_file(test_cs, 'en.test')
