#import numpy as np
import logging
from random import randint
import scipy.stats as stats
from sortedcontainers import SortedList
#from sklearn.cluster import DBSCAN
#from sklearn import metrics
#from sklearn.preprocessing import StandardScaler
from collections import namedtuple
# http://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#example-cluster-plot-dbscan-py
#
# OMG, don't judge me by this code! /me hides his face

def get_play(me,hands,h_str) :
    self = get_play
    logging.debug("/\\/\\/\\/\\/\\/\\/\\/\\/\\TONY/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\")
    if not hasattr(self, "game"):
        self.game = None
        #find players
        
    if not self.game or len(self.game.h_str) > len(h_str):
        self.game = game(self.game)
        self.game.prev_turn = 0
        
    return self.game.get_play(me,hands,h_str)

        
class player():

    def __init__ (self):
        #naive risks where lie was called
        self.all_lies = SortedList()
        self.lies_to_me = SortedList()    
        
    def _median(self,values):
        if len(values) > 12:
            med1 = values[len(values)/2]
            med2 = values[(len(values)+1)/2]
            median = (med1 + med2) /2
        else:
            #return an average instead or default value of .25 if zero length
            median = sum(values) / len(values) if values else .25
        return(median)
    
    def all_median(self):
        return(self._get_median(self.all_lies))
        
    def to_me_median(self):
        return(self._get_median(self.to_me_lies))


class game():
    """the game"""
    
    def __init__(self,old_game):
        #instance attributes
        self.players = {}
        self.opposing_bid = None
        self.prev_turn = 0
        self.total_dice = 0
        self.my_hand = None
        self.h_str = ""
        if old_game: 
            self.bid = old_game.bid
            self.player_bid = old_game.player_bid
            self.liar = old_game.liar
        else:
            self.bid = namedtuple('bid',['quant','face'])
            self.player_bid = namedtuple('player_bid',['player','bid'])
            self.liar = self.bid(0,0)

    def get_play(self,me,hands,h_str):
            #parse history for this game h_srt => history_list[] - find round number
        history_list = []
        round_num = 1 #first round
        if len(h_str) > 0: #if not the openning bid
            for player_quant_face in h_str.split(','):
                player, quant_face = player_quant_face.split(':')
                quant, face =  int(quant_face) // 10, int(quant_face) % 10
                history_list.append(self.player_bid(player, self.bid(quant,face)))
                if player == me:
                    round_num += 1 
        total_dice = 0
        for hand in hands.split(','): 
            player, dice = hand.split(':')
            total_dice += len(dice)
            if player == me :
                self.my_hand = dice
        self.total_dice = total_dice
        self.add_round(history_list[self.prev_turn:-1])
        if history_list:
            opposing_bid = history_list[-1].bid
            if opposing_bid.quant == 0:
                logging.debug("showdown!")
                return 0 #showdown
        else: #openning bid
            logging.debug("openning bid!") #bid 1 of a random face in hand
            return(10 + int(self.my_hand[randint(0,len(self.my_hand)-1)]))
        self.opposing_bid = opposing_bid
        logging.debug("Opposing bid: %i %i" % (opposing_bid.quant,opposing_bid.face))
               
        sticky_bid = self.bid(opposing_bid.quant + 1, opposing_bid.face)
        risks = {}
        logging.debug("getting risk for liar")
        risks[self.liar] = 1 - self.hand_risk(opposing_bid)
        logging.debug("getting risk for sticky bid %i %i" % (sticky_bid.quant,sticky_bid.face))
        risks[sticky_bid] = self.hand_risk(sticky_bid)
        logging.debug("INCREASING FACES")
        for face in range(1,opposing_bid.face+1):
            logging.debug("Face %i ******" % face)
            proposed_bid = self.bid(opposing_bid.quant + 1, face)
            risks[proposed_bid] = self.hand_risk(proposed_bid)   
        logging.debug("INCREASING QUANTITIES")
        if opposing_bid.face < 6:
            for face in range(opposing_bid.face + 1, 7):
                logging.debug("Face %i ******" % face)
                proposed_bid = self.bid(opposing_bid.quant, face)
                risks[proposed_bid] = self.hand_risk(proposed_bid) 
        logging.debug(risks)
    
        best_bid = min(risks, key=risks.get)
        
        logging.debug("best bid: %i %i" % (best_bid.quant,best_bid.face))
       
        # if sticking with the face is similar in risk to the best bid, just stay 
        # with the same face, but only if the naive risk < .5 for the sticky bid
        if self.naive_risk(sticky_bid) < .5:
            logging.debug("considering sticky bid best_bid: %.3f sticky_bid: %.3f"
                % (risks[best_bid], risks[sticky_bid]))
            if risks[best_bid] > 0 and risks[best_bid] < (risks[sticky_bid] + .4):
                logging.debug ("Chose sticky bid! %i %i" % sticky_bid)
                best_bid = sticky_bid
    
        # if we're aobut to call liar, but the risk of doing so is likely to
        # lose, we should bluff instead of calling liar            
        if best_bid is self.liar and ((risks[self.liar] < .5) and risks[self.liar] > .35
                or opposing_bid.quant == 1):
            logging.debug("Reconsidering Liar!")
            del risks[self.liar]
            proposed_bid = min(risks, key=risks.get)
            logging.debug("Considering %i %i instead of Liar" % proposed_bid)
            if risks[proposed_bid] < .5:
                best_bid = proposed_bid
                logging.debug("chose a new low risk bid %i %i" % best_bid)
        
        return(best_bid.quant * 10 + best_bid.face)
            
    def at_least_risk(self,dice,quant):
        logging.debug("Getting at least risk for %i in a pool of %i dice" % (quant,dice))
        if quant < 1:
            logging.debug("Surity = 0% risk")
            return 0.0
        if quant > dice:
            logging.debug("Impossible bid = 100% risk")
            return 1.0
        p = 1.0/6.0
        risk = stats.binom.cdf(quant -1, dice, p)
        logging.debug("Quant: %i Dice: %i Risk: %.3f p: %.3f" % (quant,dice,risk,p) )
        return risk

    def add_round(self, round_history_list):
        pass
    
    def naive_risk(self, bid):
        return(self.at_least_risk(self.total_dice,bid.quant))

    def hand_risk(self, bid):
        good_guess = 1 if self.opposing_bid.face == bid.face else 0
        logging.debug("Good guess is %i for face %i" % (good_guess,self.opposing_bid.face))
        hand_dice = self.total_dice - len(self.my_hand) - good_guess
        hand_quant = bid.quant - self.my_hand.count(str(bid.face)) - good_guess
        logging.debug ("hand_quant: %i in hand_dice: %i" % (hand_quant,hand_dice))
        return(self.at_least_risk(hand_dice,hand_quant))
        
    def next_risk(self, bid):
        return self.hand_risk(bid)
    
    def pool_risk(self, bid):
        return self.hand_risk(bid)
    
    def quant_risk(self, quant):
        return(self.at_least_risk(self.total_dice,quant))  