cat > stepik/module-02-io/2.3-sep-end/task-02.py << 'EOF'
# Stepik 2.3, задача 2: считать имя и вывести 'Привет, <имя>!' без переноса строки

name=input()
print(f'Привет,', name, end='!')
