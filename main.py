from enum import Enum, auto

class State(Enum):
    NO_TOKEN = auto()
    ONE_TOKEN = auto()
    BALL_DROPPED = auto()
    NOT_AVAILABLE = auto()



class GiftBall:
    
    def __init__(self, balls_left):
        self.current_state = State.NO_TOKEN
        self._balls_left = balls_left

    def insert_token(self):
        if self.current_state == State.NO_TOKEN:
            self.current_state = State.ONE_TOKEN    

    def eject_token(self):
        if self.current_state == State.ONE_TOKEN:
            self.current_state = State.NO_TOKEN
    
    def use_crank(self):
        if self.current_state == State.ONE_TOKEN:
            self.current_state = State.BALL_DROPPED

    def take_ball(self):
        if self.current_state == State.BALL_DROPPED:
            self._balls_left = self._balls_left - 1
            if self._balls_left > 0:
                self.current_state = State.NO_TOKEN
            else:
                self.current_state = State.NOT_AVAILABLE

    def check_ball_left(self):
        if self.current_state == State.BALL_DROPPED:
            self._balls_left = self._balls_left - 1

            return self.balls_left


if __name__ == "__main__":
    
    GiftBallMachine = GiftBall(2)
    print(GiftBallMachine.current_state)
    GiftBallMachine.insert_token()
    print(GiftBallMachine.current_state)
    GiftBallMachine.insert_token()
    GiftBallMachine.eject_token()
    print(GiftBallMachine.current_state)

    GiftBallMachine.insert_token()
    print(GiftBallMachine.current_state)
    GiftBallMachine.use_crank()
    print(GiftBallMachine.current_state)
    GiftBallMachine.take_ball()
    print(GiftBallMachine.current_state)

    GiftBallMachine.insert_token()
    print(GiftBallMachine.current_state)
    GiftBallMachine.use_crank()
    print(GiftBallMachine.current_state)
    GiftBallMachine.take_ball()
    print(GiftBallMachine.current_state)

    GiftBallMachine.insert_token()
    print(GiftBallMachine.current_state)

