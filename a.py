with open('src.txt') as fd: lines=fd.readlines()
def strip_non_digits(s): return ''.join( [x for x in s if x in '0123456789'] )
def strip_endspace(s): return s.strip()
def nnn4int(oInt): return str(1000+oInt)[-3:]
for line in lines:
    left,rite = line.split('-')
    book = ''.join(map(strip_endspace,left.split()))
    #rite=map(strip_non_digits,rite.split())
    chapter, vcount = map(int, map(strip_non_digits,rite.split()))
    #chapter=str(1000+chapter)[-3:]
    #vcount = int(vcount)
    for verse in range(1,vcount+1):
        _chapter = nnn4int(chapter)
        _verse = nnn4int(verse)
        name='_'.join( [book, _chapter, _verse] )
        assert not ' ' in name
        assert len(name.split('_'))==3
        print(name)
