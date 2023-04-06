def solution(players, callings):
    play = {}
    for i in range(len(players)):
        play[players[i]] = i
    for call in callings:
        idx = play[call]
        tmp = players[idx - 1]
        players[idx - 1] = call
        players[idx] = tmp
        play[call] -= 1
        play[tmp] += 1
    return players