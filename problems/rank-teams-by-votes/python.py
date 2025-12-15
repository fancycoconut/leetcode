class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]

        numOfRanks = len(votes[0])
        teamRanksMap = {}

        # Loop each rank which is same as the length of a vote
        for rank in range(numOfRanks):
            # Tally up the votes at each rank
            for vote in votes:
                team = vote[rank]
                scoresAtRank = teamRanksMap.get(team, [0] * numOfRanks)
                scoresAtRank[rank] += 1
                teamRanksMap[team] = scoresAtRank
        #print(teamRanksMap)

        # sort the letters in descending order, based on the rankings then the letter
        teamsSortedByVotes = sorted(teamRanksMap.keys(), key=lambda team: (teamRanksMap[team], -ord(team)), reverse=True)
        #print(teamsSortedByVotes)

        return "".join(teamsSortedByVotes)
