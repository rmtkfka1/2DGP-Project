from pico2d import *

#상태머신 개발 => 캐릭터의 상태 win ,lose ,idle ,jump,jump_again ??

def spacedown(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key ==SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'
class idle:
    @staticmethod
    def enter(player, e):
        print('Idle Enter')

    @staticmethod
    def exit(player, e):
        print('Idle Exit')

    @staticmethod
    def update(player):
        player.frame_divide += 2.0
        if(player.frame_divide >=1):
             if (player.frame == 0):
                 player.frame =0
             else:
                 player.frame-=1
             player.frame_divide=0

        if(player.y>180):
            player.y -= 20
        print(player.y)

    @staticmethod
    def render(player):
        player.image.clip_draw(player.frame*115,0,115,175,player.x,player.y)
        pass

class jump:
    @staticmethod
    def enter(player, e):
        player.wait_time =get_time()
        pass
    @staticmethod
    def exit(player, e):
        print('jump Exit')

    @staticmethod
    def update(player):
        player.frame_divide += 2.0
        print(player.frame_divide)
        if (player.frame_divide >= 1):
            if (player.frame == 5):
                player.frame = 5
            else:
                player.frame += 1
            player.frame_divide = 0

        if(player.y <600):
            player.y += 20.0

        if(get_time()- player.wait_time>0.3):
            player.state_machine.handle_event(('TIME_OUT',0))

        print('jump Do')

    @staticmethod
    def render(player):
        player.image.clip_draw(player.frame*115,0,115,175,player.x,player.y)
        pass

class p1_state_machine:
    def __init__(self, p1):
        self.p1 =p1
        self.cur_state=idle
        self.table={
            idle: {spacedown : jump },
            jump: {spacedown : jump ,time_out:idle}
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
        self.frame_divide=0.0
        self.image = load_image('p1_img.png')
        self.state_machine=p1_state_machine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self,event):
        self.state_machine.handle_event(('INPUT', event))

    def render(self):
        self.state_machine.render()




