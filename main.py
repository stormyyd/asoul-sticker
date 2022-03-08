import json
import string

_VERSION = '0.3.1'

def main():
    with open('config.json', encoding='utf8') as f:
        config = json.load(f)
    config['host'] = config['host'].rstrip('/')

    with open('asoul-sticker-base.css', encoding='utf8') as f:
        css_base = string.Template(f.read())
    with open('asoul-sticker-template.css', encoding='utf8') as f:
        css_template = string.Template(f.read())

    css_items = []
    with open('data.txt', encoding='utf8') as f:
        for line in [l.strip() for l in f]:
            if len(line) == 0 or line[0] == '#':
                continue
            dir_name, file_name, class_name, alt_name = line.split(' ')
            if config['flatten']:
                host = config['host']
            else:
                host = f'{config["host"]}/{dir_name}'
            css_item = css_template.substitute(className=class_name, host=host, filename=file_name, alt=f'[{alt_name}]')
            css_items.append(css_item)

    with open('dist/asoul-sticker.css', 'w', encoding='utf8', newline='\n') as f:
        f.write(css_base.substitute(version=_VERSION, host=config["host"], height=config['height'], flatten=str(config['flatten']).lower()))
        f.write('\n')
        f.write(''.join(css_items))

if __name__ == '__main__':
    main()
