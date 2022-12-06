#24 hour clock format.
def Angle(hh,mm):
    hh=hh%12
    hours=(hh*360)//12+(mm*360)//(12*60)
    minutes=(mm*360)//(60)
    angle=abs(hours-minutes)
    if angle>180:
        angle=360-angle
    return angle
    
    
hh=int(input("hour:"))
mm=int(input("minute:"))
print("Degrees:",Angle(hh,mm))