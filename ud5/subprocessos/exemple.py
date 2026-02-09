import subprocess

result = subprocess.run(['tr', 'a-z', 'A-Z'], input='hola mon', capture_output=True, text=True)
print(result.stdout)