import glob

original_files = glob.glob('data/*_original.snt.aligned')
modern_files = glob.glob('data/*_modern.snt.aligned')

with open('combined_modern.snt.aligned', 'wb') as outfile:
    for f in modern_files:
        with open(f, 'rb') as infile:
            print(infile.name)
            outfile.write(infile.read())

with open('combined_original.snt.aligned', 'wb') as outfile:
    for f in original_files:
        with open(f, 'rb') as infile:
            print(infile.name)
            outfile.write(infile.read())
