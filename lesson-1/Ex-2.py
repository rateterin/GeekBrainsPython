time_in_seconds = int(input('Type time in seconds: '))
res_seconds = str(time_in_seconds % 60).zfill(2)
res_minutes = time_in_seconds // 60
res_hours = str(res_minutes // 60).zfill(2)
res_minutes = str(res_minutes % 60).zfill(2)
print(f'{res_hours}:{res_minutes}:{res_seconds}')
