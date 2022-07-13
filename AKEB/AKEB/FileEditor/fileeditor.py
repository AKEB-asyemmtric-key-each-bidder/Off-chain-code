import json


class FileEditor:
    numberOfBidders = 0
    numberOfSubmittedBids = 0
    numberOfAskedWinner = 0
    bids = []
    winner = -1000

    def __init__(self):
        self.readValuesFromFile()

    def readValuesFromFile(self):
        with open('AKEB/FileEditor/data.json', 'r') as f:
            data = json.load(f)

        self.numberOfBidders = data['numberOfBidders']
        self.numberOfSubmittedBids = data['numberOfSubmittedBids']
        self.numberOfAskedWinner = data['numberOfAskedWinner']
        self.bids = data['bids']
        self.winner = data['winner']

    def incrementNumberOfBidders(self):
        self.numberOfBidders += 1
        self.writeIntoFile()

    def writeIntoFile(self):
        dict = {
            'numberOfBidders': self.numberOfBidders,
            'numberOfSubmittedBids': self.numberOfSubmittedBids,
            'numberOfAskedWinner': self.numberOfAskedWinner,
            'bids': self.bids,
            'winner': self.winner
        }

        with open('AKEB/FileEditor/data.json', 'w') as f:
            json.dump(dict, f)
        f.close()

    def submitBid(self, bid):
        self.bids.append(bid)
        self.numberOfSubmittedBids += 1
        self.writeIntoFile()

        # All bidders have submitted bids
        if self.numberOfBidders == self.numberOfSubmittedBids:
            self.findWinner()

    def findWinner(self):
        # self.winner = max(self.bids)
        self.winner = min(self.bids)
        # self.winner = self.bids[1]
        self.writeIntoFile()

    def getWinner(self):
        winnerTemp = self.winner

        if winnerTemp == -1000:
            return winnerTemp

        self.numberOfAskedWinner += 1
        self.writeIntoFile()

        # All bidders have asked the bidder winner, hence the data can be deleted
        if self.numberOfAskedWinner == self.numberOfBidders:
            self.reset()

        return winnerTemp

    def reset(self):
        self.numberOfBidders = 0
        self.numberOfSubmittedBids = 0
        self.numberOfAskedWinner = 0
        self.bids = []
        self.winner = -1000

        self.writeIntoFile()
