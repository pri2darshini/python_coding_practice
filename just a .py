def hoop_count(n):
    switcher= {n >= 10: "Great, now move on to tricks",
            n < 10: "Keep at it until you get it"}
    return switcher.get(1)


print(hoop_count(1))
print(hoop_count(11))
