import re

def colorizer(textEditor, line, first, last, color):
    textEditor.pack(fill=BOTH)

    #Configure the text widget with certain color
    textEditor.tag_config("start"+str(line)+str(first)+str(last), foreground=color)
    textEditor.tag_add("start"+str(line)+str(first)+str(last), f"{line}.{first}", f"{line}.{last}")


def symbols(token):
    if re.match(r'^($', token): return True
    if re.match(r'^)$',token): return True
    if re.match(r'^+$',token): return True
    if re.match(r'^-$',token): return True
    if re.match(r'^*$',token): return True

    if re.match(r'^{$',token): return True
    if re.match(r'^}$',token): return True
    if re.match(r'^<$',token): return True
    if re.match(r'^>$',token): return True
    if re.match(r'^=$',token): return True
    if re.match(r'^!$',token): return True

def function(token):
    if re.match(r'^print$', token): return True
    if re.match(r'^enumerate$',token): return True
    if re.match(r'^int$',token): return True
    if re.match(r'^str$',token): return True

def word(token):
    if re.match(r'^class$', token): return True
    if re.match(r'^for$', token): return True
    if re.match(r'^if$', token): return True
    if re.match(r'^else$', token): return True
    if re.match(r'^elif$', token): return True
    if re.match(r'^in$',token): return True
    if re.match(r'^return$',token): return True
    if re.match(r'^def$',token): return True
    if re.match(r'^global$',token): return True
    if re.match(r'^import$',token): return True
    if re.match(r'^from$',token): return True
    if re.match(r'^while$',token): return True
    
def string(reserved):
    return not re.match(reserved, r"['\w\d\ ']+")

def update(textEditor):
    reserved = ''
    first = 0

    for file_count, file_line in enumerate(textEditor.get('1.0', END).split('\n')):
        for last, str_line in enumerate(file_line):
            reserved += str_line
            print(reserved)
            
            if word(reserved):
                print(f'{file_count}:{first}:{last}')
                colorizer(file_count+1, first, last+1, '#fc0fc0')
                reserved = ''
                first = last+1
            
            
            elif function(reserved):
                print(f'{file_count}:{first}:{last}')
                colorizer(file_count+1, first, last+1, 'cyan')
                reserved = ''
                first = last+1
           # else:
           #     print(f'{file_count}:{first}:{last}')
           #     colorizer(file_count+1, first, last+1, 'yellow')
           #     reserved = ''
           #     first = last+1

        
            
         #   if symbols(reserved):
         #       reserved = ''
         #       first = last+1
            
            

        reserved = ''
        first = 0