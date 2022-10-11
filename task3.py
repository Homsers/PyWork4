a = ("Съешь ещё этих мягких французских булок, да выпей чаю.")
print(a)
print(a.translate({ord(i): "" for i in 'абв'}))

