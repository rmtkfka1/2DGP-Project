from pico2d import *

from share import game_framework
from tennis.behavior_tree import BehaviorTree, Action, Condition, Selector ,Sequence
from valleyball import balley_mode


def time_out(e):
    return e[0] == 'TIME_OUT'


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 12

TIME_PER_ACTION_SMASH =1.2
ACTION_PER_SMASH = 1.0 / TIME_PER_ACTION_SMASH
FRAMES_PER_SMASH = 13

TIME_PER_ACTION_SLIDE =0.7
ACTION_PER_SLIDE = 1.0 / TIME_PER_ACTION_SLIDE
FRAMES_PER_SLIDE = 15


TIME_PER_ACTION_RECEPTION = 1.0
ACTION_PER_RECEPTION = 1.0 / TIME_PER_ACTION_RECEPTION
FRAMES_PER_RECEPTION = 11

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



class idle:
    @staticmethod
    def enter(player, e):
        player.cur_state ='idle'
        player.frame = 0
        pass

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

        player.bt.run()
    @staticmethod
    def render(player):
        if player.dir =='left':
            player.idle_left_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        if player.dir == 'right':
            player.idle_right_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class jump:
    @staticmethod
    def enter(player, e):
        player.down=False
        player.cur_state ='jump'
        player.frame = 0
        pass


    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12


        if (player.y < 400 and player.down ==False):
            player.y += player.jump_speed * game_framework.frame_time

        if(player.y>400):
            player.y=400
            player.down=True

        if player.y >120 and player.down==True:
            player.y -= player.jump_speed * game_framework.frame_time

        if player.y<120:
            player.state_machine.handle_event(('TIME_OUT',0))

        player.bt.run()
    @staticmethod
    def render(player):
        if player.dir == 'left':
            player.idle_left_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        if player.dir == 'right':
            player.idle_right_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass

class run_right:
    @staticmethod
    def enter(player, e):
        player.dir = 'right'
        player.cur_state = 'run_right'
        player.frame = 0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
        if (player.x < 1200):
            player.x += player.run_speed * game_framework.frame_time
        player.bt.run()
    @staticmethod
    def render(player):
        player.run_right_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class run_left:
    @staticmethod
    def enter(player, e):
        player.dir='left'
        player.cur_state ='run_left'
        player.frame = 0
    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
        if (player.x >650):
            player.x -= player.run_speed * game_framework.frame_time

        player.bt.run()

    @staticmethod
    def render(player):
        player.run_left_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class run_left_to_middle:
    @staticmethod
    def enter(player, e):
        player.dir='left'
        player.cur_state ='run_left_to_middle'
        player.frame = 0
    @staticmethod
    def exit(player, e):
        player.cur_state = 'idle'

        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

        player.x -= player.run_speed * game_framework.frame_time

        if (player.x<900):
            player.x = 900
            player.state_machine.handle_event(('TIME_OUT', 0))

        player.bt.run()

    @staticmethod
    def render(player):
        player.run_left_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class run_right_to_middle:
    @staticmethod
    def enter(player, e):
        player.dir = 'right'
        player.cur_state = 'run_right_to_middle'
        player.frame = 0

    @staticmethod
    def exit(player, e):
        player.cur_state = 'idle'
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

        player.x += player.run_speed * game_framework.frame_time

        if (player.x>900):
            player.x=900
            player.state_machine.handle_event(('TIME_OUT', 0))

        player.bt.run()

    @staticmethod
    def render(player):
        player.run_right_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class smash:
    @staticmethod
    def enter(player, e):
        player.frame=0
        player.cur_state = 'smash'
        player.dist =0
    @staticmethod
    def exit(player, e):
        player.dir='left'
        player.frame = 0
        player.dist =0

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_SMASH * ACTION_PER_SMASH * game_framework.frame_time) % 13


        if (player.y < 400 and player.down == False):
            player.y += player.jump_speed * game_framework.frame_time

        if (player.y > 400):
            player.y = 400
            player.down = True

        if player.y > 120 and player.down == True:
            player.y -= player.jump_speed * game_framework.frame_time

        if player.y < 120:
            player.y=120
            player.state_machine.handle_event(('TIME_OUT', 0))

        player.bt.run()

    @staticmethod
    def render(player):
        player.smash_right_image.clip_draw(int(player.frame) * 64, 0, 64, 93, player.x, player.y)
        pass

class slide_right:
    @staticmethod
    def enter(player, e):
        player.down = False
        player.cur_state ='slide_right'
        player.frame=0
        player.dist =0
    @staticmethod
    def exit(player, e):
        player.frame = 0
        player.dist =0
        player.cur_state = 'idle'
        player.dir='right'
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_SLIDE * ACTION_PER_SLIDE * game_framework.frame_time) % 15


        if (player.x < 1200 and player.x >1170):
            player.state_machine.handle_event(('TIME_OUT', 0))

        if (player.x < 1200):
            player.x += player.slide_speed * game_framework.frame_time
            player.dist += 30* game_framework.frame_time

        if player.dist >20:
            player.state_machine.handle_event(('TIME_OUT', 0))


        player.bt.run()
    @staticmethod
    def render(player):
        player.slide_right_image.clip_draw(int(player.frame) * 64, 0, 64, 93, player.x, player.y)
        pass



class slide_left:
    @staticmethod
    def enter(player, e):
        player.down = False
        player.cur_state ='slide_left'
        player.frame=15
        player.dist =0
    @staticmethod
    def exit(player, e):
        player.cur_state = 'idle'
        player.dir='left'
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame - FRAMES_PER_SLIDE * ACTION_PER_SLIDE * game_framework.frame_time) % 15

        if (player.x < 640 and player.x > 610):
            player.state_machine.handle_event(('TIME_OUT', 0))

        if (player.x > 600):
            player.x -= player.slide_speed * game_framework.frame_time
            player.dist += 30* game_framework.frame_time

        if player.dist >20:
            player.state_machine.handle_event(('TIME_OUT', 0))

        player.bt.run()
    @staticmethod
    def render(player):
        player.slide_left_image.clip_draw(int(player.frame) * 64, 0, 64, 93, player.x, player.y)
        pass


class reception:
    @staticmethod
    def enter(player, e):
        player.wait_time = get_time()
        player.down = False
        player.dir ='right'
        player.cur_state ='reception'
        player.frame=0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame - FRAMES_PER_RECEPTION * ACTION_PER_RECEPTION * game_framework.frame_time) % 11

        if (get_time() - player.wait_time > 1.0):
            player.state_machine.handle_event(('TIME_OUT', 0))

        player.bt.run()

    @staticmethod
    def render(player):
        player.reception_right_image.clip_draw(int(player.frame) * 70, 0, 70, 93, player.x, player.y)
        pass




class state_machine:
    def __init__(self, p2):
        self.p2=p2
        self.cur_state=self.p2.cur_state
        self.table={
            idle: {time_out: idle},
            jump: {time_out: idle},
            run_right: {time_out: idle},
            run_left: {time_out: idle},
            smash: {time_out: idle},
            slide_right: {time_out: idle},
            slide_left: {time_out: idle},
            reception: {time_out: idle},
            run_right_to_middle: {time_out: idle},
            run_left_to_middle: {time_out: idle}

        }

    def start(self):
        self.cur_state.enter(self.p2,('start',0))
    def update(self):
        print(self.cur_state)
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
        self.x = 800
        self.y = 120
        self.frame = 0
        self.idle_left_image = load_image('resource/balley/ai_idle_left.png')
        self.idle_right_image = load_image('resource/balley/ai_idle_right.png')
        self.run_right_image = load_image('resource/balley/ai_right_run.png')
        self.run_left_image = load_image('resource/balley/ai_left_run.png')
        self.smash_right_image = load_image('resource/balley/ai_smash.png')
        self.slide_right_image = load_image('resource/balley/ai_slide_right.png')
        self.slide_left_image = load_image('resource/balley/ai_left_slide.png')
        self.reception_right_image = load_image('resource/balley/ai_reception.png')
        self.cur_state = idle
        self.dir = 'left'
        self.score = 0
        self.down = False
        self.ball=ball

        self.run_speed = 300
        self.jump_speed = 500
        self.slide_speed = 400
        self.dist=0

        self.count=0
        self.check_center=False

        self.state_machine = state_machine(self)
        self.bt = None  # bt 속성 초기화
        self.build_behavior_tree()  # bt 설정을 위한 메서드 호출
        self.state_machine.start()



    def update(self):
        self.state_machine.update()


    def handle_event(self,event):
        self.state_machine.handle_event(('INPUT', event))

    def render(self):
        self.state_machine.render()
        draw_rectangle(300,300,330,430)


    def get_bb(self):
        return self.x - 20, self.y - 60, self.x + 20, self.y + 50

    def handle_collusion(self, group, other):
        pass


    def ball_left_side(self):
        if self.ball.x <600:
            self.dir='left'
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    def check_left_run(self):
        if self.ball.x < self.x:
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    def check_left_slide(self):
        if self.ball.y <300 and self.ball.x < self.x and abs(self.x-self.ball.x)>60:
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    def check_right_slide(self):
        if self.ball.y <300 and self.ball.x > self.x and abs(self.x-self.ball.x)>60:
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    def change_state(self, new_state):
        self.state_machine.cur_state = new_state
        return BehaviorTree.SUCCESS

    def check_can_move(self):
        if self.cur_state=="slide_left" or self.cur_state=="slide_right" or self.cur_state=="jump" or self.cur_state=="reception" or  self.cur_state=="smash":
            return BehaviorTree.FAIL
        else:
            return BehaviorTree.SUCCESS

    def left_side(self):
        if(self.ball.x<600):
            self.check_center=True
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def run_right_to_middle(self):
        if(self.x <900):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL



    def build_behavior_tree(self):
        c9 = Condition("무엇을 해도되는가 ?", self.check_can_move)


        c1 = Condition("공이 상대편진영에 있는가?", self.ball_left_side)
        a1 = Action("아이들 상태로 만듬", self.change_state, idle)
        SEQ_IDLE_STATE = Sequence("아이들",c9,c1,a1)

        c2 =Condition("공이 자신보다 왼쪽?", self.check_left_run)
        a2 =Action("왼쪽으로 달림",self.change_state,run_left)
        SEQ_LEFT_RUN_STATE =Sequence("왼쪽으로 달림",c9,c2,a2)


        a3 = Action("오른쪽 으로 달림", self.change_state, run_right)
        SEQ_RIGHT_RUN_STATE = Sequence("오른쪽 으로 달림",c9, a3)

        c4 = Condition("왼쪽 슬라이딩을 해야하는가?", self.check_left_slide)
        a4 = Action("왼쪽 슬라이딩 으로 상태변경", self.change_state,slide_left)
        SEQ_LEFT_SLIDE = Sequence("왼쪽으로 슬라이딩 해버리기",c9,c4,a4)

        c5 = Condition("오른쪽 슬라이딩을 해야하는가?", self.check_right_slide)
        a5 = Action("오른쪽 슬라이딩 으로 상태변경", self.change_state, slide_right)
        SEQ_RIGHT_SLIDE = Sequence("왼쪽으로 슬라이딩 해버리기",c9,c5,a5)

        c6 = Condition("공이 왼쪽 편?",self.left_side)
        c7 =Condition("왼쪽에 있는가?",self.run_right_to_middle)
        a6 =Action("오른쪽으로 상태 변경",self.change_state,run_right_to_middle)
        SEQ_MOVE_RIGHT_TO_CENTER= Sequence("왼쪽에서 센터를 향해 이동",c9,c6,c7,a6)







        root = Selector("테스트용", SEQ_MOVE_RIGHT_TO_CENTER,SEQ_IDLE_STATE,SEQ_LEFT_SLIDE,SEQ_RIGHT_SLIDE,SEQ_LEFT_RUN_STATE,SEQ_RIGHT_RUN_STATE)

        self.bt = BehaviorTree(root)







