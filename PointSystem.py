from pico2d import get_time

import play_mode

def time_out(e):
    return e == 'TIME_OUT'

def def_p1_win(e):
    return e == 'p1_win'

def def_p2_win(e):
    return e == 'p2_win'

def def_game_end(e):
    return e == 'game_end'

class Start:
    @staticmethod
    def enter(ps, e):
        ps.wait_time = get_time()  # pico2d import 필요

    @staticmethod
    def exit(ps, e):
        ps.ball.start = False

    @staticmethod
    def update(ps):
        if get_time() - ps.wait_time > 2:
            ps.ball.start=True
        if ps.ball.x < 0:
            ps.state_machine.handle_event('p1_win')
        if ps.ball.x > 1200:
            ps.state_machine.handle_event('p2_win')

    @staticmethod
    def render(ps):
        pass


class P1Win:
    @staticmethod
    def enter(ps, e):

        if ps.p2.score >= 1:
            ps.state_machine.handle_event('game_end')

        ps.wait_time = get_time()  # pico2d import 필요

        ps.ball.x =900
        ps.ball.y =200
        ps.ball.fireshot=False
        ps.ball.speed=1.0
        ps.ball.going_vector=ps.ball.speed * -500,  ps.ball.speed * 300
        ps.p1.score +=1

    @staticmethod
    def exit(ps, e):
        ps.ball.start = False
        pass

    @staticmethod
    def update(ps):
        if get_time() - ps.wait_time > 2:
            ps.ball.start = True

        if ps.ball.x<0:
            ps.state_machine.handle_event('p1_win')
        if ps.ball.x>1200:
            ps.state_machine.handle_event('p2_win')


    @staticmethod
    def render(ps):
        pass

class P2Win:
    @staticmethod
    def enter(ps, e):
        if ps.p2.score >=3:
            ps.state_machine.handle_event('game_end')

        ps.wait_time = get_time()  # pico2d import 필요
        ps.ball.x = 300
        ps.ball.y = 200
        ps.ball.fireshot = False
        ps.ball.speed = 1.0
        ps.ball.going_vector = ps.ball.speed * 500, ps.ball.speed * 300
        ps.p2.score += 1

    @staticmethod
    def exit(ps, e):
        ps.ball.start = False

    @staticmethod
    def update(ps):
        if get_time() - ps.wait_time > 2:
            ps.ball.start = True

        if ps.ball.x < 0:
            ps.state_machine.handle_event('p1_win')
        if ps.ball.x > 1200:
            ps.state_machine.handle_event('p2_win')

    @staticmethod
    def render(ps):
        pass



class GameEnd:
    @staticmethod
    def enter(ps, e):
        pass

    @staticmethod
    def exit(ps, e):
        pass

    @staticmethod
    def update(ps):
        pass

    @staticmethod
    def render(ps):
        pass



class ps_state_machine:
    def __init__(self, ps):
        self.ps = ps
        self.cur_state = Start
        self.table = {Start:{def_p1_win:P1Win,def_p2_win:P2Win,time_out:Start},
                      P1Win:{def_p1_win:P1Win,def_p2_win:P2Win,def_game_end:GameEnd},
                      P2Win: {def_p1_win: P1Win, def_p2_win: P2Win,def_game_end:GameEnd}
                      }

    def start(self):
        self.cur_state.enter(self.ps, ('starting', 0))

    def update(self):
        self.cur_state.update(self.ps)

    def render(self):
        self.cur_state.render(self.ps)

    def handle_event(self, e):
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.ps, e)
                self.cur_state = next_state
                self.cur_state.enter(self.ps, e)
                return True
        return False


class PointSystem:
    def __init__(self,ball,p1,p2):
        self.ball=ball
        self.p1=p1
        self.p2=p2
        self.state_machine = ps_state_machine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def render(self):
        self.state_machine.render()


