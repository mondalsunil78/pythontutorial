# Create 3 variables to store street, city and country, now create address variable to store entire address.
# Use two ways of creating this variable, one using + operator and the other using f-string. Now
# Print the address in such a way that the street, city and country prints in a separate line

street = "126 parkstreet"
city = "kolkata"
country = "india"
address = street + "\n" + city+"\n" + country
print("address using + operator", address)
address = f'{street}\n{city}\n{country}'
print("address using f-string", address)




