mydict={1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6,0:6}
n=int(input())
for i in range (n):
    leds=input()
    result=0
    for j in range(len(leds)):
        led=int(leds[j])
        result+=mydict[led]
    print(result," Leds")
