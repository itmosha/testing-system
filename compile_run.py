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
        print('Compiltaion: compiled without errors')
        return 0
    else:
        print(f'Compiltaion: compilation error: {str(stderr)[2:-1]}')
        return str(stderr)[2:-1]

def run_cpp():
    process = subprocess.Popen(['./a.out'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    return 'No output' if str(stdout)[2:-1] == '' else str(stdout)[2:-1]