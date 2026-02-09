import subprocess

def date():
    result = subprocess.run(['date', '+%Y-%m-%d %H:%M:%S'], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    result = date()
    print(result)