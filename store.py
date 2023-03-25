freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

purse = 1000
cart = {}
total = 0
department_store = {**freelancers, **antiques, **pet_shop}
department_store.pop('name')

print('------------------------')
print(f'Starting inventory is: \n{sorted(department_store.items())}')
print('------------------------')

for shop in (freelancers,antiques,pet_shop):
    print(f'Welcome to the {shop["name"]}! What would you like to buy? ("exit" to leave store)')
    del shop['name']
    print(f'items: [{", ".join(list(shop))}]')
    buy_item = input('> ').lower()


    print('------------------------')
    if buy_item == 'exit' or buy_item not in shop:
        continue
    else:
        cart.update({buy_item:shop.pop(buy_item)})
        department_store.pop(buy_item)
        items_bought = ", ".join(list(cart.keys()))
        total += sum(cart.values())

purse = purse - total

if len(cart) == 0:
    items_bought = "no items"
print(f'You purchased {items_bought}, for {total} gold. You have {purse} gold remaining.')

print('------------------------')
print(f'Final inventory is: \n{sorted(department_store.items())}')
print('------------------------')