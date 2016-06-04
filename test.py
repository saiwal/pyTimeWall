
import os

current_path = os.path.dirname(os.path.realpath(__file__))
current_path = current_path + "/"

walls = [
	"9-Late-Night.png","1-Early-Morning.png","2-Morning.png","3-Late-Morning.png","4-Afternoon.png","5-Late-Afternoon.png","6-Evening.png","7-Late-Evening.png","8-Night.png"
	]
os.system('xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s %s%s'%(current_path,walls[1]))
