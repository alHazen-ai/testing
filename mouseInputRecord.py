import cv2

#display all the mouse events
#[print(i) for i in dir(cv2) if "EVENT" in i]

def clickEvent(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        a.append(x)
        b.append(y)
        print(x,' ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x)+','+str(y), (x,y), font, fontScale=1, color=(255,0,0))
        cv2.imshow("image", img)
        return x, y

if __name__== "__main__":
    a=[]
    b=[]
    img = cv2.imread('scan.jpg', 0)
    width, height = img.shape

    img = cv2.resize(img,(width, height), 0.5, 0.5)
    cv2.imshow("image", img)

    cv2.setMouseCallback("image", clickEvent)
    print(b," ", a)

    cv2.waitKey(0)
    cv2.destroyAllWindows()