# huamn.py -- human liar's dice player

import logging

def get_play(me,hands_str,history) : 
    ''' play against the computer '''
    logging.info('You are player "%s".' % me)
    logging.info('History: %s' % history)
    logging.info('Hands: %s' % hands_str)
    if 0 != len(history) :
        last_play = history.split(',')[-1]
        if 0 == int(last_play.split(':')[1]) :
            logging.info('Hand over. Press return to continue ...')
            raw_input()
            logging.info('*' * 50)
            return 0
    logging.info('Enter move (e.g., "0" to call, "23" for two threes, "106" for ten sixes) :')
    s = raw_input()
    x = 0
    try :
        x = int(s)
    except :
        pass
    logging.info('*' * 50)
    return x
