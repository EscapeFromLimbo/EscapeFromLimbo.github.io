import requests


def get_play_rates():

	tourneys = []
	#	"https://lackeybot.com/rev/statdex/t/gprev_21_05",
	#	"https://lackeybot.com/rev/statdex/t/gprev_25_06"]
	#print(str(r.content))

	#TODO total copies main / side
	setCodeOrder = ["SOL", "TWI", "KDT", "ERR", "CCR", "CNY", "CYB", "OLD", "TRX", "POP", "DOV", "BLR", "KSV", "KRS", "VRD", "SVG", "GQC", "KUT", "MON", "SRC", "VST"]


	for i in range(20, 27):
		for j in range(1, 13):
			exists = False
			if i == 21 and j in [5, 7, 8, 9, 10, 11]:
				exists = True
			if i > 21 and i < 26:
				exists = True
			if i == 26 and j <= 1:
				exists = True
			if i == 22 and j == 4:
				exists = False

			if j > 9 and exists:
				tourneys.append(f"https://lackeybot.com/rev/statdex/t/gprev_{i}_{j}")
			if j <= 9  and exists:
				tourneys.append(f"https://lackeybot.com/rev/statdex/t/gprev_{i}_0{j}")

	setTotalDecks = {}
	cardWins = {}
	cardGames = {}
	cardSets = {}
	cardDecks = {}
	cardTopCuts = {}
	cardMainCount = {}
	cardSideCount = {}
	cardSignatures = {}
	grandTotalDecks = 0

	for tourneyURL in tourneys:
		r = requests.get(tourneyURL)

		playersInGP = []
		playersInTopCut = []
		cardsInGP = []
		setsSeen = []
		totalDecks = 0

		tourneyName = str(r.content).split("\"longName\":\"")[1].split("\"")[0]
		print(tourneyName)
		if tourneyURL.endswith("_04") or tourneyURL.endswith("_08") or tourneyURL.endswith("_12"):
			print("Nonstandard GP, skipping")
			continue

		deckData = str(r.content).split("\"players\"")[1].split("\"playerIDs\"")[0].split("username\":\"")[1:]
		deckTable = {}
		for deck in deckData:
			#print(deck)
			playerName = deck.split("\"")[0].lower().replace("_", "")
			cards = deck.split("\"mainCount\":")[1:]
			deckTable[playerName] = []
			
			deckHasCards = False
			for card in cards:
				#print(card)
				cardName = card.split("\"displayName\":\"")[1].split("\"")[0]
				setCode = card.split("\"setID\":\"")[1].split("\"")[0]
				if "Ardent Ascetic" in cardName:
					setCode = "KSV"
				copiesMain = int(card.split(",")[0])
				copiesSide = int(card.split("\"sideCount\":")[1].split(",")[0])
				if copiesMain > 0 or copiesSide > 0:
					deckHasCards  = True
				deckTable[playerName].append(cardName)
				if cardName not in cardSets:
					cardSets[cardName] = []	
				if setCode not in cardSets[cardName] and setCode != "REV" and setCode != "PLANE":
					cardSets[cardName].append(setCode)
				if cardName not in cardMainCount:
					cardMainCount[cardName] = 0
				if cardName.replace("\\", "") not in cardSignatures:
					cardSignatures[cardName.replace("\\", "")] = playerName.replace("\\", "")
				if cardSignatures[cardName.replace("\\", "")] != playerName.replace("\\", ""):
					cardSignatures[cardName.replace("\\", "")] = ""
				cardMainCount[cardName] += copiesMain
				if cardName not in cardSideCount:
					cardSideCount[cardName] = 0
				cardSideCount[cardName] += copiesSide
				if setCode not in setTotalDecks:
					setTotalDecks[setCode] = 0
				cardsInGP.append(cardName)
			if deckHasCards:
				totalDecks += 1


		deckTable["Bye"] = []

		for cardName in cardsInGP:
			if len(cardSets[cardName]) == 1 and cardSets[cardName][0] not in setsSeen:
				setsSeen.append(cardSets[cardName][0])
		firstSet = ""
		firstSetIndex = 0
		numSets = 7
		for i in range(len(setCodeOrder)):
			if setCodeOrder[i] == "CCR":
				numSets = 6
			if setCodeOrder[i] in setsSeen:
				firstSet = setCodeOrder[i]
				firstSetIndex = i
				break

		for i in range(numSets):
			if firstSetIndex + i < len(setCodeOrder):
				setTotalDecks[setCodeOrder[firstSetIndex + i]] += totalDecks
		grandTotalDecks += totalDecks

		playerData = str(r.content).split("\"leaderboard\"")[1].split("playerSwissLine")[0].split("],[")
		#print(playerData)
		playerTable = {}
		for player in playerData:
			playerName = player.split(",")[1].replace("\"", "")
			playerID = player.split(",")[9].split("]")[0].replace("\"", "")
			playerTable[playerID] = playerName.lower().replace("_", "")
			#print(f"player {playerName} has ID {playerID}")
		playerTable[str(r.content).split("const bye = \"")[1].split("\"")[0]] = "Bye"

		#if "Shigane" in tourneyName:
		#	print(deckTable)
		matchData = str(r.content).split("\"matches\"")[1].split("\"players\"")[0]
		#print(matchData)
		matchData = matchData.split("\"p\"")

		#print(matchData)

		for match in matchData:
			if not "\"s\"" in match:
				continue
			#print(match)
			id1 = match.split(":[\"")[1].split("\"")[0]
			id2 = match.split("\",\"")[1].split("\"")[0]
			winner = match.split("\"w\":")[1].split(",")[0]
			gpround = match.split("\"n\":")[1].split(",")[0].split("}")[0]
			#print(f"{playerTable[id1]} vs {playerTable[id2]} in round {gpround}. {winner} wins")
			if not playerTable[id1] in playersInGP:
				playersInGP.append(playerTable[id1])
			if not playerTable[id2] in playersInGP:
				playersInGP.append(playerTable[id2])
			if playerTable[id1] in deckTable:
				for card in deckTable[playerTable[id1]]:
					if card not in cardGames:
						cardGames[card] = 0
						cardWins[card] = 0
						cardTopCuts[card] = 0
						cardDecks[card] = 0
					cardGames[card] += 1
					if winner == "1":
						cardWins[card] += 1
			if playerTable[id2] in deckTable:
				for card in deckTable[playerTable[id2]]:
					if card not in cardGames:
						cardGames[card] = 0
						cardWins[card] = 0
						cardTopCuts[card] = 0
						cardDecks[card] = 0
					cardGames[card] += 1
					if winner == "2":
						cardWins[card] += 1	
		for player in playersInGP:
			for card in deckTable[player]:
				cardDecks[card] += 1
		for player in playersInTopCut:
			for card in deckTable[player]:
				cardTopCuts[card] += 1

	#print(playerWins)
	#print(playerLosses)

	#print("Card Name, Set, Wins, Losses, Games, Winrate, Top Cuts, Decks, Top Cut Rate, Total Copies Main, Total Copies Side")
	#for card in cardGames:
	#	print(f"{card.replace(',', '')}, {cardSets[card]}, {cardWins[card]}, {cardGames[card] - cardWins[card]}, {cardGames[card]}, {cardWins[card] / cardGames[card]}, {cardTopCuts[card]}, {cardDecks[card]}, {cardTopCuts[card] / cardDecks[card]}, {cardMainCount[card]}, {cardSideCount[card]}")

	print("Total decks for each set")
	print(setTotalDecks)
	cardPlayRates = {}
	for cardName in cardGames:
		#if "A Journey" in cardName:
		#	print("Journey Begins count")
		#	print(cardMainCount[cardName] + cardSideCount[cardName])
		totalPossibleDecks = 0
		desanName = cardName.replace("\\", "")
		for setCode in cardSets[cardName]:
			totalPossibleDecks += setTotalDecks[setCode]
			#if "A Journey" in cardName:
			#	print(f"set {setCode} adds {setTotalDecks[setCode]}")
		if totalPossibleDecks == 0:
			cardPlayRates[desanName] = 0
		elif len(cardSets[cardName]) > 10:
			cardPlayRates[desanName] = int(1000 * (cardMainCount[cardName] + cardSideCount[cardName]) / grandTotalDecks)
		else:
			cardPlayRates[desanName] = int(1000 * (cardMainCount[cardName] + cardSideCount[cardName]) / totalPossibleDecks)
	return cardPlayRates, cardSignatures