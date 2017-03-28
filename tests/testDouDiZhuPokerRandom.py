#!/bin/python
import roomai
import roomai.doudizhu
import unittest

class DouDiZhuPokerRandomPlayerTester(unittest.TestCase):
    
    
    def testPlayersRepeat(self):
        for i in xrange(100):
            self.testPlayers()
    

    def testPlayers(self):

        players = [roomai.doudizhu.DouDiZhuPokerRandomPlayer() for i in xrange(3)]
        env     = roomai.doudizhu.DouDiZhuPokerEnv()

        isTerminal, _, infos = env.init()

        for i in xrange(len(players)):
            players[i].receiveInfo(infos[i])

        count = 0
        while isTerminal == False: 
            turn = infos[-1].public_state.turn
            actions =roomai.doudizhu.Utils.candidate_actions(players[turn].hand_cards, env.public_state)
            action = players[turn].takeAction()
            isTerminal, scores, infos = env.forward(action)
            for i in xrange(len(players)):
                players[i].receiveInfo(infos[i])

            count += 1
            if count > 10000:
                raise Exception("A round has more than 10000 epoches")

