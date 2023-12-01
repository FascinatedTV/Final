import random

def rollDice():
    return random.randint(1, 6)

def firstRoll(numDice):
    return [rollDice() for _ in range(numDice)]

def newRoll(diceList, choice):
    return [dice if dice == choice else rollDice() for dice in diceList]

def createDiceDict(diceList):
    return {i: diceList.count(i) for i in range(1, 7)}

def mostFrequent(diceDict):
    return max(diceDict, key=lambda k: (diceDict[k], k))

def probabilityYahtzee(numTrials, numDice):
    yahtzee_count = 0
    for _ in range(numTrials):
        dice = firstRoll(numDice)
        diceDict = createDiceDict(dice)
        choice = mostFrequent(diceDict)
        dice = newRoll(dice, choice)
        diceDict = createDiceDict(dice)
        if all(value == choice for value in dice):
            yahtzee_count += 1
    return yahtzee_count / numTrials

def rollsToGetTenzi(numTrials, numDice):
    rolls_count = {i: 0 for i in range(1, 12)}
    for _ in range(numTrials):
        dice = firstRoll(numDice)
        for rolls in range(1, 12):
            diceDict = createDiceDict(dice)
            if len(set(dice)) == 1:
                rolls_count[min(rolls, 11)] += 1
                break
            if(rolls == 11):
                rolls_count[11] += 1
                break
            choice = mostFrequent(diceDict)
            dice = newRoll(dice, choice)
    return rolls_count

def main():
    while True:
        choice = input("Enter 'Y' to play Yahtzee, 'T' to play Tenzi, or anything else to quit: ")
        if choice.lower() == 'y':
            numTrials = int(input("Enter the number of trials for Yahtzee: "))
            numDice = int(input("Enter the number of dice: "))
            probability = probabilityYahtzee(numTrials, numDice)
            print(f"Probability of Yahtzee with {numDice} dice: {probability:.4f}")
        elif choice.lower() == 't':
            numTrials = int(input("Enter the number of trials for Tenzi: "))
            numDice = int(input("Enter the number of dice: "))
            tenzi = rollsToGetTenzi(numTrials, numDice)
            tenzi["more than 10"] = tenzi.pop(11)
            print(f"Rolls to get Tenzi with {numDice} dice:")
            print(tenzi)
        else:
            break

if __name__ == "__main__":
    main()