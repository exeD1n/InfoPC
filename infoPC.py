import platform
import psutil
from cpuinfo import get_cpu_info
import GPUtil
import wmi

def information():
    computers = wmi.WMI()
    print('Имя пользователя компьютера: ' + psutil.users()[0][0]) #Получаем имя пользователя компьютера
    print('На вашем компьютере установлена: ' + platform.system()) #Получаем название системы
    print('Полное название системы: ' + platform.platform()) #Получаем полное название системы
    print('Версия вашей системы: ' + platform.version()) #Получаем версию системы
    # print(get_cpu_info()) Получение всей инфы о процессоре 
    print('\n')
    print('Бренд процессора компьютера: ' + get_cpu_info()['brand_raw']) #Название процессора
    print('Такатовая частота процессора: ' + get_cpu_info()['hz_actual_friendly']) #Тактовая частота процессора
    print('Процессор имеет физических ядер: ' + str(psutil.cpu_count(logical=False))) #Физ. ядра процессора
    print('Процессор имеет логических ядер: ' + str(psutil.cpu_count())) #Лог. ядра процессора
    print('\n')
    print('Материнская плата в компьютере' + computers.Win32_BaseBoard()[0].Product) #Получаем название материнской платы
    print('Компьютер имеет оперативную память: ' + str(round((psutil.virtual_memory()[0])/1073741824)) + ' GB') #Получаем весь объем оперативной памяти ПК
    print('Главный диск C имеет: ' + str(round(psutil.disk_usage('/')[0]/1073741824)) + ' GB') #Получаем объем главного жесткого диска
    gpu_info = computers.Win32_VideoController()[0]
    # print(gpu_info) Получение всей инфы о видеокарте
    print('Видеокарта в компьютере: ' + gpu_info.Caption) #Получаем название видеокарты
    
    
    
if __name__ == '__main__':
    information()