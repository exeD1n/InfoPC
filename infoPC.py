import platform
import psutil
import cpuinfo
from cpuinfo import get_cpu_info

def information():
    print('На вашем компьютере установлена: ' + platform.system()) #Получаем название системы
    print('Полное название системы: ' + platform.platform()) #Получаем полное название системы
    print('Версия вашей системы: ' + platform.version()) #Получаем версию системы
    # print(get_cpu_info())
    print('\n')
    print('Бренд процессора компьютера: ' + get_cpu_info()['brand_raw']) #Название процессора
    print('Такатовая частота процессора: ' + get_cpu_info()['hz_actual_friendly']) #Тактовая частота процессора
    print('Процессор имеет физических ядер: ' + str(psutil.cpu_count(logical=False))) #Физ. ядра процессора
    print('Процессор имеет логических ядер: ' + str(psutil.cpu_count())) #Лог. ядра процессора
    print('\n')
    print('Машина имеет оперативную память: ' + str(round((psutil.virtual_memory()[0])/1073741824)) + ' GB')
    print('\n')
    print('Главный диск C имеет: ' + str(round(psutil.disk_usage('/')[0]/1073741824)) + ' GB')
    print(psutil.disk_io_counters(perdisk=False)[4]) #время чтения с диска, миллисекунды
    print(psutil.disk_io_counters(perdisk=False)[5]) #время записи на диск, миллисекунды
    
    
if __name__ == '__main__':
    information()