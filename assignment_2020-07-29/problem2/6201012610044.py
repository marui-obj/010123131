import pygame
import pygame.camera
from pygame.locals import *
import sys

rect_list = []

def open_camera( frame_size=(1280,720),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    print( 'Mumber of cameras found: ', len(list_cameras) )
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 
def rectPos(mouse):
    x,y = mouse[0],mouse[1]
    for rect in rect_list:
        if (x > rect[0]) and (x < rect[0]+rect[2]) and (y > rect[1]) and (y < rect[1] + rect[3]):
            return rect_list.index(rect)
    return None


scr_w, scr_h = 1280, 720
pygame.init()
camera = open_camera()
if camera:
    camera.start()
else:
    print('Cannot open camera')
    sys.exit(-1)

screen = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
M,N = 10,10
rw, rh = scr_w//M, scr_h//N
img_list = []
img = None
current_img = []
while(img == None):
    img = camera.get_image()
for i in range(M):
        for j in range(N):
            rect = (i*rw, j*rh, rw, rh)
            rect_list.append(rect)      
for i in range(len(rect_list)):
    current_img.append(i)
    
rect_up,rect_down = None,None
click = False
is_running = True 
while is_running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )
        if e.type == pygame.MOUSEBUTTONDOWN:
            click = True
            mouse_down = pygame.mouse.get_pos()
            rect_down = rectPos(mouse_down)
        elif e.type == pygame.MOUSEBUTTONUP:
            click = False
            mouse_up = pygame.mouse.get_pos()
            rect_up = rectPos(mouse_up)
        if rect_up != rect_down and rect_up != None and rect_down != None and not(click):
            current_img[rect_down],current_img[rect_up] = current_img[rect_up],current_img[rect_down]
            rect_up,rect_down = None,None

    img = camera.get_image()
    if img is None:
        continue
    else:
        for split in range(len(rect_list)):
            img_list.append(img.subsurface(rect_list[split]))
    for i in range(len(rect_list)):
        surface.blit( img_list[current_img[i]], rect_list[i],)
        pygame.draw.rect( surface, (0,255,0), rect_list[i], 1)
    screen.blit( surface, (0,0) )
    pygame.display.update()
    img_list = []
# close the camera
camera.stop()
print('Done....')
###################################################################