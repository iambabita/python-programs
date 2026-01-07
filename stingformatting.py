letter="Nepal is a {} country and it is Rich in {}."
Word="Nature"
empty="beautiful"
print (letter.format(empty,Word))
print(f"Nepal is a {empty} country and it is Rich in {Word}.")

txt="for only {price:.2f} dollars"
print(txt.format(price=49))

print(f"{2*30}")
print(type( f"{2*30}"))

print(f"Nepal is a {{empty}} country and it is Rich in {{Word}}.")