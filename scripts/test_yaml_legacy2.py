import yaml
with open('src/content/sources/augustine-enchiridion.yaml', encoding='utf-8') as f:
    text = f.read()
# Strip the frontmatter delimiter
text = text.replace('---\n', '', 1).rstrip()
try:
    data = yaml.safe_load(text)
    print('parsed OK')
    print('keys:', list(data.keys()) if isinstance(data, dict) else type(data))
    print('paraphrase:', repr(data.get('paraphrase')))
except Exception as e:
    print('parse error:', e)
