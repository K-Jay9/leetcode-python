#! /usr/bin/env python


def solution(n,k):
    tally = []
    if n == 1:
        return []
    players = [i for i in range(1,n+1)]*n*100
    indexer = 1
    position = 0
    while True:
        if players[position] in tally:
            break
        tally.append(players[position])
        position += indexer*k
        indexer+= 1
    return [i for i in range(1,n+1) if i not in tally]

if __name__ == "__main__":
    print(solution(5,2))
    print(solution(4,4))
