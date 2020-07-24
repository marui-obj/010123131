import threading
import pygame

print( 'File:', __file__ )

def mandelbrot(c,max_iters=100):
    i = 0
    z = complex(0,0)
    while abs(z) <= 2 and i < max_iters:
        z = z*z + c
        i += 1 
    return i
def thread(id,surface,lock,barrier,max_N):
    x = 0
    max_h = int(scr_h/max_N*id)
    y = int(max_h - scr_h/max_N)
    scale = 0.006
    offset = complex(-0.55,0.0)
    while y < max_h:
        while x <= scr_w:
            re = scale*(x-scr_w/2) + offset.real
            im = scale*(y-scr_h/2) + offset.imag
            c = complex( re, im )
            color = mandelbrot(c, 63)
            r = (color << 6) & 0xc0
            g = (color << 4) & 0xc0
            b = (color << 2) & 0xc0
            with lock:
                surface.set_at( (x, y), (255-r,255-g,255-b) )
            try:
                barrier.wait()
            except threading.BrokenBarrierError:
                pass
            x += 1
        x = 0
        y += 1

N = 100

lock = threading.Lock()

barrier = threading.Barrier(N+1)


list_threads = []

# initialize pygame
pygame.init()

# create a screen of width=600 and height=400
scr_w, scr_h = 500, 500
screen = pygame.display.set_mode( (scr_w, scr_h) )

# set window caption
pygame.display.set_caption('Fractal Image: Mandelbrot') 

# create a clock
clock = pygame.time.Clock()

# create a surface for drawing
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

first_create = True 

for i in range(N):
    id = (i+1)
    t = threading.Thread(target=thread, args=(id,screen,lock,barrier,N))
    t.setName( 'Thread-{:03d}'.format(id) )
    list_threads.append( t )


for t in list_threads:
    t.start()

running = True
w2, h2 = scr_w/2, scr_h/2 # half width, half screen
while running:

    try:
        barrier.wait()
    except threading.BrokenBarrierError:
        pass



    with lock:
        # draw the surface on the screen
        screen.blit( surface, (0,0) )
    # update the display
    pygame.display.flip()

    clock.tick(120) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

barrier.reset()
pygame.quit()
print( 'PyGame done...')
################################################################