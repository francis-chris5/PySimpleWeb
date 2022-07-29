#!C:/Users/franc/AppData/Local/Programs/Python/Python310/python.exe
print("Content-Type: text/html\n")

import cgi

## calculate the tip percentage and total bill
bill = cgi.FieldStorage()
price = float(bill['price'].value)
satisfaction = int(bill['satisfaction'].value)
tip = satisfaction / 345 + 0.03
total = price + price * tip
data = {"price": str(price), "satisfaction": str(satisfaction), "tip":format((tip * 100), ".2f"), "total":format(total, ".2f")}


## write the results into the html template
with open("results.html", "r") as htmlFile:
    buffer = ""
    for line in htmlFile:
        buffer += line
    for key in data.keys():
        if "<$ " + key + " $>" in buffer:
            buffer = buffer.replace("<$ " + key + " $>", data[key])
    print(buffer)
