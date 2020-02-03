import cv2 
import time
import datetime

cam=cv2.VideoCapture(0)
ret_val, img=cam.read()
ret_val, img=cam.read()
while(True):
	
	ret_val, img=cam.read()
	cv2.imshow('mycam', img)
	#cv2.waitKey(1)
	
	now=datetime.datetime.now()
	
	cv2.imwrite(str(now.strftime("%y_%m_%d_%H_%M_%S")+".jpg"),img)
	print("saved...")
	
	
	
	
	time.sleep(5000)
		
cv2.destroyAllWindows()
