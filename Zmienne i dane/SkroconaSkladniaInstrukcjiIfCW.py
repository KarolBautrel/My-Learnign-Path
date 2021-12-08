

price = 123
bonus = 23
bonus_granted = True


bonusPrice = (price - bonus) if bonus_granted else price

print(bonusPrice)


rating = 4


rate = print("Very good") if rating == 5 else print(
    "Good") if rating == 4 else print("Weak")


today_weekday = "niedziela"


print("Pomagam mamie") if today_weekday == "poniedzialek"else print("Robie pranie") if today_weekday == "wtorek" else print("pranie") if today_weekday == "sroda" else print(
    "dyzur") if today_weekday == "czwartek" else print("dwa zebrania") if today_weekday == ("piatek") else print("lekcje") if today_weekday == "sobota"else print("Niedziala dla nas")
