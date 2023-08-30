# TASK 1
city = "London"
print(city)

# TASK 2
city = "Berlin"
population = str(3645000)
print(city +(":") + " "+population)

# TASK 3
city = "London (True)"
population = str(9000000)
print("City:", city)
print("Population:", population)

# TASK 4
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
words = text.split( )
for word in words:
    print(word)
result = text.index("capital")
print("capital: ", result)

# TASK 5
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
print(text.split())

# TASK 6
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
print(text.replace("capital", "capital of Germany"))