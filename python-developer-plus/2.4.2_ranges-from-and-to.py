print('Это первый этаж.')
# Первый этаж построен, начинайте строить со второго
for i in range(2, 11):
    # Здесь вместо многоточий
    # вставьте номер текущего этажа,
    # вычислите и вставьте номер предыдущего этажа.
    print('А это', str(i), 'этаж, он на один выше, чем этаж', str(i-1))
