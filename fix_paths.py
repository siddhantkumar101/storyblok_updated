import glob

pages_files = glob.glob('pages/*.html')

for f in pages_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix broken index.html anchors
    content = content.replace('href="index.html#', 'href="../index.html#')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Fixed index.html# anchors.")
