s = input("Do you agree: ").lower()

# if s == 'Y' or s == 'y':
if s.lower() in ['y','yes']:
    print('Agreed')
# elif s == 'N' or s == 'n':
elif s.lower() in ['N', 'n']:
    print('Disagreed')
