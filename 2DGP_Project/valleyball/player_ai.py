from pico2d import *

from share import game_framework
from tennis.behavior_tree import BehaviorTree, Action, Condition, Selector, Sequence


def idle_t(e):
    return e[0] == 'TIME_OUT_IDLE'


def jump_t(e):
    return e[0] == 'TIME_OUT_JUMP'


def left_sliding_t(e):
    return e[0] == 'TIME_OUT_LEFT_SLIDING'


def right_sliding_t(e):
    return e[0] == 'TIME_OUT_RIGHT_SLIDING'


def run_right_t(e):
    return e[0] == 'TIME_OUT_RUN_RIGHT'


def run_left_t(e):
    return e[0] == 'TIME_OUT_RUN_LEFT'


def run_left_to_middle_t(e):
    return e[0] == 'TIME_OUT_RUN_LEFT_TO_MIDDLE'


def run_right_to_middle_t(e):
    return e[0] == 'TIME_OUT_RUN_RIGHT_TO_MIDDLE'


def reception_t(e):
    return e[0] == 'TIME_OUT_RECEPTION'


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 12

TIME_PER_ACTION_SMASH = 1.2
ACTION_PER_SMASH = 1.0 / TIME_PER_ACTION_SMASH
FRAMES_PER_SMASH = 13

TIME_PER_ACTION_SLIDE = 1.0
ACTION_PER_SLIDE = 1.0 / TIME_PER_ACTION_SLIDE
FRAMES_PER_SLIDE = 15

TIME_PER_ACTION_RECEPTION = 1.0
ACTION_PER_RECEPTION = 1.0 / TIME_PER_ACTION_RECEPTION
FRAMES_PER_RECEPTION = 11

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class idle:
    @staticmethod
    def enter(player, e):
        player.cur_state = 'idle'
        pass

    @staticmethod
    def exit(player, e):
        player.cur_state = 'idle'
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

        player.bt.run()

    @staticmethod
    def render(player):
        if player.dir == 'left':
            player.idle_left_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        if player.dir == 'right':
            player.idle_right_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class jump:
    @staticmethod
    def enter(player, e):
        player.down = False

        player.frame = 0
        player.cur_state = 'jump'
        pass

    @staticmethod
    def exit(player, e):
        player.cur_state = 'idle'
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

        if (player.y < 400 and player.down == False):
            player.y += player.jump_speed * game_framework.frame_time

        if (player.y > 400):
            player.y = 400
            player.down = True

        if player.y > 120 and player.down == True:
            player.y -= player.jump_speed * game_framework.frame_time

        if player.y < 120:
            player.state_machine.handle_event(('TIME_OUT_IDLE', 0))

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

    @staticmethod
    def exit(player, e):
        player.cur_state = 'idle'
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
        player.dir = 'left'
        player.cur_state = 'run_left'

    @staticmethod
    def exit(player, e):
        player.cur_state = 'idle'
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
        if (player.x > 650):
            player.x -= player.run_speed * game_framework.frame_time

        player.bt.run()

    @staticmethod
    def render(player):
        player.run_left_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class smash:
    @staticmethod
    def enter(player, e):
        player.frame = 0
        player.dist = 0
        player.cur_state = 'smash'


    @staticmethod
    def exit(player, e):
        player.dir = 'left'
        player.frame = 0
        player.dist = 0

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
            player.state_machine.handle_event(('TIME_OUT_IDLE', 0))

        player.bt.run()

    @staticmethod
    def render(player):
        player.smash_right_image.clip_draw(int(player.frame) * 64, 0, 64, 93, player.x, player.y)
        pass


class slide_right:
    @staticmethod
    def enter(player, e):
        player.down = False
        player.dist = 0
        player.cur_state = 'slide_right'


    @staticmethod
    def exit(player, e):
        player.dir = 'right'

        player.cur_state = 'idle'
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_SLIDE * ACTION_PER_SLIDE * game_framework.frame_time) % 15

        player.dist += 20 * game_framework.frame_time

        if (player.x < 1170):
            player.x += player.slide_speed * game_framework.frame_time

        if player.dist > 20:
            player.state_machine.handle_event(('TIME_OUT_IDLE', 0))

        player.bt.run()

    @staticmethod
    def render(player):
        player.slide_right_image.clip_draw(int(player.frame) * 64, 0, 64, 93, player.x, player.y)
        pass


class slide_left:
    @staticmethod
    def enter(player, e):
        player.down = False
        player.frame = 15
        player.dist = 0

        player.cur_state = 'slide_left'

    @staticmethod
    def exit(player, e):
        player.dir = 'left'
        player.cur_state = 'idle'



        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame - FRAMES_PER_SLIDE * ACTION_PER_SLIDE * game_framework.frame_time) % 15

        player.dist += 20 * game_framework.frame_time

        if (player.x > 650):
            player.x -= player.slide_speed * game_framework.frame_time

        if player.dist > 20:
            player.state_machine.handle_event(('TIME_OUT_IDLE', 0))

        player.bt.run()

    @staticmethod
    def render(player):
        player.slide_left_image.clip_draw(int(player.frame) * 64, 0, 64, 93, player.x, player.y)
        pass


class run_left_to_middle:
    @staticmethod
    def enter(player, e):
        player.dir = 'left'
        player.cur_state = 'run_left_to_middle'


    @staticmethod
    def exit(player, e):
        player.cur_state = 'idle'
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

        player.x -= player.run_speed * game_framework.frame_time

        if (player.x <= 1000):
            player.x = 1000
            player.state_machine.handle_event(('TIME_OUT_IDLE', 0))

        player.bt.run()

    @staticmethod
    def render(player):
        player.run_left_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class run_right_to_middle:
    @staticmethod
    def enter(player, e):
        player.dir = 'left'
        player.cur_state ='reception'


    @staticmethod
    def exit(player, e):
        player.cur_state ='idle'
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

        player.x += player.run_speed * game_framework.frame_time

        if (player.x >= 1000):
            player.x=1000
            player.state_machine.handle_event(('TIME_OUT_IDLE', 0))

        player.bt.run()

    @staticmethod
    def render(player):
        player.run_right_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class reception:
    @staticmethod
    def enter(player, e):
        player.wait_time = get_time()
        player.down = False
        player.dir = 'right'
        player.frame = 0
        player.cur_state ='reception'


    @staticmethod
    def exit(player, e):

        player.cur_state = 'idle'
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame - FRAMES_PER_RECEPTION * ACTION_PER_RECEPTION * game_framework.frame_time) % 11

        if (get_time() - player.wait_time > 1.0):
            player.state_machine.handle_event(('TIME_OUT_IDLE', 0))

        player.bt.run()

    @staticmethod
    def render(player):
        player.reception_right_image.clip_draw(int(player.frame) * 70, 0, 70, 93, player.x, player.y)
        pass


class state_machine:
    def __init__(self, p2):
        self.p2 = p2
        self.cur_state = self.p2.cur_state
        self.now =self.p2.now
        self.table = {
            idle: {idle_t: idle, jump_t: jump, left_sliding_t: slide_left, right_sliding_t: slide_right,
                   run_right_t: run_right, run_left_t: run_left, run_left_to_middle_t: run_left_to_middle,
                   run_right_to_middle_t: run_right_to_middle,reception_t:reception},
            jump: {idle_t: idle},
            run_right: {idle_t: idle, jump_t: jump, left_sliding_t: slide_left, right_sliding_t: slide_right,
                        run_right_t: run_right, run_left_t: run_left, run_left_to_middle_t: run_left_to_middle,
                        run_right_to_middle_t: run_right_to_middle,reception_t:reception},
            run_left: {idle_t: idle, jump_t: jump, left_sliding_t: slide_left, right_sliding_t: slide_right,
                       run_right_t: run_right, run_left_t: run_left, run_left_to_middle_t: run_left_to_middle,
                       run_right_to_middle_t: run_right_to_middle,reception_t:reception},
            smash: {idle_t: idle},
            slide_right: {idle_t: idle, jump_t: jump},
            slide_left: {idle_t: idle, jump_t: jump},
            reception: {idle_t: idle, jump_t: jump},
            run_left_to_middle:{idle_t: idle, jump_t: jump},
            run_right_to_middle: {idle_t: idle, jump_t: jump},

        }


    def start(self):
        self.cur_state.enter(self.p2, ('start', 0))

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
    def __init__(self, ball):
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
        self.now ='idle'
        self.dir = 'left'
        self.score = 0
        self.down = False
        self.ball = ball

        self.run_speed = 300
        self.jump_speed = 500
        self.slide_speed = 400
        self.dist = 0

        self.count = 0
        self.check_center = False


        self.state_machine = state_machine(self)
        self.bt = None  # bt 속성 초기화
        self.build_behavior_tree()  # bt 설정을 위한 메서드 호출
        self.state_machine.start()

    def update(self):
        self.state_machine.update()
        print(self.cur_state)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def render(self):
        self.state_machine.render()
        draw_rectangle(0, 200, 90, 250)

    def get_bb(self):
        return self.x - 20, self.y - 60, self.x + 20, self.y + 50

    def handle_collusion(self, group, other):
        pass

    def change_state(self, new_state):
        if self.cur_state=='jump' or self.cur_state=='slide_right' or self.cur_state=='slide_left':
            return BehaviorTree.FAIL

        if new_state == run_right:
            self.state_machine.handle_event(('TIME_OUT_RUN_RIGHT', 0))
            return BehaviorTree.SUCCESS

        elif new_state == run_left:
            self.state_machine.handle_event(('TIME_OUT_RUN_LEFT', 0))
            return BehaviorTree.SUCCESS

        elif new_state == jump:
            self.state_machine.handle_event(('TIME_OUT_JUMP', 0))
            return BehaviorTree.SUCCESS

        elif new_state == slide_left:
            self.state_machine.handle_event(('TIME_OUT_LEFT_SLIDING', 0))
            return BehaviorTree.SUCCESS

        elif new_state == slide_right:
            self.state_machine.handle_event(('TIME_OUT_RIGHT_SLIDING', 0))
            return BehaviorTree.SUCCESS

        elif new_state == idle:
            self.state_machine.handle_event(('TIME_OUT_IDLE', 0))
            return BehaviorTree.SUCCESS

        elif new_state == run_left_to_middle:
            self.state_machine.handle_event(('TIME_OUT_RUN_LEFT_TO_MIDDLE', 0))
            return BehaviorTree.SUCCESS

        elif new_state == run_right_to_middle:
            self.state_machine.handle_event(('TIME_OUT_RUN_RIGHT_TO_MIDDLE', 0))
            return BehaviorTree.SUCCESS

        elif new_state == reception:
            self.state_machine.handle_event(('TIME_OUT_RECEPTION', 0))
            return BehaviorTree.SUCCESS

    def ball_left_side(self):
        if self.ball.x<600:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def ball_right_side(self):
        if self.ball.x>=600:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def ball_smaller_than_me(self):
        if self.ball.x < self.x:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def ball_bigger_than_me(self):
        if self.ball.x > self.x:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL


    def have_to_jump(self):
        if self.ball.y>700:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def have_to_reception(self):
        if abs(self.x- self.ball.x)<30 and abs(self.ball.y - self.y) <70:
            return BehaviorTree.SUCCESS
        else :
            return BehaviorTree.FAIL


    def have_to_right_slide(self):
        if self.ball.x > self.x and abs(self.x - self.ball.x) > 50 and self.ball.y<300:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def check_right_run_to_middle(self):
        if self.x < 1000:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def check_left_run_to_middle(self):
        if self.x >= 1000:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL


    def build_behavior_tree(self):
        c1 = Condition("공이 상대편에 가있는가?", self.ball_left_side)
        c2 = Condition("중심기준 왼쪽편에 본인이 존재하는가?", self.check_left_run_to_middle)
        a1 = Action(" ", self.change_state,run_left_to_middle)

        SEQ_RUN_RIGHT_TO_MIDDLE=Sequence("상태: RUN_RIGHT_TO_MIDDLE",c1,c2,a1)


        c3 = Condition("중심기준 오른쪽편에 본인이 존재하는가?", self.check_right_run_to_middle)
        a2 = Action(" ", self.change_state, run_right_to_middle)

        SEQ_RUN_LEFT_TO_MIDDLE = Sequence("상태: RUN_RIGHT_TO_MIDDLE", c1, c3, a2)


        SEL_DEFENCE = Selector("방어",SEQ_RUN_RIGHT_TO_MIDDLE,SEQ_RUN_LEFT_TO_MIDDLE)

        ######################################################################

        c4 = Condition("공이 우리편에 넘어왔는가?" , self.ball_right_side)
        c5 = Condition("공이 자기기준 왼쪽편에 있는가?", self.ball_smaller_than_me)
        a3 = Action("  ",self.change_state,run_left)

        SEQ_RUN_LEFT = Sequence("상태 : RUN_LEFT",c4,c5,a3)
        #################################################################
        c6 = Condition("공이 자기기준 오른쪽 있는가?", self.ball_bigger_than_me)
        a4 = Action(" ", self.change_state, run_right)

        SEQ_RUN_RIGHT = Sequence("상태 : RUN_RIGHT", c4, c6, a4)
        #################################################################



        c8 =Condition("오른쪽으로 슬라이딩해야되는가?",self.have_to_right_slide)
        a6 =Action(" ",self.change_state,slide_right)
        SEQ_RIGHT_SILDE = Sequence("상태 : SLIDE_RIGHT",c4,c8,a6)


        c9 =Condition("리샙션해야하는가?",self.have_to_reception)
        a7 =Action(" ",self.change_state,reception)
        c10 = Condition(" ",self.have_to_jump)
        a8 =Action("점프",self.change_state,jump)
        SEQ_RECEPTION = Sequence("상태 : 리샙션", c9,a7,c10,a8)



        SEL_ATTRACK=Selector("어택",SEQ_RECEPTION,SEQ_RIGHT_SILDE,SEQ_RUN_LEFT,SEQ_RUN_RIGHT)

        ######################################################
        root = Selector("최종결과",SEL_DEFENCE,SEL_ATTRACK)

        self.bt=BehaviorTree(root)


