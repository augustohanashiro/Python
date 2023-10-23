import calendar

# Link Enunciado https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true


# Minha resolução 

# data = input()
# data_list = data.split(" ")
# dia = int(data_list[1])
# mes = int(data_list[0])
# ano = int(data_list[2])

# dia = calendar.weekday(ano,mes,dia)


# calendario = { 
#     "0":"MONDAY",
#     "1":"TUESDAY",
#     "2":"WEDNESDAY",
#     "3":"THURSDAY",
#     "4":"FRIDAY",
#     "5":"SATURDAY",
#     "6":"SUNDAY",
#  }

# for elemento in calendario:
#     if elemento == str(dia):
        # print(calendario[elemento]) 
    
# map ira aplicar uma função em cada item de um iteravel
MM, DD, YYYY = map(int,input().split())
print (calendar.day_name[calendar.weekday(YYYY,MM,DD)].upper())