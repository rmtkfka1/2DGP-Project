from pico2d import *
from share import game_world, game_framework

TIME_PER_ACTION = 3.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 60


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class Ball:
    def __init__(self):
        self.image =load_image('resource/tennis_ball.png')
        self.fire_image = load_image('resource/fireball.png')
        self.fireshot =False
        # self.x=300
        self.x =900
        self.y=200
        self.frame =0

        self.top = self.y+20
        self.bottom =self.y-20
        self.left =self.x-20
        self.right =self.x+20

        self.start =True ##점수시스템에서 필요한변수
        self.dir ='None'
        self.going_vector= (-10,10)
        self.going_vector= game_world.normalize_vector(self.going_vector[0],self.going_vector[1])
        self.speed_x=700
        self.speed_y=700
        self.gravity =1# 중력 값 (원하는 값으로 조정)


    def update(self):
        self.frame =(self.frame+1)%60

        if(self.start):
            self.top = self.y + 20
            self.bottom = self.y - 20
            self.left = self.x - 20
            self.right = self.x + 20

            self.x += self.speed_x*self.going_vector[0]* game_framework.frame_time
            self.y += self.speed_y*self.going_vector[1]* game_framework.frame_time - self.gravity * game_framework.frame_time
            self.gravity+=500.0*game_framework.frame_time

            if self.going_vector[1] > 0:
                self.dir = 'up'
            else:
                self.dir = 'down'

            self.reflection_wall()


    def reflection_wall(self):
        if (self.y > 680):
            self.y = 680
            self.gravity = 0
            self.speed_x = 700
            self.speed_y = 700
            self.going_vector = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 0, -1)

        if (self.x < 20):
            self.x = 20
            self.gravity = 0
            self.speed_x = 700
            self.speed_y = 700
            self.going_vector = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], -1, 0)

        if (self.x > 1180):
            self.x = 1180
            self.gravity = 0
            self.speed_x = 700
            self.speed_y = 700
            self.going_vector = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 1, 0)

        if (self.y < 60):
            self.y = 60
            self.gravity = 0
            self.speed_x = 700
            self.speed_y = 700
            self.going_vector = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 0, 1)

    def render(self):
        if self.fireshot:
            self.fire_image.clip_draw(self.frame*101,0,101,293,self.x,self.y+101)
        else:
            self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-20, self.y-20, self.x +20, self.y +20

    def handle_collusion(self,group,other):
        if group == "player1:ball":
            print("충돌")
            self.gravity=0

            if other.cur_state == 'smash':
                if(self.x < other.x):
                    self.going_vector = game_world.normalize_vector(-25, 15)

                if (self.x > other.x ):
                    self.speed_x=1000
                    self.going_vector = game_world.normalize_vector(20, -15)
            else:
                self.speed_x = 700
                if (self.x < other.x):
                    self.going_vector = game_world.normalize_vector(-10, 10)

                if (self.x > other.x):
                    self.going_vector = game_world.normalize_vector(10, 10)

