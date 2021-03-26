import pyperclip
import random
from os import listdir




DirListFull =  listdir('JumpStartDecks');
DeckLists = [];
for it in range(len(DirListFull)):
    if 'txt' in DirListFull[it]:
        DeckLists.append(DirListFull[it])


NdeckMax = len(DeckLists);

BadInput = True
while BadInput:
	try:
		Ndecks = int(input('Choose amount of 20-card boosters in deck. Minimum: 2, Maximum: '+str(NdeckMax)+'\n'));
		if Ndecks <= NdeckMax and Ndecks >= 2:
			BadInput = False;
		else:
			print('Input must be between 2 and '+str(NdeckMax)+'.')

	except ValueError:
		print('Input must be an integer.')






DeckChoose = random.sample(DeckLists, Ndecks);


print('The chosen configuration is')
print(DeckChoose)


DeckBuild = '';

for iLoad in DeckChoose:

	f1 = open('JumpStartDecks/'+iLoad,'r')
	for line in f1:
		DeckBuild = DeckBuild + line
	DeckBuild = DeckBuild + '\n'

pyperclip.copy(DeckBuild)

input('Deck copied to clipboard. Press any key to close.')
