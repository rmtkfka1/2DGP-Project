from pico2d import *

from tennis.behavior_tree import BehaviorTree, Action, Sequence, Condition


def keydown_f(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key ==SDLK_w

def time_out(e):
    return e[0] == 'TIME_OUT'

from pico2d import get_time

from share import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class idle:
    @staticmethod
    def enter(player, e):
        player.gravity = 0.05


    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        if player.frame > 0:
            player.frame -= (ACTION_PER_TIME * FRAMES_PER_ACTION * game_framework.frame_time)

        if (player.y > 120):
            player.y -= RUN_SPEED_PPS * game_framework.frame_time + player.gravity

            player.gravity += 1.0 * game_framework.frame_time

        if (player.y < 120):
            player.y = 120

        player.top = player.y + 60
        player.bottom = player.y - 90

        player.bt.run()
        pass

    @staticmethod
    def render(player):
        player.image.clip_draw(int(player.frame)*115,0,115,175,player.x,player.y)
        pass

class jump:
    @staticmethod
    def enter(player, e):
        player.wait_time =get_time()

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        if (player.frame < 5):
            player.frame += (ACTION_PER_TIME * 2 * FRAMES_PER_ACTION * game_framework.frame_time)

        if (player.y < 600):
            player.y += 500 * game_framework.frame_time

        if (get_time() - player.wait_time > 0.3):
            player.state_machine.handle_event(('TIME_OUT', 0))

        player.top = player.y + 90
        player.bottom = player.y - 60

        player.bt.run()
        pass


    @staticmethod
    def render(player):
        player.image.clip_draw(int(player.frame)*115,0,115,175,player.x,player.y)
        pass



class state_machine:
    def __init__(self, p2):
        self.p2=p2
        self.cur_state=self.p2.state
        self.table={
            idle: {time_out :jump},
            jump: {time_out: idle}
        }

    def start(self):
        self.cur_state.enter(self.p2,('start',0))
    def update(self):
        self.cur_state.update(self.p2)
    def render(self):
        self.cur_state.render(self.p2)


    def handle_event(self, e):
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.p2, e)
                self.cur_state = next_state
                self.cur_state.enter(self.p2, e)
                return True
        return False




class ai:
    def __init__(self,ball):
        self.x=200
        self.y=120
        self.frame = 0
        self.bottom = 120-90
        self.top = 120+60
        self.left = 200 + 59.9
        self.right = 200 + 60
        self.score = 0
        self.bt = None  # bt 속성 초기화
        self.state=idle
        self.image = load_image('resource/p2_img.png')
        self.ball =ball

        self.state_machine = state_machine(self)
        self.build_behavior_tree()  # bt 설정을 위한 메서드 호출
        self.state_machine.start()
        self.wait_time = 0  # Initialize wait_time attribute
        self.count=0


    def update(self):
        self.state_machine.update()


    def handle_event(self,event):
        self.state_machine.handle_event(('INPUT', event))

    def render(self):
        self.state_machine.render()


    def get_bb(self):
        cur_state = self.state_machine.cur_state
        if cur_state == idle:
            return self.x+55,self.y-90,self.x+60,self.y+60
        if cur_state == jump:
            return self.x+55, self.y-60, self.x+60, self.y +90

    def handle_collusion(self, group, other):
        pass

    def check(self):
        if self.ball.start==False:
            return BehaviorTree.FAIL
        if self.ball.y - self.y > 20:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL


    def change_state(self,new_state):
        self.state_machine.cur_state = new_state
        return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        c1 = Condition("조건 검사", self.check)  ## action 노드생성
        a1 = Action("점프상태",self.change_state,jump)
        SEQ_wander = Sequence("점프상태로만듬", c1, a1)
        self.bt =BehaviorTree(SEQ_wander)





