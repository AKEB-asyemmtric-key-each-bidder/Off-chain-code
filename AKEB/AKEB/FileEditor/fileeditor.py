import json
import os


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

    def submitBid(self, bid):
        self.bids.append(bid)
        self.writeIntoFile()
