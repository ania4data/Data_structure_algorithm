"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
incoming_calls = []
outgoing_calls = []
for call in calls:
	incoming_calls.append(call[1])
	outgoing_calls.append(call[0])
incoming_calls = set(incoming_calls)
outgoing_calls = set(outgoing_calls)

incoming_texts = []
outgoing_texts = []
for text in texts:
	incoming_texts.append(text[1])
	outgoing_texts.append(text[0])
incoming_texts = set(incoming_texts)
outgoing_texts = set(outgoing_texts)
'''
for O(n^2) complexity, better solution is using sets
telemarketers_list = [] 
for call in outgoing_calls:
	if((call not in incoming_calls) and (call not in incoming_texts) and (call not in outgoing_texts)):
		telemarketers_list.append(call)
telemarketers_list = sorted(telemarketers_list)
'''
not_in_sets = incoming_calls.union(incoming_texts, outgoing_texts)
telemarketers_list = list(outgoing_calls - not_in_sets)

telemarketers_list = sorted(telemarketers_list)
print('These numbers could be telemarketers:')
for telemarketer in telemarketers_list:
	print(telemarketer)
