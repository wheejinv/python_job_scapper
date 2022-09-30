days = ["mon", "tue"]

days.append("wed")

print(days)

# 튜플 - 불변성을 가짐.
dd = ("Mon", "Tue")

print(dd[1])
print(dd[-1])

# 딕셔너리
player = {
    'name': 'whee',
    'age': 12
}

print(player.get('name'))
print(player['name'])

player['money'] = 100000

print(player)