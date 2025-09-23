import requests
import urllib.request
import os.path
import shutil
import json
import sys

# Only needed fields: name and cards
# and within card: 
# card.details.coloridentity
# card.cmc
# card.type_line
# card.details.name
# card.board
#also add card.url

def make_roto_file():

	cubestr = ""

	jsonurl = "https://raw.githubusercontent.com/rudyards/Revolution-Manifesto/refs/heads/main/frontend/public/cards/AllSetsEternal.json"
	r = requests.get(jsonurl)

	s = str(r.content)

	allsets = requests.get(jsonurl).json()

	preamble = """
	{
		"name": "Revolution Eternal Rotisserie",
		"cards": {"mainboard": [
	"""

	cubestr += preamble

	names = []

	setcodes = ["TWI", "KDT", "ERR", "CCR", "CNY", "CYB", "OLD", "TRX", "POP", "DOV", "BLR", "KSV", "KRS", "VRD", "SVG", "GQC", "KUT", "MON", "SRC", "VST"]
	firstcard = True
	for i in range(len(setcodes)):
		cards = allsets["data"][setcodes[i]]["cards"]
		for card in cards:
			if "Basic" in card["type"]:
				continue
			if "b" in card["number"]:
				continue
			if "PRO" in card["name"]:
				continue
			if "★" in card["name"]:
				continue
			if "(" in card["name"] and not "()" in card["name"]:
				continue
			if "On Borrowed Time" in card["name"]:
				continue
			if len(card["colorIdentity"]) == 0:
				colidtext = "[]"
			else:
				colidtext = "[\"" + '","'.join(card["colorIdentity"]) + "\"]"
			cardname = card["name"].replace("\"", "\\\"").replace("_" + setcodes[i], "")
			if cardname in names:
				continue
			names.append(cardname)
			if firstcard:
				firstcard = False
			else:
				cubestr += ","
			cardtext = f"""
			{{
				"cmc": {card["convertedManaCost"]},
				"type_line": "{card["type"].replace("—", "-")}",
				"board": "mainboard",
				"details": {{
					"name": "{cardname}",
					"color_identity": {colidtext},
					"mana_cost": "{card["manaCost"]}",
					"set_code": "{setcodes[i]}"
				}}
			}}
			"""	
			try:
				cubestr += cardtext
			except UnicodeEncodeError:
				sys.exit()
				
	cubestr += "]\n}\n}"
	with open(f"custom/cubefile.json", "w", encoding="utf-8") as f:
		f.write(cubestr)