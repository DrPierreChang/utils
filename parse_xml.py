from bs4 import BeautifulSoup


with open("xml_example.xml", "r") as file:
    soup = BeautifulSoup(file, "xml")
    if soup.find("para"):
        print(soup.para.text)
    else:
        print("para is not found")
