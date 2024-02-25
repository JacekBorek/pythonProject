import os
import time
import datetime

ts1 = time.time()
print(ts1)
print(os.getcwd())
os.chdir('C:\\Users\\jacbo\\desktop\\')
print(os.getcwd())
# print(os.environ)
# time.sleep(1)
os.mkdir('Badanie czasu')
# time.sleep(2)
os.rename('Badanie czasu', 'Czas')
# time.sleep(2)
os.rmdir('Czas')
# os.mkdir('Nowy folder z zajęć 2')
# os.rename('Nowy folder z zajęć 2','Jutro bedzie futro')

# os.rmdir('Nowy folder z zajęć')
ts2 = time.time()
print(f'Czas trwania tworzenia folderu: {ts2-ts1}')
print('C:\\Users\\jacbo\\desktop\\ip.txt')
# os.system('cmd /c "ipconfig"')
print(datetime.datetime.now())