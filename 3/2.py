def get_info(name, last_name, year_of_birthday, city, email, phone):
    print(
        f"{last_name} {name}, {year_of_birthday} года рождения, "
        f"проживающий(ая) в городе{city}, {email}, {phone}"
    )


get_info(
    name="Чье",
    last_name="Чья",
    year_of_birthday="2000",
    city="Москва",
    email="em@ai.l",
    phone="123-45-67",
)
