import cv2

img = cv2.imread("solar-system.jpg")

cv2.imshow("output",img)

cv2.waitKey(0)

cv2.putText(img,  
            "Sun",
            (20, 300),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,  
            (255,255,255)
           )

cv2.putText(img,  
            "Mercury",
            (25, 320),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,  
            (255,255,255)
           )

cv2.putText(img,  
            "Venus",
            (28, 330),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,  
            (255,255,255)
           )     

cv2.putText(img,  
            "Earth",
            (30, 340),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,  
            (255,255,255)
           )                      

cv2.putText(img,  
            "Mars",
            (32, 350),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,  
            (255,255,255)
           )     

cv2.putText(img,  
            "Jupitar",
            (34, 360),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,  
            (255,255,255)
           ) 

cv2.putText(img,  
            "Saturn",
            (36, 370),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,  
            (255,255,255)
           )                               

cv2.putText(img,  
            "Uranus",
            (38, 380),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,  
            (255,255,255)
           )               

cv2.putText(img,  
            "Neptune",
            (40, 390),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,  
            (255,255,255)
           )          
                  