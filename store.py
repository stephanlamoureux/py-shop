melee = {
    "name": "Melee Shop",
    "baseball bat": 70,
    "butterfly knife": 20,
    "scythe": 100,
    "katana": 500,
    "golf club": 15,
}
guns = {
    "name": "Gun Store",
    "rifle": 400,
    "pellet gun": 3,
    "pistol": 150,
    "shotgun": 75,
    "machine gun": 750,
}
tailor = {
    "name": "Tactical Tailor",
    "night vision": 100,
    "kevlar helmet": 250,
    "bullet proof vest": 400,
    "assault gloves": 100,
}

credits = 10000
cart = {}
total = 0
inventory = {**melee, **guns, **tailor}
inventory.pop("name")

print("---------------------------")
print(f'Starting Inventory: \n[{", ".join(list(sorted(inventory)))}]')
print("---------------------------\n")

for shop in (melee, guns, tailor):
    print(
        f'Welcome to the {shop["name"]}. What would you like to buy? ("exit" to leave):'
    )
    del shop["name"]
    print(f'items: {", ".join(list(shop))}')
    buy_item = input("> ").lower()
    print("---------------------------\n")

    if buy_item == "exit":
        continue
    elif buy_item not in shop:
        continue
    else:
        cart.update({buy_item: shop.pop(buy_item)})
        inventory.pop(buy_item)
        items_bought = ", ".join(list(cart.keys()))
        total += sum(cart.values())

credits = credits - total

if len(cart) == 0:
    items_bought = "no items"
print(
    f"You purchased {items_bought}, for {total} credits. You have {credits} gold remaining.\n\nPrepare for the horde!!!\n"
)

print("---------------------------")
print(f'Final Inventory: \n[{", ".join(list(sorted(inventory)))}]')
print("---------------------------")
