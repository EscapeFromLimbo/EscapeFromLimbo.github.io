import requests
import urllib.request
import os.path
import shutil
import json
import sys

'''
git push https://EscapeFromLimbo@github.com/EscapeFromLimbo/EscapeFromLimbo.github.io.git

		<card>
			<name>Zakros Stompers</name>
			<text>Menace
Whenever you sacrifice a permanent, exile the top card of your library. Until the end of your turn, you may play that card.</text>
			<prop>
				<type>Creature — Giant Warrior</type>
				<cmc>5</cmc>
				<manacost>3RR</manacost>
				<maintype>Creature</maintype>
				<format-revolution-eternal>legal</format-revolution-eternal>
				<layout>normal</layout>
				<pt>5/5</pt>
				<side>front</side>
				<format-revolution-brawl>legal</format-revolution-brawl>
				<coloridentity>R</coloridentity>
				<format-revolution>legal</format-revolution>
				<colors>R</colors>
				<format-revolution-eternal-pauper>not legal</format-revolution-eternal-pauper>
			</prop>
			<set num="163" rarity="uncommon">TRX</set>
			<tablerow>2</tablerow>
		</card>
'''

'''
		{
			"card_name": "Ambitious Angel",
			"color": "W",
			"rarity": "common",
			"type": "Creature \u2014 Angel Soldier Archer",
			"number": 1,
			"color_identity": "W",
			"cost": "{W}",
			"rules_text": "",
			"flavor_text": "[i][/i]",
			"pt": "1/1",
			"special_text": "Flying\nLevel up {3}{W}{W} [i]({3}{W}{W}: Put a level counter on this. Level up only as a sorcery.)[/i]\n[level 1-2] Flying\n[level 3+] Flying",
			"shape": "leveler",
			"set": "ERR",
			"loyalty": "",
			"artist": "Eddy Shinjuku",
			"notes": "Enchantments 1/1 3/2\nLevel Up 1/1 2/2\nCache 0/0.5 2/2\nError 1/1\nProgram 2/2\nblink 0.5/0.5 3.5/3.5\nTokens 1/1 1.5/2\nRegion: The Stack. Brutalist\n\n1-5 2/2 flier or 2-5 4/4 flier?\n\nart4"
		},
'''
'''
https://raw.githubusercontent.com/rudyards/Revolution-Manifesto/refs/heads/main/frontend/public/cards/OLD/256.jpg
https://raw.githubusercontent.com/rudyards/Revolution-Manifesto/refs/heads/main/frontend/public/cards/OLD/Story%20Spotlight.jpg

<number>_cardname.jpg
'''
'''
{
	"name": "Errors in the Weft",
	"formats": "",
	"trimmed": "y",
	"image_type": "jpg",
	"cards": [
	...
	],
	"version": 1
}
'''
'''
ERR-files/ERR.json
ERR-files/img/1_Ambitious Angel.jpg
'''
'''
import urllib.request

urllib.request.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")
'''
'''
		<card>
			<name>Daybreak Rider</name>
			<text>Flying
When Daybreak Rider enters, you may bless another target creature. (Create a token copy of this creature's blessing attached to that permanent.)</text>
			<prop>
				<type>Creature — Archon</type>
				<cmc>5</cmc>
				<manacost>4W</manacost>
				<maintype>Creature</maintype>
				<format-revolution-eternal>legal</format-revolution-eternal>
				<layout>modal_dfc</layout>
				<pt>3/3</pt>
				<side>front</side>
				<format-revolution-brawl>legal</format-revolution-brawl>
				<coloridentity>W</coloridentity>
				<format-revolution>legal</format-revolution>
				<colors>W</colors>
				<format-revolution-eternal-pauper>legal</format-revolution-eternal-pauper>
			</prop>
			<set num="13a" rarity="common">TRX</set>
			<related attach="transform">The Sun's Blessing</related>
			<tablerow>2</tablerow>
		</card>
		<card>
			<name>The Sun's Blessing</name>
			<text>(You may also cast this side from your hand.)
Flash
Enchant creature
Enchanted creature gets +2/+2.</text>
			<prop>
				<type>Enchantment — Aura Blessing</type>
				<cmc>3</cmc>
				<manacost>2W</manacost>
				<maintype>Enchantment</maintype>
				<format-revolution-eternal>legal</format-revolution-eternal>
				<layout>modal_dfc</layout>
				<side>back</side>
				<format-revolution-brawl>legal</format-revolution-brawl>
				<coloridentity>W</coloridentity>
				<format-revolution>legal</format-revolution>
				<colors>W</colors>
				<format-revolution-eternal-pauper>legal</format-revolution-eternal-pauper>
			</prop>
			<set num="13b" rarity="common">TRX</set>
			<related attach="transform">Daybreak Rider</related>
			<tablerow>1</tablerow>
		</card>

		{
			"card_name": "Daybreak Rider",
			"color": "W",
			"rarity": "common",
			"type": "Creature \u2014 Archon",
			"number": 13,
			"color_identity": "W",
			"cost": "{4}{W}",
			"rules_text": "Flying\nWhen Daybreak Rider enters, you may bless another target creature. [i](Create a token copy of this creature's blessing attached to that permanent.)[/i]",
			"flavor_text": "[i][/i]",
			"pt": "3/3",
			"special_text": "",
			"shape": "modal double faced",
			"set": "TRX",
			"loyalty": "",
			"artist": "Pascal Quidault",
			"card_name2": "The Sun's Blessing",
			"color2": "W",
			"type2": "Enchantment \u2014 Aura Blessing",
			"cost2": "{2}{W}",
			"rules_text2": "[i](You may also cast this side from your hand.)[/i]\nFlash\nEnchant creature\nEnchanted creature gets +2/+2.",
			"flavor_text2": "[i][/i]",
			"pt2": "",
			"special_text2": "",
			"loyalty2": "",
			"artist2": "Francesca Resta",
			"notes": "!tag Theros\n!tag Heliod"
		},

<number>_cardname_front.jpg
<number>_cardname_back.jpg

https://escapefromlimbo.github.io/sets/ERR-files/img/134_Error%20Tide.jpg

https://escapefromlimbo.github.io/sets/CCR-files/img/258_Root%20Fossil_back.jpg

https://escapefromlimbo.github.io/sets/VRD-files/img/127_Calamity%20Smith%20In:%20The%20Gilded%20Heist_VRD.jpg

TODO:
Pull https://raw.githubusercontent.com/rudyards/Revolution-Manifesto/refs/heads/main/frontend/public/cards/AllSetsEternal.json instead

{
     "artist": "Magic Media",
     "convertedManaCost": 2,
     "faceConvertedManaCost": 2,
     "manaValue": 2,
     "faceManaValue": 2,
     "colors": [
      "B"
     ],
     "colorIdentity": [
      "B"
     ],
     "designer": "DrChipmunk",
     "flavor": "",
     "frameType": "normal",
     "frameVersion": "2015",
     "id": "Exorcist of Errors_ERR",
     "imageName": "exorcist of errors",
     "layout": "normal",
     "legalities": {
      "revolution": "Legal",
      "revolution-brawl": "Legal",
      "revolution-eternal": "Legal",
      "revolution-eternal-pauper": "Not Legal"
     },
     "manaCost": "{1}{B}",
     "multiverseid": 5363,
     "name": "Exorcist of Errors",
     "number": "95",
     "power": "2",
     "rarity": "rare",
     "relatedCards": {
      "spellbook": []
     },
     "subtypes": [
      "Human",
      "Warlock"
     ],
     "text": "When this creature enters, target player separates their hand into a face-up pile and a face-down pile. Choose one of those piles, reveal it, and choose a nonland card from it. Exile that card until this creature leaves the battlefield.",
     "toughness": "3",
     "type": "Creature — Human Warlock",
     "types": [
      "Creature"
     ],
     "uuid": "Exorcist of Errors_ERR"
    },



{
     "artist": "Lana Monx",
     "convertedManaCost": 1,
     "faceConvertedManaCost": 1,
     "manaValue": 1,
     "faceManaValue": 1,
     "colors": [
      "G"
     ],
     "colorIdentity": [
      "G"
     ],
     "designer": "Zangy",
     "flavor": "",
     "frameType": "dfc-normal-normal",
     "frameVersion": "2015",
     "id": "Seeker of New Horizons//Ilysian Guardian_TRX",
     "imageName": "seeker of new horizons",
     "layout": "modal_dfc",
     "legalities": {
      "revolution": "Legal",
      "revolution-brawl": "Legal",
      "revolution-eternal": "Legal",
      "revolution-eternal-pauper": "Not Legal"
     },
     "manaCost": "{G}",
     "multiverseid": 3792,
     "name": "Seeker of New Horizons // Ilysian Guardian",
     "faceName": "Seeker of New Horizons",
     "names": [
      "Seeker of New Horizons",
      "Ilysian Guardian"
     ],
     "side": "a",
     "number": "194a",
     "power": "0",
     "rarity": "rare",
     "relatedCards": {
      "spellbook": []
     },
     "subtypes": [
      "Satyr",
      "Scout"
     ],
     "text": "Whenever a Forest you control enters, put a +1/+1 counter on Seeker of New Horizons. Then you may remove four +1/+1 counters from among creatures you control. If you do, bless that land. (Create a token copy of this creature's blessing attached to that permanent.)",
     "toughness": "1",
     "type": "Creature — Satyr Scout",
     "types": [
      "Creature"
     ],
     "uuid": "Seeker of New Horizons//Ilysian Guardian_TRX-0",
     "otherFaceIds": [
      "Seeker of New Horizons//Ilysian Guardian_TRX-1"
     ]
    },
{
     "artist": "Rousteinire",
     "convertedManaCost": 3,
     "faceConvertedManaCost": 3,
     "manaValue": 3,
     "faceManaValue": 3,
     "colors": [
      "G"
     ],
     "colorIdentity": [
      "G"
     ],
     "designer": "Zangy",
     "flavor": "",
     "frameType": "dfc-normal-normal",
     "frameVersion": "2015",
     "id": "Seeker of New Horizons//Ilysian Guardian_TRX",
     "imageName": "ilysian guardian",
     "layout": "modal_dfc",
     "legalities": {
      "revolution": "Legal",
      "revolution-brawl": "Legal",
      "revolution-eternal": "Legal",
      "revolution-eternal-pauper": "Not Legal"
     },
     "manaCost": "{2}{G}",
     "multiverseid": 3792,
     "name": "Seeker of New Horizons // Ilysian Guardian",
     "faceName": "Ilysian Guardian",
     "names": [
      "Seeker of New Horizons",
      "Ilysian Guardian"
     ],
     "side": "b",
     "number": "194b",
     "rarity": "rare",
     "relatedCards": {
      "spellbook": []
     },
     "subtypes": [
      "Aura",
      "Blessing"
     ],
     "text": "Enchant land\nEnchanted land is a 4/4 Dryad creature with reach, vigilance, and haste. It's still a land.\nWhen enchanted land dies, return it to its owner's hand.",
     "type": "Enchantment — Aura Blessing",
     "types": [
      "Enchantment"
     ],
     "uuid": "Seeker of New Horizons//Ilysian Guardian_TRX-1",
     "otherFaceIds": [
      "Seeker of New Horizons//Ilysian Guardian_TRX-0"
     ]
    },

'''
class Card(object):
	pass

def pull_all_images(play_rate_table):

	jsonurl = "https://raw.githubusercontent.com/cajunwritescode/Revolution/refs/heads/main/AllSetsEternal.json"
	r = requests.get(jsonurl)
	#print(str(r.content))
	s = str(r.content)
	#print(s)
	#print(r.encoding)
	allsets = requests.get(jsonurl).json()

	tokenurl = "https://raw.githubusercontent.com/cajunwritescode/Revolution/refs/heads/main/tokens.xml"
	r = requests.get(tokenurl)
	#print(str(r.content))
	alltokens = str(r.content)
	#print(s)

	cubefilename = "custom/Curator's Cube Peasant List.txt"
	f = open(cubefilename, "r", encoding='utf-8')

	cubecards = [l.split('"name": "')[1].split('"')[0] for l in f.readlines() if '"name"' in l]

	setnames = ["Exalts of Twiltrie", "Theros: Age of Trax", "Cliques of Nylin", "Errors in the Weft", "Chikyu: Chaos Rains", "Cybaros", "Awakening in Oldun", "Kitsuo: Dusk of Time",
		"Hyperpop", "Duelists of Vereaux", "Blood Like Rivers", "Karslav", "Karsus", "Viridian's Last Mission", "Svergard", "Ghariv, the Quaking City",
		"Kuutalya", "Monsters of Chikyu", "Secrets of the River Cities", "Vastuum", "Revolution Renegades", "Revolution Planechase"]
	setcodes = ["TWI", "KDT", "ERR", "CCR", "CNY", "CYB", "OLD", "TRX", "POP", "DOV", "BLR", "KSV", "KRS", "VRD", "SVG", "GQC", "KUT", "MON", "SRC", "VST", "REV", "PLANE"]
	setcards = []
	num_sets = 22
	for i in range(num_sets):
		setcards.append([])

	cardfilenames = []

	for code in setcodes:
		if not os.path.exists(f"sets/{code}-files"):
			os.makedirs(f"sets/{code}-files")
		if not os.path.exists(f"sets/{code}-files/img"):
			os.makedirs(f"sets/{code}-files/img")

	def extract(text, tag):
		if f"<{tag}>" in text and f"</{tag}>" in text:
			return text.split(f"<{tag}>")[1].split(f"</{tag}>")[0]
		return ""

	#print(allsets["meta"])
	#print(allsets["data"]["VST"])
	for i in range(len(setcodes)):
		cards = allsets["data"][setcodes[i]]["cards"]
		setnames[i] = allsets["data"][setcodes[i]]["name"]
		for card in cards:
			c = Card()
			front = False
			back = False
			c.form = "normal"
			c.backside = ""
			c.card_name = card["name"]
			if "faceName" in card:
				c.card_name = card["faceName"]
				for name in card["names"]:
					if name != c.card_name:
						c.backside = name
			c.card_name = c.card_name.replace("// ", "").replace("é", "e").replace("“", "").replace("”", "").replace(":", "").replace("★", "(shiny)").replace("\"", "")
			c.backside = c.backside.replace("// ", "").replace("é", "e").replace("“", "").replace("”", "").replace(":", "").replace("★", "(shiny)").replace("\"", "")
			c.color = ""
			c.color_identity = ""
			for col in "WUBRG":
				if col in card["colors"]:
					c.color = c.color + col
				if col in card["colorIdentity"]:
					c.color_identity = c.color_identity + col
			c.rarity = card["rarity"]
			c.type = card["type"]
			c.number = card["number"]
			fetchnumber = c.number
			if "Story" in c.number:
				c.number = "136"
			if "a" in c.number:
				c.number = c.number.replace("a", "")
				front = True
				c.form = "front"
			if "b" in c.number:
				c.number = c.number.replace("b", "")
				back = True
				c.form = "back"
			c.cost = card["manaCost"]
			c.rules_text = card["text"].replace("\n", "\\n").replace("“", "\\\"").replace("”", "\\\"").replace("—", "-").replace("’", "'").replace("​", "")
			c.flavor_text = card["flavor"].replace("\n", "\\n").replace("“", "\\\"").replace("”", "\\\"").replace("—", "-").replace("’", "'").replace("​", "").replace("\\>", "\\\\>")
			c.pt = ""
			if "power" in card:
				c.pt = f"{card['power']}/{card['toughness']}"
			c.loyalty = ""
			if "loyalty" in card:
				c.loyalty = card["loyalty"]
			c.artist = card["artist"].replace("\"","")
			if card["frameType"] == "split":
				if card["side"] == "b":
					continue
				for othercard in cards:
					if othercard["name"] == card["name"] and othercard["faceName"] != card["faceName"]:
						card2 = othercard
				c.form = "normal"
				c.card_name = card["name"].replace("// ", "")
				c.color = c.color_identity
				c.cost = card["manaCost"] + " // " + card2["manaCost"]
				c.rules_text = card["text"].replace("\n", "\\n") + "\\n\\n---\\n\\n" + card2["text"].replace("\n", "\\n")
				if card["artist"] != card2["artist"]:
					c.artist = card["artist"] + ", " + card2["artist"]

			#print(f"{setcodes[i]} #{c.number}: {c.card_name}")
			card_exists = False
			for card in setcards[i]:
				if card.card_name == c.card_name:
					card_exists = True
			if not card_exists:
				cardfilename = f"sets/{setcodes[i]}-files/img/{c.number}_{c.card_name}.jpg"
				if front:
					cardfilename = f"sets/{setcodes[i]}-files/img/{c.number}_{c.card_name}_front.jpg"
				if back:
					cardfilename = f"sets/{setcodes[i]}-files/img/{c.number}_{c.backside}_back.jpg"
				c.cardfilename = cardfilename
				
				cardfilenames.append(cardfilename)
				if not os.path.isfile(cardfilename):
					print(f"Downloading {setcodes[i]} #{c.number}: {c.card_name} at {c.cardfilename}")
					#urllib.request.urlretrieve(f"https://raw.githubusercontent.com/rudyards/Revolution-Manifesto/refs/heads/main/frontend/public/cards/{setcodes[i]}/{fetchnumber}.jpg".replace(" ", "%20"), cardfilename)
					urllib.request.urlretrieve(f"https://raw.githubusercontent.com/cajunwritescode/Revolution/refs/heads/main/img/{setcodes[i]}/{fetchnumber}.jpg".replace(" ", "%20"), cardfilename)
				setcards[i].append(c)

	"""
	<card>
	 <name>Haste Gadget VRD</name>
	 <text>Equipped creature has haste.
	Equip {2}</text>
	 <colors></colors>
	 <type>Token Artifact — Equipment</type>
	 <token>1</token>
	 <tablerow>1</tablerow>
	 <set num="VRD18" rarity="token">tokens</set>
	</card>
	            "card_name": "Treasure ERR",
	            "color": "",
	            "rarity": "common",
	            "type": "Token Artifact \u2014 Treasure",
	            "number": 24,
	            "color_identity": "C",
	            "cost": "",
	            "rules_text": "{T}, Sacrifice this artifact: Add a mana of any color.",
	            "flavor_text": "[i][/i]",
	            "pt": "",
	            "special_text": "",
	            "shape": "token",
	            "set": "ERR",
	            "loyalty": "",
	            "artist": "TheBakaArts",
	            "notes": "!!exportname Treasure ERR\n!\nart4"
	"""
	#https://raw.githubusercontent.com/rudyards/Revolution-Manifesto/refs/heads/main/frontend/public/cards/tokens/SRC1.jpg
	tokens = alltokens.split("<card>")
	for token in tokens:
		#print(token)
		if not "set num=\"" in token:
			continue
		if "set num=\"REV" in token and not "Puzzlebox" in token and not "Angel" in token and not "OVERFLOW" in token:
			continue
		if "set num=\"PLANE" in token:
			continue
		if not "<type>Token" in token and not "Legendary" in token:
			continue
		c = Card()
		c.card_name = extract(token, "name").replace("\\", "").replace("// ", "").replace("é", "e").replace("“", "").replace("”", "").replace(":", "").replace("★", "(shiny)").replace("\"", "")
		c.rules_text = extract(token, "text").replace("\n", "\\n").replace("“", "\\\"").replace("”", "\\\"").replace("—", "-").replace("•", "::").replace("’", "'").replace("​", "").replace("é", "e").replace("\\xe2\\x80\\x94", "-").replace("\\'", "'").replace("\\xe2\\x80\\x9c", "\\\"").replace("\\xe2\\x80\\x9d", "\\\"")
		c.color = extract(token, "colors")
		c.color_identity = ""	
		c.rarity = "common"
		c.type = extract(token, "type").replace("—", "-").replace("\\xe2\\x80\\x94", "-")
		if "Token" not in c.type:
			c.type = "Token " + c .type
		fetchnumber = token.split( "num=\"")[1].split("\"")[0]
		setcode = "XXX"
		c.number = fetchnumber
		for code in setcodes:
			if fetchnumber.startswith(code):
				setcode = code
				c.number = fetchnumber.replace(code, "")
		if "World Championship 2025" in c.number:
			c.number = 2025
		c.cost = ""
		c.flavor_text = ""
		c.pt = extract(token, "pt").replace("\\xe2\\x98\\x85", "X")
		c.loyalty = extract(token, "loyalty")
		c.artist = ""
		c.form = "token"
		for i in range(num_sets):
			if setcodes[i] == setcode:
				card_exists = False
				for card in setcards[i]:
					if card.card_name == c.card_name:
						card_exists = True
				if not card_exists:
					cardfilename = f"sets/{setcodes[i]}-files/img/{c.number}t_{c.card_name}.jpg"
					c.cardfilename = cardfilename
					cardfilenames.append(cardfilename)
					try:
						if not os.path.isfile(cardfilename):
							print(f"Downloading Token {setcodes[i]} #{c.number}: {c.card_name}")
							#urllib.request.urlretrieve(f"https://raw.githubusercontent.com/rudyards/Revolution-Manifesto/refs/heads/main/frontend/public/cards/tokens/{fetchnumber}.jpg".replace(" ", "%20"), cardfilename)
							urllib.request.urlretrieve(f"https://raw.githubusercontent.com/cajunwritescode/Revolution/refs/heads/main/img/tokens/{fetchnumber}.jpg".replace(" ", "%20"), cardfilename)
							print(f"Download Successful: Saved to {cardfilename}")
						setcards[i].append(c)
					except:
						pass

	print("Done pulling images")
	print("Deleting unnecessary images")

	for i in range(len(setcodes)):
		for filename in os.listdir(f"sets/{setcodes[i]}-files/img/"):
			file_exists = False
			for cardfilename in cardfilenames:
				if cardfilename.endswith(filename) and cardfilename.startswith(f"sets/{setcodes[i]}"):
					file_exists = True
					break
			if not file_exists:
				print(f"File without corresponding card: {filename}")
				os.remove(f"sets/{setcodes[i]}-files/img/{filename}")


	#for cubecard in cubecards:
	#	print(cubecard)

	for i in range(num_sets):
		print(f"Writing json for {setcodes[i]}")
		formatstring = "eternal"
		if i < 7:
			formatstring += ",standard,planechase"
		else:
			formatstring += ",rotated"
		#if card.card_name in cubecards:
		#	formatstring += ",cube"
		if setcodes[i] == "PLANE":
			formatstring = "planechase"
		prelude = f'''
		"name": "{setnames[i]}",
		"formats": "{formatstring}",
		"trimmed": "y",
		"image_type": "jpg",
		"cards": [
	'''
		postlude = '''
		],
		"version": 1
	'''
		setfile = "{" + prelude
		firstcard = True

		draftfile = """
	[Settings]
	{
		"name": "REPLACEWITHNAME",
		"withReplacement": false,
		"layouts": {
			"PlayBooster": {
				"weight": 1,
				"slots": {
	  				"Rare": 1,
	    			"Uncommon": 3,
	    			"Wildcard": 2,
	     			"Common": 7,
					"Land": 1,
					"Token": 1
				}
			},
		}
	}
	[CustomCards]
	[
	""".replace("REPLACEWITHNAME", setnames[i])
		#identify: are there common duals?
		#identify: are there mythics?

		commonNames = []
		uncommonNames = []
		rareNames = []
		mythicNames = []
		landNames = []
		basicNames = []
		tokenNames = []

		for card in setcards[i]:
			#print(card.card_name)

			play_rate = 0
			if card.card_name in play_rate_table:
				play_rate = play_rate_table[card.card_name]
			elif card.card_name.split("_")[0] in play_rate_table:
				play_rate = play_rate_table[card.card_name.split("_")[0]]
			elif card.card_name.split(" (")[0] in play_rate_table:
				play_rate = play_rate_table[card.card_name.split(" (")[0]]

			tags = '\\n!tag' + '\\n!tag '.join(formatstring.split(','))
			if card.card_name in cubecards:
				tags = tags + "\\n!tag cube"
				cubecards.remove(card.card_name)
			if card.card_name.replace("_" + setcodes[i], "") in cubecards:
				tags = tags + "\\n!tag cube"
				cubecards.remove(card.card_name.replace("_" + setcodes[i], ""))	
			if play_rate >= 100:
				tags = tags + "\\n!tag staple"	
			if play_rate >= 20:
				tags = tags + "\\n!tag playable"	
			if "_PRO" in card.card_name or "REV" in setcodes[i] or "(shiny)" in card.card_name or ")_" in card.card_name:
				tags = tags + "\\n!tag promo"
			if card.form in ["normal", "token"]:
				cardtext = f'''
					"card_name": "{card.card_name}",
					"color": "{card.color}",
					"rarity": "{card.rarity}",
					"type": "{card.type}",
					"number": {card.number},
					"color_identity": "{card.color_identity}",
					"cost": "{card.cost}",
					"rules_text": "{card.rules_text}",
					"flavor_text": "[i]{card.flavor_text}[/i]",
					"pt": "{card.pt}",
					"special_text": "",
					"shape": "{card.form}",
					"set": "{setcodes[i]}",
					"loyalty": "{card.loyalty}",
					"artist": "{card.artist}",
					"play_rate": {play_rate},
					"notes": "{tags}"
		'''
				drafttext = f'''
		{{
			"name": "{card.card_name.strip()}",
			"mana_cost": "{card.cost.replace('Vp', 'S')}",
			"type": "{card.type.split(' ')[0]}",
			"image": "{card.cardfilename.replace('sets/', 'https://EscapeFromLimbo.github.io/sets/')}",
			"colors": [{','.join(['"' + k + '"' for k in card.color])}],
			"set": "{setcodes[i]}",
			"collector_number": "{card.number}",
			"rarity": "{card.rarity.replace('basic', 'common')}",
			"subtypes": [],
			"oracle_text": "{card.rules_text}",
		}},
		'''	
			elif card.form == "split":
				card2 = None
				for c in setcards[i]:
					if c.card_name == card.backside:
						card2 = c
						break			
			elif card.form == "front":
				card2 = None
				for c in setcards[i]:
					if c.card_name == card.backside:
						card2 = c
						break
				cardtext = f'''
					"card_name": "{card.card_name}",
					"color": "{card.color}",
					"rarity": "{card.rarity}",
					"type": "{card.type}",
					"number": {card.number},
					"color_identity": "{card.color_identity}",
					"cost": "{card.cost}",
					"rules_text": "{card.rules_text}",
					"flavor_text": "[i]{card.flavor_text}[/i]",
					"pt": "{card.pt}",
					"special_text": "",
					"shape": "modal double faced",
					"set": "{setcodes[i]}",
					"loyalty": "{card.loyalty}",
					"artist": "{card.artist}",
					"play_rate": {play_rate},
					"card_name2": "{card2.card_name}",
					"color2": "{card2.color}",
					"type2": "{card2.type}",
					"cost2": "{card2.cost}",
					"rules_text2": "{card2.rules_text}",
					"flavor_text2": "[i]{card2.flavor_text}[/i]",
					"pt2": "{card2.pt}",
					"special_text2": "",
					"loyalty2": "{card2.loyalty}",
					"artist2": "{card2.artist}",
					"notes": "{tags}"
		'''    
				drafttext = f'''
		{{
			"name": "{card.card_name}",
			"mana_cost": "{card.cost.replace('Vp', 'S')}",
			"type": "{card.type.split(' ')[0]}",
			"image": "{card.cardfilename.replace('sets/', 'https://EscapeFromLimbo.github.io/sets/')}",
			"colors": [{','.join(['"' + k + '"' for k in card.color])}],
			"set": "{setcodes[i]}",
			"collector_number": "{card.number}",
			"rarity": "{card.rarity}",
			"subtypes": [],
			"oracle_text": "{card.rules_text}",
			"back": {{
				"name": "{card2.card_name}",
				"mana_cost": "{card2.cost.replace('Vp', 'S')}",
				"type": "{card2.type.split(' ')[0]}",
				"image": "{card2.cardfilename.replace('sets/', 'https://EscapeFromLimbo.github.io/sets/')}",
				"colors": [{','.join(['"' + k + '"' for k in card2.color])}],
				"set": "{setcodes[i]}",
				"collector_number": "{card2.number}",
				"rarity": "{card2.rarity}",
				"subtypes": [],
				"oracle_text": "{card2.rules_text}",
			}}
		}},
		'''	        
			if card.form in ["normal", "front", "token"]:
				if firstcard:
					firstcard = False
					setfile = setfile + "{" + cardtext + "}"
				else:
					setfile = setfile + ",{" + cardtext + "}"

				#print(cardtext)
				#draftfile...
				if not "PRO" in card.card_name:
					if card.form == "token":
						tokenNames.append(card.card_name)
					elif "Basic" in card.type:
						basicNames.append(card.card_name)
					elif "Land" in card.type and card.rarity in ["common", "basic"] and len(card.color_identity) == 2:
						landNames.append(card.card_name)
					elif card.rarity == "common":
						commonNames.append(card.card_name)
					elif card.rarity == "uncommon":
						uncommonNames.append(card.card_name)
					elif card.rarity == "rare":
						rareNames.append(card.card_name)
					elif card.rarity == "mythic":
						mythicNames.append(card.card_name)
					draftfile = draftfile + drafttext
		# play booster numbers
		# 13 cards + land slot
		# 7 common 20x each common
		# 3 uncommon 10x each uncommon
		# 1 rare 4x each rare, 2x each mythic
		# 2 wildcard (each 4/8 common, 3/8 uncommon, 1/8 rare/mythic. To get there, 1x each mythic, 2x each rare, 4x each uncommon, 6x each common)
		# 1`land 10x each common dual, 20x each common basic
		draftfile = draftfile + "]\n[Common]\n"
		for name in commonNames:
			draftfile = draftfile + "20 " + name + "\n"
		draftfile = draftfile + "\n[Uncommon]\n"
		for name in uncommonNames:
			draftfile = draftfile + "10 " + name + "\n"
		draftfile = draftfile + "\n[Rare]\n"
		for name in rareNames:
			draftfile = draftfile + "4 " + name + "\n"
		for name in mythicNames:
			draftfile = draftfile + "2 " + name + "\n"
		draftfile = draftfile + "\n[Land]\n"
		for name in landNames:
			draftfile = draftfile + "10 " + name + "\n"
		for name in basicNames:
			draftfile = draftfile + "20 " + name + "\n"
		draftfile = draftfile + "\n[Token]\n"
		for name in tokenNames:
			draftfile = draftfile + "20 " + name + "\n"
		draftfile = draftfile + "\n[Wildcard]\n"
		for name in commonNames:
			draftfile = draftfile + "6 " + name + "\n"
		for name in uncommonNames:
			draftfile = draftfile + "4 " + name + "\n"
		for name in rareNames:
			draftfile = draftfile + "2 " + name + "\n"
		for name in mythicNames:
			draftfile = draftfile + "1 " + name + "\n"

		setfile = setfile + postlude + "}"
		#print(setfile)
		with open(f"sets/{setcodes[i]}-files/{setcodes[i]}.json", "w", encoding="utf-8") as f:
			f.write(setfile)
		if not setcodes[i] in ["PLANE", "REV"]:
			with open(f"sets/{setcodes[i]}-files/{setcodes[i]}-draft.txt", "w", encoding="utf-8") as f:
				f.write(draftfile)
	print(f"{len(cubecards)} cube cards unaccounted for")
	if len(cubecards) > 0:
		print(cubecards)

	#TODO: white border around set logos