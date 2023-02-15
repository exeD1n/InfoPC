import platform
import psutil
import cpuinfo
from cpuinfo import get_cpu_info

def information():
    print('На вашем компьютере установлена: ' + platform.system()) #Получаем название системы
    print('Полное название системы: ' + platform.platform()) #Получаем полное название системы
    print('Версия вашей системы: ' + platform.version()) #Получаем версию системы
    print(get_cpu_info())
    print('Бренд процессора компьютера: ' + get_cpu_info()['brand_raw'])
    
    
if __name__ == '__main__':
    information()