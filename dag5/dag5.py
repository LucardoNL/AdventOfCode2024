with open('dag5rules.txt') as f:
    input = f.read()
    regels = [regel.split('|') for regel in input.splitlines()]

with open('dag5input.txt') as f:
    input = f.read()
    updates = input.splitlines()

resultaat = 0
nieuweUpdates = []

def validatorEnUpdater (updates, resultaat):
    for update in updates:
        update = update.split(',')
        updateValid = True
        for page in update:
                for regel in regels:
                    if updateValid:
                        if page == regel[0] and regel[1] in update and update.index(regel[1]) < update.index(page):
                            #print(str(update) + 'did not pass 1')
                            updateAangepast = update
                            updateAangepast.remove(page)
                            updateAangepast.insert(update.index(regel[1]), page)
                            nieuweUpdates.append(','.join(updateAangepast))
                            updateValid = False
                        elif page == regel[1] and regel[0] in update and update.index(regel[0]) > update.index(page):
                            #print(str(update) + 'did not pass 2')
                            updateAangepast = update

                            #print(updateAangepast, regel[1], regel[0], update.index(regel[0]))

                            updateAangepast.remove(regel[0])
                            updateAangepast.insert(update.index(regel[1]), regel[0])

                            #print(updateAangepast)

                            nieuweUpdates.append(','.join(updateAangepast))
                            updateValid = False
                        else:
                            continue
                    else:
                        break
        if updateValid:
            resultaat += int(update[len(update)/2]) 
    return resultaat

resultaat = validatorEnUpdater(updates, resultaat)
resultaat2 = 0       
resultaat2 = validatorEnUpdater(nieuweUpdates, resultaat2)


print(resultaat, resultaat2)

