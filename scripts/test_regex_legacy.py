with open('src/content/sources/augustine-enchiridion.yaml', encoding='utf-8') as f:
    t = f.read()
# Find the translation line
for i, line in enumerate(t.splitlines(), 1):
    if 'translation' in line:
        print(f'Line {i}: {line!r}')
        # Show each char
        for j, c in enumerate(line):
            if c in '"\'':
                print(f'  pos {j}: {c!r}')
        break
