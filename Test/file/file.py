fname = input('Enter the file name: ')
try:
    fhand = open(fname,'r') 
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname) 