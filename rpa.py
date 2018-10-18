import re

lines = []
with open('./selenium.txt', 'r', encoding = 'utf8') as f:
    lines = f.readlines()


source = ''
source += "#coding : utf-8\n"
source += "from selenium import webdriver\n"
source += "from selenium.webdriver.chrome.options import Options\n"
source += "from selenium.webdriver.common.keys import Keys\n"
source += "\n"
source += "options = Options()\n"
source += "options.add_argument('disable-infobars')\n"
source += "\n"
source += "browser = webdriver.Chrome(chrome_options=options)\n"
source += "browser.maximize_window()\n"
source += "\n"

for i in range(len(lines)):
    lines[i] = re.sub(r'\.\.\..*', '', lines[i].replace('\n', ''))
    if 'open on' in lines[i]:
        lines[i] = re.sub(r'.*open on ', '', lines[i])
        source += "browser.get('" + lines[i] + "')\n"
        source += "\n"
    elif 'setWindowSize on' in lines[i]:
        lines[i] = re.sub(r'.*setWindowSize on ', '', lines[i])
    elif 'runScript on' in lines[i]:
        lines[i] = re.sub(r'.*runScript on ', '', lines[i])
        source += "browser.execute_script('" + lines[i] + "')\n"
        source += "\n"
    elif 'mouseOver on' in lines[i]:
        lines[i] = re.sub(r'.*mouseOver on ', '', lines[i])
    elif 'mouseOut on' in lines[i]:
        lines[i] = re.sub(r'.*mouseOut on ', '', lines[i])
    elif 'click on' in lines[i]:
        lines[i] = re.sub(r'.*click on ', '', lines[i])
        type = lines[i].split('=')[0]
        if type == 'css':
            css = lines[i].replace('css=', '')
            source += "browser.find_element_by_css_selector('" + css + "').click()\n"
            source += "\n"
        elif type == 'id':
            id = lines[i].replace('id=', '')
            source += "browser.find_element_by_id('" + id + "').click()\n"
            source += "\n"
    elif 'type on' in lines[i]:
        lines[i] = re.sub(r'.*type on ', '', lines[i])
        type = lines[i].split('=')[0]
        value = re.sub(r'.*with value ', '', lines[i])
        if type == 'css':
            css = lines[i].replace('css=', '')
            css = re.match(r'css=(.*) with', lines[i]).group(1)
            source += "browser.find_element_by_css_selector('" + css + "').send_keys('" + value + "')\n"
            source += "\n"
        elif type == 'id':
            id = re.match(r'id=(.*) with', lines[i]).group(1)
            source += "browser.find_element_by_id('" + id + "').send_keys('" + value + "')\n"
            source += "\n"
    elif 'sendKeys on' in lines[i]:
        lines[i] = re.sub(r'.*sendKeys on ', '', lines[i])
        type = lines[i].split('=')[0]
        value = re.sub(r'.*with value ', '', lines[i])
        key = re.match(r'.*\{(.*)\}', lines[i]).group(1)
        if key == 'KEY_ENTER':
            key = 'Keys.ENTER'
        
        if type == 'css':
            css = re.match(r'css=(.*) with', lines[i]).group(1)
            source += "browser.find_element_by_css_selector('" + css + "').send_keys(" + key + ")\n"
            source += "\n"
        elif type == 'id':
            id = re.match(r'id=(.*) with', lines[i]).group(1)
            source += "browser.find_element_by_id('" + id + "').send_keys(" + key + ")\n"
            source += "\n"

with open('./script.py', 'w', encoding = 'utf8') as f:
    f.write(source)



