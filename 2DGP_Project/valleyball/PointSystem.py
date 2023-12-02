from pico2d import get_time, load_font, load_wav

from share import game_framework, game_world

from tennis import select_mode
from valleyball.Player2 import idle


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
        ps.stop=True
        ps.ball.start = False  ##점수시스템에서 필요한변수
        ps.p1.cur_state = idle
        ps.p2.cur_state = idle
        ps.p2.down = True
        ps.p1.down = True


    @staticmethod
    def exit(ps, e):
        ps.ball.start = False

    @staticmethod
    def update(ps):

        if ps.ball.y < 60 :
          if ps.ball.x<600:
              ps.state_machine.handle_event('p2_win')
          else:
              ps.state_machine.handle_event('p1_win')

        if(ps.stop):
            if get_time() - ps.wait_time > 2:
                ps.ball.start=True



    @staticmethod
    def render(ps):

        if get_time()-ps.wait_time >=0 and get_time()-ps.wait_time<1:
            ps.winfont.draw(550, 100, f'{2}', (255, 255, 0))

        if get_time()-ps.wait_time >= 1 and get_time()-ps.wait_time<2:
            ps.winfont.draw(550, 100, f'{1}', (255, 255, 0))


        ps.font.draw(700, 200, f'{ps.p2.score}', (255, 255, 255))
        ps.font.draw(480, 200, f'{ps.p1.score}', (255, 255, 255))


class P1Win:
    @staticmethod
    def enter(ps, e):
        ps.bgm.play()
        ps.p1.x = 200
        ps.p1.y = 121

        ps.p2.x = 1000
        ps.p2.y = 121
        ps.p1.score+=1
        ps.p1.cur_state = idle
        ps.p2.cur_state = idle
        ps.p1.dir='right'
        ps.p2.dir='left'

        ps.p2.down = True
        ps.p1.down = True
        if ps.p1.score >= 4:
            ps.winner = 'p1'
            ps.state_machine.handle_event('game_end')

        ps.wait_time = get_time()  # pico2d import 필요

        # self.x=300
        ps.ball.x = 900
        ps.ball.y = 200
        ps.ball.frame = 0

        ps.ball.top = ps.ball.y + 20
        ps.ball.bottom = ps.ball.y - 20
        ps.ball.left = ps.ball.x - 20
        ps.ball.right = ps.ball.x + 20

        ps.ball.start = False  ##점수시스템에서 필요한변수

        ps.ball.going_vector = (-10, 10)
        ps.ball.going_vector = game_world.normalize_vector(ps.ball.going_vector[0], ps.ball.going_vector[1])
        ps.ball.speed_x = 700
        ps.ball.speed_y = 700
        ps.ball.gravity = 1  # 중력 값 (원하는 값으로 조정)
        ps.ball.dir = "up"

    @staticmethod
    def exit(ps, e):
        ps.p2.down = True
        ps.p1.down = True
        ps.ball.start = False

        pass

    @staticmethod
    def update(ps):
        if ps.ball.y < 60 :
          if ps.ball.x<600:
              ps.state_machine.handle_event('p2_win')
          else:
              ps.state_machine.handle_event('p1_win')

        if  ps.stop:
            if get_time() - ps.wait_time > 2:
                ps.ball.start = True




    @staticmethod
    def render(ps):

        if get_time()-ps.wait_time >=0 and get_time()-ps.wait_time<1:
            ps.winfont.draw(550, 100, f'{2}', (255, 255, 0))

        if get_time()-ps.wait_time >= 1 and get_time()-ps.wait_time<2:
            ps.winfont.draw(550, 100, f'{1}', (255, 255, 0))

        ps.font.draw(700, 200, f'{ps.p2.score}', (255, 255, 255))
        ps.font.draw(480, 200, f'{ps.p1.score}', (255, 255, 255))

class P2Win:
    @staticmethod
    def enter(ps, e):
        ps.p2.down = True
        ps.p1.down = True
        ps.p1.x = 200
        ps.p1.y = 121

        ps.p2.x = 1000
        ps.p2.y = 121
        ps.p2.score+=1
        ps.p1.cur_state = idle
        ps.p2.cur_state = idle
        ps.p1.dir='right'
        ps.p2.dir='left'
        ps.bgm.play()

        if ps.p2.score >= 4:
            ps.winner = 'p2'
            ps.state_machine.handle_event('game_end')



        ps.wait_time = get_time()  # pico2d import 필요

        ps.ball.fireshot = False
        # self.x=300
        ps.ball.x = 300
        ps.ball.y = 200
        ps.ball.frame = 0

        ps.ball.top =ps.ball.y + 20
        ps.ball.bottom = ps.ball.y - 20
        ps.ball.left = ps.ball.x - 20
        ps.ball.right =ps.ball.x + 20

        ps.ball.start = False  ##점수시스템에서 필요한변수

        ps.ball.going_vector = (10, 10)
        ps.ball.going_vector = game_world.normalize_vector(   ps.ball.going_vector[0],    ps.ball.going_vector[1])
        ps.ball.speed_x = 700
        ps.ball.speed_y = 700
        ps.ball.gravity = 1  # 중력 값 (원하는 값으로 조정)
        ps.ball.dir = "up"

    @staticmethod
    def exit(ps, e):
        ps.p1.cur_state = idle
        ps.p2.cur_state = idle
        ps.p2.down = True
        ps.p1.down = True
        ps.ball.start = False

    @staticmethod
    def update(ps):
        if ps.ball.y < 60 :
          if ps.ball.x<600:
              ps.state_machine.handle_event('p2_win')
          else:
              ps.state_machine.handle_event('p1_win')

        if ps.stop:
            if get_time() - ps.wait_time > 2:
                ps.ball.start = True


    @staticmethod
    def render(ps):

        if get_time()-ps.wait_time >=0 and get_time()-ps.wait_time<1:
            ps.winfont.draw(550, 100, f'{2}', (255, 255, 0))

        if get_time()-ps.wait_time >= 1 and get_time()-ps.wait_time<2:
            ps.winfont.draw(550, 100, f'{1}', (255, 255, 0))

        ps.font.draw(700, 200, f'{ps.p2.score}', (255, 255, 255))
        ps.font.draw(480, 200, f'{ps.p1.score}', (255, 255, 255))



class GameEnd:
    @staticmethod
    def enter(ps, e):
        ps.p1.cur_state = idle
        ps.p2.cur_state = idle
        ps.p2.down = True
        ps.p1.down = True
        ps.wait_time = get_time()  # pico2d import 필요
        ps.bgm.play()

    @staticmethod
    def exit(ps, e):
        pass

    @staticmethod
    def update(ps, title_mode=None):
        if get_time() - ps.wait_time > 3:
            game_framework.change_mode(select_mode)

    @staticmethod
    def render(ps):

        if ps.winner == 'p2':
            ps.winfont.draw(200, 400, f'{"RED WIN"}', (255, 0, 0))

        if ps.winner == 'p1':
            ps.winfont.draw(150, 400, f'{"BLUE WIN"}', (0, 0, 255))
        ps.font.draw(700, 200, f'{ps.p2.score}', (255, 255, 255))
        ps.font.draw(480, 200, f'{ps.p1.score}', (255, 255, 255))



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
    bgm=None
    def __init__(self,ball,p1,p2):
        self.ball=ball
        self.p1=p1
        self.p2=p2
        self.font = load_font('resource/ENCR10B.TTF', 50)
        self.winfont = load_font('resource/ENCR10B.TTF', 200)
        self.state_machine = ps_state_machine(self)
        self.state_machine.start()
        if not PointSystem.bgm:
            PointSystem.bgm = load_wav("resource/jackjack.wav")
            PointSystem.bgm.set_volume(30)


    def update(self):
        self.state_machine.update()

    def render(self):
        self.state_machine.render()


