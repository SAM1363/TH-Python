
all_restaurants = [
    "Taco City",
    "Burgertown",
    "Tacovilla",
    "Hotdog station",
    "House of tacos",
]


def tacos_only(restaurants):
    taco_joints = restaurants.copy()
    for taco_joint in taco_joints.copy():
        if "taco" not in taco_joint.lower():
            taco_joints.remove(taco_joint)
    return taco_joints

print(tacos_only(all_restaurants))

print(all_restaurants)

# 'taco' というキーワードがあるものだけプリントしたい
for each in all_restaurants:
    if each == 'taco'.lower():
        print(each)
