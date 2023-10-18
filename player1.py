from pico2d import *

#상태머신 개발 => 캐릭터의 상태 win ,lose ,idle ,jump,jump_again ??


class idle:
    @staticmethod
    def enter(player, e):
        player.frame = 0
        print('Idle Enter')

    @staticmethod
    def exit(player, e):
        print('Idle Exit')

    @staticmethod
    def update(player):
        player.frame=(player.frame+1)%5
        print('Idle Do')

    @staticmethod
    def render(player):
        player.image.clip_draw(player.frame*115,0,115,175,player.x,player.y)
        pass


class p1_state_machine:
    def __init__(self, p1):
        self.p1 =p1
        self.cur_state=idle
        self.table={
            idle:{}
        }
    def start(self):
        self.cur_state.enter(self.p1,('start',0))
    def update(self):
        self.cur_state.update(self.p1)
    def render(self):
        self.cur_state.render(self.p1)

    def handle_event(self, e):
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.p1, e)
                self.cur_state = next_state
                self.cur_state.enter(self.p1, e)

                return True
        return False

class player1:
    def __init__(self):
        self.x=1000
        self.y=180
        self.frame = 0
        self.image = load_image('123.png')
        self.state_machine=p1_state_machine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self,e):
        self.state_machine.handle_event(('INPUT', e))

    def render(self):
        self.state_machine.render()




