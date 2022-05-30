def check_for_keywords(code_text):
    flags = [code_text.find('system'),
             code_text.find('stdexcept'),
             code_text.find('pstream'),
             code_text.find('atlstr')]

    if sum(flags) != -len(flags):
        print('Parsing: found system commands')
        return -1
    else:
        return 0