import requests
import wget

req = requests.get("https://www.minecraft.net/en-us/download/server/")

#HTML Format
string_request_web = req.text

# locates where .jar is
jar_location = string_request_web.find('.jar')

# approcimates where the link could possibly be
estimate_location_of_link = string_request_web[ (jar_location - 100) : (jar_location + 20)]

#link is made but it is on a list
exact_URL_list = estimate_location_of_link.split('"')[1::2]

# link converted from list to String
URL = "".join(map(str,exact_URL_list ))

# download jar
wget.download(URL, "E:/") 
print("Success")
