import urllib.request
import urllib.parse
import requests
import os

def down(api_url_old, api_flag, ab, zu):
	if ab != "":
		api_url_old = api_url + "&older=" + ab
	while True:

		get_data = requests.get(api_url_old).json()

		id_nr = 0
		url_nr = 0
		while True:
			try:
				id = get_data["items"][id_nr]["id"]
			except IndexError:
				break
			url = get_data["items"][url_nr]["image"]
			end = url.split('.')[1]
			full_name = str(id) + "." + end
			full_url = "http://pr0gramm.com/data/images/" + url
			dir_name = os.path.join(".\\down\\", full_name)
			if not os.path.exists(dir_name):
				urllib.request.urlretrieve(full_url, dir_name)
			else:
				print("Übersprungen")
			print("id: " + str(id))
			print("url: " + url)
			print(end)
			print(" ")
			id_nr = id_nr + 1
			url_nr = url_nr + 1
			if zu == id:
				print("Am ende von " + zu +" angekommen")
				break


		atEnd = get_data["atEnd"]
		if atEnd == True:
			print("am Ende angekommen/keine Bilder vorhanden mit diesem Parametern")
			break
		if zu == id:
			break
		api_url_old = api_url + "&older=" + str(id)


main_api = "http://pr0gramm.com/api/items/get?self=true"
print("Viel spaß mit dem Pr0gramm von D3fus")
user = input("Username? (Leer lassen für ganz Pr0) ")
mode = input("Favs herunterladen von "+user+" = 1; Uploads herunterladen von "+user+" = 2? (Enter für ganz Pr0) ")
if mode == "":
	mode = "1"

flag = input("Filer sfw = 1; nsfw = 2; nsfl = 4; nsfp = 8 (zugelassen 1 bis 15; Enter = standart 15 alles) ")
tag = input("Tags eingeben; Enter alle ")
ab = input("ab welchen Upload? (Enter ab neuste) ")
zu = int(input("zu welchen Upload? (0 für alle) "))

if zu == None:
	zu = 0

if flag == "":
	flag = "15"

if not os.path.exists(".\\down\\"):
    os.makedirs(".\\down\\")

if mode == "1":
	api_flag = main_api + "&flags=" + flag
	api_user = api_flag + "&likes=" + user
	api_url = api_user + "&tags=" + tag.replace(" ", "%20")
	api_url_old = api_url
	down(api_url_old, api_flag, ab, zu)

elif mode == "2":
	api_flag = main_api + "&flags=" + flag
	api_user = api_flag + "&user=" + user
	api_url = api_user + "&tags=" + tag.replace(" ", "%20")
	api_url_old = api_url
	down(api_url_old, api_flag, ab, zu)
