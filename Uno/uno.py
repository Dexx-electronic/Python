import random

"""
Build deck
"""


def buildDeck():
    deck = []
    colours = ["R", "G", "Y", "B"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "D2", "Skip", "Rev"]
    for colour in colours:
        for value in values:
            cardVal = f"{colour} {value}"
            deck.append(cardVal)
            if (value != 0):
                deck.append(cardVal)  # becouse we need 2 of each card instead 0
    wilds = ["Wild", "Wild D4"]

    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    return deck


"""
Shuffle deck
"""


def suffleDeck(deck):
    for cardPos in range(len(deck)):
        randPos = random.randint(0, len(deck) - 1)
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    return deck


"""
Deals x cards to x player
"""
def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn

""" 
Shows player hand
parameter: player->initger, playerHand->List
return: none
"""
def showHand(player, playerHand):
    print(f"Player {player + 1}")
    print("Your Hand")
    print("-------------")
    y = 1
    for  card in playerHand:
        print(f"{y}: {card}")
        y += 1
    print("")

"""
Chcecks if player is able to play
Parameters: 

"""
def canPlay(colour, value,  playerHand):
    for card in playerHand:
        if "Wild" in card:
            return True
        elif colour in card or value in card:
            return True
    return False


if __name__ == '__main__':
    unoDeck = buildDeck()
    print(suffleDeck(unoDeck))
    discards = []
    players = []
    numPlayers = int(input("How many players? "))
    while numPlayers > 5 or numPlayers < 2:
        numPlayers = int(input("Invalid!. How many Players? "))
    for player in range(numPlayers):
        players.append(drawCards(5))

    print(players)

    playerTurn = 0
    playDirection = 1
    playing = bool
    discards.append(unoDeck.pop(0))




    while playing:
        showHand(playerTurn, players[playerTurn])
        print(f"Card on top of te discard pile: {discards[-1]}")
        splitCard = discards[-1].split(' ', 1)
        currentColour = splitCard[0]
        if currentColour != "Wild":
            cardVal = splitCard[1]
        else:
            cardVal = "Any"
        if(canPlay(currentColour, cardVal,players[playerTurn])):
            cardChosen = int(input("Which card do you want to play? "))
            while not canPlay(currentColour,cardVal,[players[playerTurn][cardChosen-1]]):
                    cardChosen = int(input("Wrong card! choose again "))
            print(f"Played card: {players[playerTurn][cardChosen-1]} \n")

            discards.append(players[playerTurn].pop(cardChosen -1))
        else:
            print("You can't play. Card drawed ")
            players[playerTurn].extend(drawCards(1))
            input("Press Enter to continue...")

        colours = ["R", "G", "Y", "B"]

        splitCard = discards[0].split(' ', 1)
        currentColour = splitCard[0]
        if currentColour == "Wild":
            print(f"1. Blue \n2. Yellow \n3. Red \n4. Green")
            newColour =  int(input("Pick colour"))
            while newColour > 4 or newColour < 1:
                newColour = int(input("Invalid. Pick colour"))

        playerTurn += playDirection
        if(numPlayers == playerTurn):
            playerTurn = 0
        elif playerTurn < 0:
            playerTurn = numPlayers-1







