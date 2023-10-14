from pico2d import *

open_canvas(1250,700)
ch=load_image("1.png")
frame=0

running=True
y=100

def handle_events():
    global running
    global mx,my
    global frame
    global y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            y+=10

while(running):
    clear_canvas()
    handle_events()  # 사용자 입력을 받는다
    ch.clip_draw(frame*40,0,40,40,1100,y,200,200)
    frame = (frame + 1) % 5
    update_canvas()
    delay(0.1)



