import json
import string

def main():
    css_items = []
    with open('config.json', encoding='utf8') as f:
        config = json.load(f)
    with open('style_template.css', encoding='utf8') as f:
        css_template = string.Template(f.read())
    flatten = config["flatten"]
    with open('data.txt', encoding='utf8') as f:
        for line in [l.strip() for l in f]:
            if len(line) == 0 or line[0] == '#':
                continue
            dir_name, file_name, class_name, alt_name = line.split(' ')
            if flatten:
                host = config['host']
            else:
                host = config['host'] + '/' + dir_name
            css_item = css_template.substitute(className=class_name, host=host, filename=file_name, height=config['height'])
            css_items.append(css_item)
    css_content = ''.join(css_items)
    with open('dist/asoul-sticker.css', 'w', encoding='utf8', newline='\n') as f:
        f.write(css_content)

if __name__ == '__main__':
    main()
