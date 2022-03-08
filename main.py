import json
import string

_VERSION = '0.3.2'

def main():
    with open('config.json', encoding='utf8') as f:
        config = json.load(f)
    config['host'] = config['host'].rstrip('/')

    with open('asoul-sticker-base.css', encoding='utf8') as f:
        css_base = string.Template(f.read())
    with open('asoul-sticker-template.css', encoding='utf8') as f:
        css_template = string.Template(f.read())

    sticker_items = []
    class_prefixes = set()
    with open('data.txt', encoding='utf8') as f:
        for line in [l.strip() for l in f]:
            if len(line) == 0 or line[0] == '#':
                continue
            dir_name, file_name, class_name, alt_name = line.split(' ')
            class_prefixes.add(dir_name)
            if config['flatten']:
                host = config['host']
            else:
                host = f'{config["host"]}/{dir_name}'
            css_item = css_template.substitute(
                className=class_name,
                host=host,
                filename=file_name,
                alt=f'[{alt_name}]',
            )
            sticker_items.append(css_item)

    with open('dist/asoul-sticker.css', 'w', encoding='utf8', newline='\n') as f:
        selectors = [f'span[class^="{prefix}_"]' for prefix in sorted(class_prefixes)]
        f.write(css_base.substitute(
            version=_VERSION,
            host=config["host"],
            height=config['height'],
            flatten=str(config['flatten']).lower(),
            selectors=',\n'.join(selectors)
        ))
        f.write('\n')
        f.write(''.join(sticker_items))

if __name__ == '__main__':
    main()
