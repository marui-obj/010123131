
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
        if (x > rect[0][0]) and (x < rect[0][0]+rect[0][2]) and (y > rect[0][1]) and (y < rect[0][1] + rect[0][3]):
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
M,N = 5,5
rw, rh = scr_w//M, scr_h//N
for i in range(M):
        for j in range(N):
            # draw a green frame (tile)
            rect = (i*rw, j*rh, rw, rh),(i,j)
            rect_list.append(rect)
            
black = rect_list.copy()

img = None
is_running = True 
while is_running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            rect_pos = rectPos(mouse_pos)
            if rect_pos != None:
                black[rect_pos] = None
                
                
    # try to capture the next image from the camera 
    img = camera.get_image()
    if img is None:
        continue

    # get the image size
    img_rect = img.get_rect()
    img_w, img_h = img_rect.w, img_rect.h
    for b in black:
        if b == None:
            continue
        pygame.draw.rect(img,(0,0,0),b[0])
        pygame.draw.rect( img, (0,255,0), b[0], 1)
    for rect in rect_list:
        surface.blit( img, rect[0], rect[0] )

    screen.blit( surface, (0,0) )
    pygame.display.update()

# close the camera
camera.stop()

print('Done....')
###################################################################