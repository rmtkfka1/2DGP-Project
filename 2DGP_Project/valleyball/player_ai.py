from pico2d import *

from share import game_framework
from tennis.behavior_tree import BehaviorTree, Action, Condition, Selector ,Sequence
from valleyball import balley_2player_mode


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

        if player.down==True:
            player.y -= player.jump_speed * game_framework.frame_time

        player.bt.run()


        if player.y<120:
            player.state_machine.handle_event(('TIME_OUT',0))

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

        player.bt.run()

        if (player.x < 1200):
            player.x += player.run_speed * game_framework.frame_time

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
        player.dir = 'left'
        player.cur_state = 'run_right_to_middle'
        player.frame = 0

    @staticmethod
    def exit(player, e):

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
        player.job =True
        player.cur_state ='slide_right'
        player.frame=0
        player.dist =0
    @staticmethod
    def exit(player, e):
        player.frame = 0
        player.job =False
        player.dist =0
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

        #
        player.bt.run()
    @staticmethod
    def render(player):
        player.slide_right_image.clip_draw(int(player.frame) * 64, 0, 64, 93, player.x, player.y)
        pass



class slide_left:
    @staticmethod
    def enter(player, e):
        player.down = False
        player.job =True
        player.cur_state ='slide_left'
        player.frame=15
        player.dist =0
    @staticmethod
    def exit(player, e):
        player.job =False
        player.dist = 0
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame - FRAMES_PER_SLIDE * ACTION_PER_SLIDE * game_framework.frame_time) % 15

        if (player.x < 650 and player.x > 610):
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
        self.x = 1000
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
        self.job =False
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
        draw_rectangle(300,300,400,430)


    def get_bb(self):
        return self.x - 20, self.y - 60, self.x + 20, self.y + 50

    def handle_collusion(self, group, other):
        pass


    def check_left_run(self):
        if self.ball.x >600 and self.ball.x < self.x:
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    def check_right_run(self):
        if self.ball.x >600 and self.ball.x > self.x:
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    def check_left_slide(self):
        if self.ball.x >600 and self.x > self.ball.x and(self.x-self.ball.x)>50:
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    def check_right_slide(self):
        if self.ball.x >600 and self.x < self.ball.x and abs(self.x-self.ball.x)>50:
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    def can_go(self):
        if self.cur_state == jump or self.cur_state == slide_left or self.cur_state == slide_right:
            return BehaviorTree.FAIL
        else:
            return BehaviorTree.SUCCESS

    def change_state(self, new_state):
        if self.job ==True:
            return BehaviorTree.FAIL
        self.state_machine.cur_state = new_state
        return BehaviorTree.SUCCESS


    def left_side(self): ##공이 상대편진영에 있는가 ?
        if(self.ball.x<600):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL


    def check_self_left_side(self): ##자기기준 왼쪽편에 존재하는가?
        if self.x<900:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL


    def check_self_right_side(self): ##자기기준 오른쪽편에 존재하는가?
        if self.x>900:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL


    def build_behavior_tree(self):
        c0 =Condition("상태를 바꿔도 괜찮은가 ?", self.can_go)
        c1 = Condition("공이 상대편 진영에 있는가?", self.left_side)
        #######################################################
        ##공이 상대편일떄 행동패턴
        c2 = Condition("자기 진영기준 왼쪽편에 서있는가?",self.check_self_left_side)
        a1 = Action("왼쪽에서 센터를 향해으로 달린다.",self.change_state,run_right_to_middle)

        SEQ_RIGHT_RUN_TO_CENTER = Sequence("result:센터를향해 왼쪽에서 오른쪽으로 달림",c0,c1,c2,a1)

        c3 = Condition("자기 진영기준 오른편에 서있는가?", self.check_self_right_side)
        a2 = Action("result :오른쪽에서 센터를 향해 달린다.",self.change_state,run_left_to_middle)
        SEQ_LEFT_RUN_TO_CENTER = Sequence("result:센터를향해 오른쪽에서 왼쪽으로 달림",c0, c1, c3, a2)
        SLELECTOR_DEFENCE =Selector("방어를 위해 센터로 이동",SEQ_RIGHT_RUN_TO_CENTER,SEQ_LEFT_RUN_TO_CENTER)
        #######################################################

        #######################################################
        a3= Action("아이들 상태로 만듬",self.change_state,idle)
        SEQ_IDLE =Sequence("아이들 상태로만듬",c0, c1,a3 )
        #######################################################



        ###### 왼쪽편 or 오른쪽 런 결졍
        ##공이 넘어 왔을때 행동패턴
        ########################### 달리기 #############################
        c3 = Condition("공이 넘어왔을대 자기보다 왼쪽편에 존재하는가?", self.check_left_run)
        a4 = Action("왼쪽으로 달린다.",self.change_state, run_left)
        SEQ_LEFT_RUN = Sequence("왼쪽으로 달린다" , c0 , c3 ,a4)

        c4 = Condition("공이 넘어왔을대 자기보다 오른쪽편에 존재하는가?", self.check_right_run)
        a5 = Action("오른쪽 으로 달린다.", self.change_state, run_right)
        SEQ_RIGHT_RUN = Sequence("오른쪽으로 달린다",c0, c4,a5)

        SELECTOR_RUN_LEFT_RIGHT = Selector("REUSLT ",SEQ_LEFT_RUN,SEQ_RIGHT_RUN)
        ###########################################################


        ############################# 슬라이딩 ################################
        c5 = Condition("왼쪽으로 슬라이딩을 해야되는가 ??", self.check_left_slide)
        a6 =Action("왼쪽으로 슬라이딩 해도되는가?",self.change_state,slide_left)
        SEQ_SLIDE_LEFT = Sequence("왼쪽으로 슬라이딩",c0, c5, a6)

        c6 = Condition("오른으로 슬라이딩을 해야되는가 ??", self.check_left_slide)
        a7 = Action("오른쪽으로 슬라이딩 해도되는가?", self.change_state, slide_left)
        SEQ_SLIDE_RIGHT = Sequence("오른쪽으로 슬라이딩",c0 , c6, a7)

        SELECTOR_SLIDE = Selector("REUSLT ", SEQ_SLIDE_LEFT, SEQ_SLIDE_RIGHT)


        SEQ_RESULT = Selector("FINAL RESULT",SELECTOR_SLIDE, SELECTOR_RUN_LEFT_RIGHT)
        self.bt = BehaviorTree(SEQ_RESULT)







