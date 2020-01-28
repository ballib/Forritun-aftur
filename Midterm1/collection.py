cans = input("Enter number of cans: ")
int_cans = int(cans)

can  = int_cans%6
int_packs = int_cans//6
packs = int_packs%4
boxes = int_packs//4



print(f'{boxes} boxe(s), {packs} pack(s), and {can} can(s)')


