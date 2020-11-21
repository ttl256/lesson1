d = {
    "city": "Moscow",
    "temperature": 20
}

print(d["city"])
#d["temperature"] = 
d["temperature"] -= 5
print(d["temperature"])

print(d)

print(d.get("coutry", "Russia"))

d["date"] = "27.05.2019"
print(d)
print(len(d))