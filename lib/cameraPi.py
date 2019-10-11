'''
Camera Interfacing for the Raspberry Pi Camera (V2)
'''

import numpy
import cv2

from picamera import PiCamera

class AMCamera:
    '''A Camera setup and capture class for the PiCamV2'''
    
    def __init__(self, camParams):
        '''Initialise the camera, based on a dict of settings'''
        
        if camParams['resolution'][0] % 16 != 0 or camParams['resolution'][1] % 16 != 0:
            print("Error: Camera resolution must be divisible by 16")
            return
            
        self.camParams = camParams
        self.camera = PiCamera(resolution=camParams['resolution'], framerate=camParams['framerate'],sensor_mode=camParams['sensor_mode'])
        self.camera.rotation = camParams['rotation']
        
        self.image = numpy.empty((self.camera.resolution[0] * self.camera.resolution[1] * 3,), dtype=numpy.uint8)
        
        # Set ISO to the desired value
        camera.iso = 100
        # Wait for the automatic gain control to settle
        sleep(2)
        # Now fix the values
        camera.shutter_speed = camera.exposure_speed
        camera.exposure_mode = 'off'
        g = camera.awb_gains
        camera.awb_mode = 'off'
        camera.awb_gains = g
        
    def getNumberImages(self):
        '''Get number of loaded images'''
        return None

    def getFileName(self):
        '''Get current file in camera'''
        return None
        
    def getImage(self):
        ''' Capture a single image from the Camera '''
        
        self.camera.capture(self.image, format="bgr", use_video_port=self.camParams['use_video_port'])
        
        # and convert to OpenCV greyscale format
        self.image = self.image.reshape((self.camera.resolution[1], self.camera.resolution[0], 3))
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) 
