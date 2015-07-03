import nxppy
import time
import sys
import signal
import pygame

import os

mifare = nxppy.Mifare()

f = open("user_list.csv",'r')

user_hash = {}

for line in f:
    user_hash[line.split(',')[0]] = line.split(',')[1].strip()

def signal_term_handler(signum = None, frame = None):
    sys.stderr.write("Terminated.\n")
    f.close()
    sys.exit(0)

for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]: 
    signal.signal(sig, signal_term_handler)

class pyscope :
    screen = None;
    
    def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print "I'm running under X display = {0}".format(disp_no)
        
        # Check which frame buffer drivers are available
        # Start with fbcon since directfb hangs with composite output
        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False
        for driver in drivers:
            # Make sure that SDL_VIDEODRIVER is set
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print 'Driver: {0} failed.'.format(driver)
                continue
            found = True
            break
    
        if not found:
            raise Exception('No suitable video driver found!')
        
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print "Framebuffer size: %d x %d" % (size[0], size[1])
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0, 0, 255))        
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

    def test(self):
        uid = None
        # Get a font and use it render some text on a Surface.
        font = pygame.font.Font(None, 80)
        for i in range(30):
            #clear the screen
            self.screen.fill((0, 0, 255))     
            # Render some text with a background color
            timestr = time.strftime("%H:%M:%S", time.localtime())
            text_surface = font.render(timestr,
                True, (255, 255, 255))
            # Blit the text
            self.screen.blit(text_surface, (100, 30))
            # Update the display
            pygame.display.update()
            try:
                uid = mifare.select()
            except nxppy.SelectError:
                pass
            if uid is not None:
                #print "Card detected:", uid
                if uid in user_hash.keys():
                    text_surface = font.render("Hello",
                        True, (255, 255, 255))
                    self.screen.blit(text_surface, (140, 180))                	
                    text_surface = font.render(user_hash[uid],
                        True, (255, 255, 255))
                    self.screen.blit(text_surface, (160, 240))
                uid = None #reset uid to None
                pygame.display.update()
                time.sleep(1) #pause for 1 seconds
            time.sleep(1)
        #get out of full screen
        #size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        pygame.quit()

# Create an instance of the PyScope class
scope = pyscope()
scope.test()
# Wait 10 seconds



