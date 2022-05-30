def check_for_keywords(code_text):
    flag1 = code_text.find('system')
    if flag1 != -1:
        return -1
    else:
        return 0