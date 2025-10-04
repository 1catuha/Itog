from smartphone import Smartphone


catalog = [
    Smartphone(brand="Nokia", model="6300", number="+79148860077"),
    Smartphone(brand="Philips", model="Xenium E590", number="+79098994545"),
    Smartphone(brand="Sony", model="Xperia 1 III", number="+79243126851"),
    Smartphone(brand="Samsung", model="Galaxy S25 Ultra",
               number="+79038482413"),
    Smartphone(brand="Huawei", model="Nova 13i", number="+79684575200")
]


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
