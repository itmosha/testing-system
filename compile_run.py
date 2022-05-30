import subprocess

def compile_cpp(code_text):
    file = open('code.cpp', 'w')
    file.write(code_text)
    file.close()

    process = subprocess.Popen(['g++', 'code.cpp'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if stderr == b'':
        return 0
    else:
        return str(stderr)[2:-1]

def run_cpp():
    process = subprocess.Popen(['./a.out'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    return 'No output' if str(stdout)[2:-1] == '' else str(stdout)[2:-1]