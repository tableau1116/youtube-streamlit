data = ['3-A', '2-B', '1-C', '3-D', '1-E', '1-G', '2-H', '3-I']
counter = {}
for value in data:
    year, name = value.split('-')   
    if year not in counter:
        counter[year] = []
    counter[year].append(name)    
for year in sorted(counter):
    print(f'{year}年')
    for order, name in enumerate(counter[year]):
        print(f'{order+1}位:{name}') 
           
