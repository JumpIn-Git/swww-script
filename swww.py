import os
import random
import subprocess
import time

wall_path = ("~/.config/hypr/wall") #Change to your wallpaper folder
interval = None #How many minutes between randomizing wallpaper, None to not change
if wall_path.startswith("~"):
    wall_path = os.path.expanduser(wall_path)
walls = []
random_wall = None

if subprocess.run(["which", "swww"], stdout=subprocess.DEVNULL).returncode != 0:
    subprocess.run('notify-send "Installing swww" "Please wait, this can take some time."', shell=True)
    subprocess.run(["yay", "-S", "--noconfirm", "swww"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    subprocess.run('notify-send "swww installed!"', shell=True)

subprocess.run("swww-daemon", stderr=subprocess.DEVNULL)
while True:
    walls.clear()
    for wall_name in os.listdir(wall_path):
        path = os.path.join(wall_path, wall_name)
        if os.path.isfile(path) and os.path.splitext(path)[1].lower() == {".jpeg", ".jpg", ".png", ".gif", ".pnm", ".tga", ".tiff", ".webp", ".bmp", ".farbfeld"}:
            walls.append(wall_name)

    if walls:
        while True:
            temp = random.choice(walls)
            if random_wall == temp:
                continue
            else:
                random_wall = temp
                break
        subprocess.run(f'notify-send "Changing Wallpaper" "to {random_wall}"', shell=True)
        subprocess.run(f'swww img {os.path.join(wall_path, random_wall)}', shell=True)
        if interval != None:
            time.sleep(interval*60)
            continue
    else:
        subprocess.run('notify-send "No wallpapers found" "Please add a wallpaper/change the path and relaunch me."', shell=True)
        exit()
