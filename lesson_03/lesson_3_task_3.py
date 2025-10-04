from address import Address
from mailing import Mailing

to_address = Address("681000", "Komsomolsk-on-Amur", "Kirova", "54", "1")
from_address = Address("680000", "Khabarovsk", "Lenina", "51", "12")
mailing = Mailing(to_address, from_address, "151,00 рублей", "6800002548721")


print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment}, "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost}."
    )
