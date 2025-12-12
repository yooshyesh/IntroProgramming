temps = [19.5, 25.0, 22.1, 17.9, 21.3]
allowed = (18.0, 24.0)
valid_temps = []

for i in temps:
    if i < allowed[0] or i > allowed[1]:
        print(f"Temp warning {i} is outside of {allowed}")
    else:
        valid_temps.append(i)

ok_percentage = 100 / len(temps) * len(valid_temps)
print(f"Percentage: {ok_percentage} %")