import tkinter as tk
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
import shutil
import os

teams = None
divisions = None
abvs = {}
maps = None
gamemodes = None
GAMENAME = None

game1 = {"Team 1": "", "Team 2": ""}
game2 = {"Team 1": "", "Team 2": ""}

with open('settings\gamemodes.txt', 'r') as f:
    # Read the contents of the file into a list
    gamemodes = f.readlines()

with open('settings\maps.txt', 'r') as f:
    # Read the contents of the file into a list
    maps = f.readlines()

with open('settings\\teams.txt', 'r') as f:
    # Read the contents of the file into a list
    teams = f.readlines()

with open('settings\divisions.txt', 'r') as f:
    # Read the contents of the file into a list
    divisions = f.readlines()

with open('settings\\abvs.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line:
            key, value = line.split(',')
            key = key.strip()
            value = value.strip()
            abvs[key] = value

with open('settings\game.txt', 'r') as file:
    GAMENAME = file.readline().rstrip('\n')



gamemodes = [gamemode.rstrip('\n') for gamemode in gamemodes]
maps = [map.rstrip('\n') for map in maps]
teams = [team.rstrip('\n') for team in teams]
divisions = [division.rstrip('\n') for division in divisions]
weeks = ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "Playoffs", "Chumps", "TBD"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "TBD"]
seasons = ["Summer","Fall","Winter","Spring", "TBD"]

directory = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory"

divisionspath = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Assets\TimeDivs"

weekpath = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Assets\Week\Options"


scorespath = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Assets\Scores"

team1path = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Team 1"
team2path = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Team 2"
team3path = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Team 3"
team4path = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Team 4"

game1path = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Game 1"
game2path = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Game 2"

leftcasterpath = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Game 1\Left Caster.txt"
rightcasterpath = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Game 1\Right Caster.txt"

def large_first(one,two):

    if one != "" and two != "":
        if int(one) > int(two):
            return str(one), str(two)
        else:
            return str(two), str(one) 
    else:
        return None, None



def score_tab_submit(game1_scores, game2_scores, game1_winners, game2_winners):
    directory = "C:/Dropbox/Teams/CRL/Alpha/Scene Switcher Directory/"

    assets = "C:/Dropbox/Teams/CRL/Alpha/Scene Switcher Directory/zz Assets zz/"

    game1_score_dest = "C:/Dropbox/Teams/CRL/Alpha/Scene Switcher Directory/zz Assets zz/Game 1/Map Set/"
    game2_score_dest = "C:/Dropbox/Teams/CRL/Alpha/Scene Switcher Directory/zz Assets zz/Game 2/Map Set/"

    count = 0

    for winner in game1_winners:
        count += 1
        game1_winner_path = os.path.join(directory, winner + "/Map Win/Win.png")
        game1_winner_dest = os.path.join(game1_score_dest, "Map " + str(count))
        shutil.copy2(game1_winner_path, game1_winner_dest)
        score1, score2 = large_first(game1_scores["Team 1"][count-1], game1_scores["Team 2"][count-1])
        if score1 == None or score2 == None or (score1 == "0" and score2 == "0"):
            with open(game1_score_dest + "/Map " + str(count) + "/Map.txt", 'w') as file:
                file.write("")
        else:
            with open(game1_score_dest + "/Map " + str(count) + "/Map.txt", 'w') as file:
                file.write(score1 + " - " + score2)

    count = 0
    for winner in game2_winners:
        count += 1
        game1_winner_path = os.path.join(directory, winner + "/Map Win/Win.png")
        game1_winner_dest = os.path.join(game2_score_dest, "Map " + str(count))
        shutil.copy2(game1_winner_path, game1_winner_dest)        
        score1, score2 = large_first(game2_scores["Team 1"][count-1], game2_scores["Team 2"][count-1])       
        if score1 == None or score2 == None or (score1 == "0" and score2 == "0"):
            with open(game2_score_dest + "/Map " + str(count) + "/Map.txt", 'w') as file:
                file.write("")
        else:
            with open(game2_score_dest + "/Map " + str(count) + "/Map.txt", 'w') as file:
                file.write(score1 + " - " + score2)

def mapset_tab_load():
    pass

def mapset_tab_submit(game1maps, game2maps, gamemodes):

    maps = [game1maps,game2maps]
    mapsetpath = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Assets\Maps"

    modespath = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Assets\Modes\Options"
    modesdest = "C:\Dropbox\Teams\CRL\Alpha\Scene Switcher Directory\zz Assets zz\Assets\Modes\Active"

    game1dest = game1path + "\Map Set"
    game2dest = game2path + "\Map Set"


    for i in range(2):
        for j in range(5):

            modespathL = os.path.join(modespath + "\\" + gamemodes[j], "Mode.png")
            mapdestL = os.path.join(modesdest + "\Map " + str(j+1), "Mode.png")
            if os.path.isfile(modespathL):
                        # Copy the file to the destination
                        shutil.copy(modespathL, mapdestL)

            map_path = os.path.join(mapsetpath + "\\" + maps[i][j], "Map.png")
            map_dest = os.path.join(game1dest + "\Map " + str(j+1), "Map.png")

            if i == 0:
                map_path = os.path.join(mapsetpath + "\\" + maps[i][j], "Map.png")
                map_dest = os.path.join(game1dest + "\Map " + str(j+1), "Map.png")
                if os.path.isfile(map_path):
                            # Copy the file to the destination
                            shutil.copy(map_path, map_dest)
            elif i == 1:
                mappath = mapsetpath + maps[i][j]
                map_path = os.path.join(mapsetpath + "\\" + maps[i][j], "Map.png")
                map_dest = os.path.join(game2dest + "\Map " + str(j+1), "Map.png")
                if os.path.isfile(map_path):
                            # Copy the file to the destination
                            shutil.copy(map_path, map_dest)
            else:
                pass

def main_tab_button(week, day, g1t1_name, g1t1_score, g1t2_name, g1t2_score, g1_division, g2t1_name, g2t1_score, g2t2_name, g2t2_score, g2_division, l_caster, r_caster, season):
    directory = "C:/Dropbox/Teams/CRL/Alpha/Scene Switcher Directory/"
    divisions = "C:/Dropbox/Teams/CRL/Alpha/Scene Switcher Directory/zz Assets zz/Assets/TimeDivs/"
    scores = "C:/Dropbox/Teams/CRL/Alpha/Scene Switcher Directory/zz Assets zz/Assets/Scores/"
    weekdest_local = "C:/Dropbox/Teams/CRL/Alpha/Scene Switcher Directory/zz Assets zz/Assets/Week/Active"


    game1["Team 1"] = g1t1_name
    game1["Team 2"] = g1t2_name

    game2["Team 1"] = g2t1_name
    game2["Team 2"] = g2t2_name

    update_winner_options()


    team_paths = {
        g1t1_name + " (G1T1)": "zz Assets zz/Team 1/",
        g1t2_name + " (G1T2)": "zz Assets zz/Team 2/",
        g2t1_name + " (G2T1)": "zz Assets zz/Team 3/",
        g2t2_name + " (G2T2)": "zz Assets zz/Team 4/"
    }

    game_paths = {
        "Game 1": "zz Assets zz/Game 1/",
        "Game 2": "zz Assets zz/Game 2/"
    }

    team_scores = {
        "zz Assets zz/Team 1/": g1t1_score,
        "zz Assets zz/Team 2/": g1t2_score,
        "zz Assets zz/Team 3/": g2t1_score,
        "zz Assets zz/Team 4/": g2t2_score
    }

    with open(leftcasterpath, 'w') as file:
        file.write(l_caster)

    with open(rightcasterpath, 'w') as file:
        file.write(r_caster)

    with open(team1path + "\Score.txt", 'w') as file:
        file.write(g1t1_score)
    with open(team2path + "\Score.txt", 'w') as file:
        file.write(g1t2_score)
    with open(team3path + "\Score.txt", 'w') as file:
        file.write(g2t1_score)
    with open(team4path + "\Score.txt", 'w') as file:
        file.write(g2t2_score)
    
    
    week_path = os.path.join(weekpath + "\\" + week, "Week.png")
    week_dest = os.path.join(weekdest_local, "Week.png")
    if os.path.isfile(week_path):
                # Copy the file to the destination
                shutil.copy(week_path, week_dest)   

    for team_name, team_path_suffix in team_paths.items():
        source_path = os.path.join(directory, team_name[:-7])
        dest_path_team = os.path.join(directory, team_path_suffix)

        for file_name in os.listdir(source_path):
            if file_name.endswith(".png"):
                file_path = os.path.join(source_path, file_name)
                dest_file_path = os.path.join(dest_path_team, file_name)
                shutil.copy2(file_path, dest_file_path)

    for team_path, score in team_scores.items():
        source_path_score = None
        dest_path_score = os.path.join(directory, team_path)   

        if team_path == "zz Assets zz/Team 1/":

            source_path_score = os.path.join(scores, score)
        elif team_path == "zz Assets zz/Team 2/":
            source_path_score = os.path.join(scores, score)
        elif team_path == "zz Assets zz/Team 3/":
            source_path_score = os.path.join(scores, score)
        elif team_path == "zz Assets zz/Team 4/":
            source_path_score = os.path.join(scores, score)
        else:
            pass

        for file_name in os.listdir(source_path_score):
            if file_name.endswith(".png"):
                file_path = os.path.join(source_path_score, file_name)
                dest_file_path = os.path.join(dest_path_score , file_name)
                shutil.copy2(file_path, dest_file_path)


    for game_name, game_path_suffix in game_paths.items():
        source_path_div = None
        dest_path_div = None

        if game_name == "Game 1":
            source_path_div = os.path.join(divisions, "800/", g1_division)
            dest_path_div = os.path.join(directory, game_path_suffix)

        else:
            source_path_div = os.path.join(divisions, "930/", g2_division)
            dest_path_div = os.path.join(directory, game_path_suffix)              

        for file_name in os.listdir(source_path_div):
            if file_name.endswith(".png"):
                file_path = os.path.join(source_path_div, file_name)
                dest_file_path = os.path.join(dest_path_div , file_name)
                shutil.copy2(file_path, dest_file_path)

    #sample title CRL Vanguard: Fall W0  ll MIN Floppr vs CHI Hunted (Gold) ll NY Lightning vs DC Minutemen (Diamond) | !league !discord
    title = "CRL " + GAMENAME + ": " + season + " " + week + " ll " + abvs[g1t1_name] + " vs " + abvs[g1t2_name] + " (" + g1_division.split()[0] + ") ll " + abvs[g2t1_name] + " vs " + abvs[g2t2_name] + " (" + g2_division.split()[0] + ") | !league !discord"
    title_text.delete(0, tk.END)  # Clear the content of the Entry widget
    title_text.insert(tk.END, title)

    #sample com !editcom !mc Minnesota Floppr 0-0 Chicago Hunted (Gold Premade South)
    g1command = "!editcom !mc " + g1t1_name + " " + g1t1_score + "-" + g1t2_score + " " + g1t2_name + " (" + g1_division + ")"
    g1mapCount_text.delete(0, tk.END)
    g1mapCount_text.insert(tk.END, g1command)

    #sample com !editcom !mc Minnesota Floppr 0-0 Chicago Hunted (Gold Premade South)
    g2command = "!editcom !mc " + g2t1_name + " " + g2t1_score + "-" + g2t2_score + " " + g2t2_name + " (" + g2_division + ")"
    g2mapCount_text.delete(0, tk.END)
    g2mapCount_text.insert(tk.END, g2command)


root = tk.Tk()

root.config(bg="yellow")

ttk.Style().configure("Tab.TNotebook", background="yellow")
ttk.Style().configure("TabBG.TNotebook", background="grey")

# Set the minimum size of the window
root.minsize(725, 740)

# Make the window unscalable
root.resizable(width=False, height=False)



notebook = ttk.Notebook(root, style="TabBG.TNotebook")


# Create the first tab
tab1 = ttk.Frame(notebook)

week_label = tk.Label(tab1, text="Week")
# Create the drop-down menu
week_menu = AutocompleteCombobox(tab1, weeks)
week_menu.set(weeks[-1])


day_label = tk.Label(tab1, text="Match Day")
# Create the drop-down menu
day_menu = AutocompleteCombobox(tab1)
day_menu.config(values=days)
day_menu.set(days[-1])

season_label = tk.Label(tab1, text="Season")
season_menu = AutocompleteCombobox(tab1)
season_menu.config(values=seasons)
season_menu.set(seasons[-1])

game1_label = tk.Label(tab1, text="Game 1")

game1_division_label = tk.Label(tab1, text="Division")
# Create the drop-down menu
game1_division_menu = AutocompleteCombobox(tab1, divisions)
game1_division_menu.set(divisions[-1])

# Create the drop-down menu
g1t1_name_menu = AutocompleteCombobox(tab1, teams)
g1t1_name_menu.set(teams[-1])


# Create the drop-down menu
g1t2_name_menu = AutocompleteCombobox(tab1, teams)
g1t2_name_menu.set(teams[-1])

# Create the drop-down menu
score_g1t1_menu = AutocompleteCombobox(tab1, ["0", "1", "2", "3"])
score_g1t1_menu.set("0")

# Create the drop-down menu
score_g1t2_menu = AutocompleteCombobox(tab1, ["0", "1", "2", "3"])
score_g1t2_menu.set("0")

# Create the drop-down menu
score_g2t1_menu = AutocompleteCombobox(tab1, ["0", "1", "2", "3"])
score_g2t1_menu.set("0")

# Create the drop-down menu
score_g2t2_menu = AutocompleteCombobox(tab1, ["0", "1", "2", "3"])
score_g2t2_menu.set("0")

left_caster_name = tk.Entry(tab1)
right_caster_name = tk.Entry(tab1)


g1t1_label = tk.Label(tab1, text="Team 1")
g1t2_label = tk.Label(tab1, text="Team 2")

game2_label = tk.Label(tab1, text="Game 2")
game2_division_label = tk.Label(tab1, text="Division")

# Create the drop-down menu
game2_division_menu = AutocompleteCombobox(tab1, divisions)
game2_division_menu.set(divisions[-1])

# Create the drop-down menu
g2t1_name_menu = AutocompleteCombobox(tab1, teams)
g2t1_name_menu.set(teams[-1])

# Create the drop-down menu
g2t2_name_menu = AutocompleteCombobox(tab1, teams)
g2t2_name_menu.set(teams[-1])

g2t1_label = tk.Label(tab1, text="Team 1")
g2t2_label = tk.Label(tab1, text="Team 2")

left_caster_label = tk.Label(tab1, text="Left Caster")
right_caster_label = tk.Label(tab1, text="Right Caster")

title_label = tk.Label(tab1, text="Title:")
title_text = tk.Entry(tab1)
g1mapCount_label = tk.Label(tab1, text="Map Count Game 1:")
g1mapCount_text = tk.Entry(tab1)
g2mapCount_label = tk.Label(tab1, text="Map Count Game 2:")
g2mapCount_text = tk.Entry(tab1)

button = tk.Button(tab1, text="Submit", command=lambda: main_tab_button(week_menu.get(),day_menu.get(),g1t1_name_menu.get(),score_g1t1_menu.get(),g1t2_name_menu.get(),score_g1t2_menu.get(),game1_division_menu.get(),g2t1_name_menu.get(),score_g2t1_menu.get(),g2t2_name_menu.get(),score_g2t2_menu.get(),game2_division_menu.get(), left_caster_name.get(), right_caster_name.get(), season_menu.get()))

week_label.grid(row=0, column=0)
week_menu.grid(row=0, column=1)

day_label.grid(row=1, column=0)
day_menu.grid(row=1, column=1)

season_label.grid(row=2, column=0)
season_menu.grid(row=2, column=1)

game1_label.grid(row=3, column=0)

game1_division_label.grid(row=4, column=1)
game1_division_menu.grid(row=4, column=2)

g1t1_label.grid(row=5, column=1)
g1t1_name_menu.grid(row=5, column=2)
score_g1t1_menu.grid(row=5, column=3) 

g1t2_label.grid(row=6, column=1)
g1t2_name_menu.grid(row=6, column=2) 
score_g1t2_menu.grid(row=6, column=3)


game2_label.grid(row=7, column=0)

game2_division_label.grid(row=8, column=1)
game2_division_menu.grid(row=8, column=2)

g2t1_label.grid(row=9, column=1)
g2t1_name_menu.grid(row=9, column=2)
score_g2t1_menu.grid(row=9, column=3) 

g2t2_label.grid(row=10, column=1)
g2t2_name_menu.grid(row=10, column=2) 
score_g2t2_menu.grid(row=10, column=3) 

left_caster_label.grid(row=11,column=0)
left_caster_name.grid(row=11, column=1)
right_caster_label.grid(row=11, column=2)
right_caster_name.grid(row=11, column=3)
title_label.grid(row=12, column=0)
title_text.grid(row=13, column=0, sticky="ew", columnspan=4)
g1mapCount_label.grid(row=14,column=0)
g1mapCount_text.grid(row=15, column=0, sticky="ew", columnspan=4)
g2mapCount_label.grid(row=16,column=0)
g2mapCount_text.grid(row=17, column=0, sticky="ew", columnspan=4)
button.grid(row=18, column= 0)

notebook.add(tab1, text="Main")

# Create the second tab
tab2 = ttk.Frame(notebook)
mapset_game1_label = tk.Label(tab2, text="Game 1")
mapset_game2_label = tk.Label(tab2, text="Game 2")

mapset_game1_maplabel1 = tk.Label(tab2, text="Map 1")
mapset_game1_maplabel2 = tk.Label(tab2, text="Map 2")
mapset_game1_maplabel3 = tk.Label(tab2, text="Map 3")
mapset_game1_maplabel4 = tk.Label(tab2, text="Map 4")
mapset_game1_maplabel5 = tk.Label(tab2, text="Map 5")

mapset_game2_maplabel1 = tk.Label(tab2, text="Map 1")
mapset_game2_maplabel2 = tk.Label(tab2, text="Map 2")
mapset_game2_maplabel3 = tk.Label(tab2, text="Map 3")
mapset_game2_maplabel4 = tk.Label(tab2, text="Map 4")
mapset_game2_maplabel5 = tk.Label(tab2, text="Map 5")


mapset_game1_map1 = AutocompleteCombobox(tab2, maps)
mapset_game1_map1.set(maps[-1])

mapset_game1_map2 = AutocompleteCombobox(tab2, maps)
mapset_game1_map2.set(maps[-1])

mapset_game1_map3 = AutocompleteCombobox(tab2, maps)
mapset_game1_map3.set(maps[-1])

mapset_game1_map4 = AutocompleteCombobox(tab2, maps)
mapset_game1_map4.set(maps[-1])

mapset_game1_map5 = AutocompleteCombobox(tab2, maps)
mapset_game1_map5.set(maps[-1])


mapset_game2_map1 = AutocompleteCombobox(tab2, maps)
mapset_game2_map1.set(maps[-1])

mapset_game2_map2 = AutocompleteCombobox(tab2, maps)
mapset_game2_map2.set(maps[-1])

mapset_game2_map3 = AutocompleteCombobox(tab2, maps)
mapset_game2_map3.set(maps[-1])

mapset_game2_map4 = AutocompleteCombobox(tab2, maps)
mapset_game2_map4.set(maps[-1])

mapset_game2_map5 = AutocompleteCombobox(tab2, maps)
mapset_game2_map5.set(maps[-1])

gamemodes_label = tk.Label(tab2, text="Gamemodes")

gamemode_map1 = AutocompleteCombobox(tab2, gamemodes)
gamemode_map1.set(gamemodes[3])

gamemode_map2 = AutocompleteCombobox(tab2, gamemodes)
gamemode_map2.set(gamemodes[6])

gamemode_map3 = AutocompleteCombobox(tab2, gamemodes)
gamemode_map3.set(gamemodes[0])

gamemode_map4 = AutocompleteCombobox(tab2, gamemodes)
gamemode_map4.set(gamemodes[3])

gamemode_map5 = AutocompleteCombobox(tab2, gamemodes)
gamemode_map5.set(gamemodes[6])



mapset_submit_button = tk.Button(tab2, text="Submit", command=lambda: mapset_tab_submit([mapset_game1_map1.get(),mapset_game1_map2.get(),mapset_game1_map3.get(),mapset_game1_map4.get(),mapset_game1_map5.get()],
                                                                                        [mapset_game2_map1.get(),mapset_game2_map2.get(),mapset_game2_map3.get(),mapset_game2_map4.get(),mapset_game2_map5.get()],
                                                                                        [gamemode_map1.get(),gamemode_map2.get(),gamemode_map3.get(),gamemode_map4.get(),gamemode_map5.get()]))
mapset_load_button = tk.Button(tab2, text="Load", command=lambda: mapset_tab_load())


mapset_game1_label.grid(row=0,column=0)

mapset_game1_maplabel1.grid(row=1,column=0)
mapset_game1_maplabel2.grid(row=1,column=1)
mapset_game1_maplabel3.grid(row=1,column=2)
mapset_game1_maplabel4.grid(row=1,column=3)
mapset_game1_maplabel5.grid(row=1,column=4)

mapset_game1_map1.grid(row=2,column=0)
mapset_game1_map2.grid(row=2,column=1)
mapset_game1_map3.grid(row=2,column=2)
mapset_game1_map4.grid(row=2,column=3)
mapset_game1_map5.grid(row=2,column=4)

mapset_game2_label.grid(row=3,column=0)

mapset_game2_maplabel1.grid(row=4,column=0)
mapset_game2_maplabel2.grid(row=4,column=1)
mapset_game2_maplabel3.grid(row=4,column=2)
mapset_game2_maplabel4.grid(row=4,column=3)
mapset_game2_maplabel5.grid(row=4,column=4)

mapset_game2_map1.grid(row=5,column=0)
mapset_game2_map2.grid(row=5,column=1)
mapset_game2_map3.grid(row=5,column=2)
mapset_game2_map4.grid(row=5,column=3)
mapset_game2_map5.grid(row=5,column=4)

gamemodes_label.grid(row=6, column=0)

gamemode_map1.grid(row=7, column=0)
gamemode_map2.grid(row=7, column=1)
gamemode_map3.grid(row=7, column=2)
gamemode_map4.grid(row=7, column=3)
gamemode_map5.grid(row=7, column=4)

mapset_load_button.grid(row=8, column=0)
mapset_submit_button.grid(row=8, column=1)


notebook.add(tab2, text="Map Set")

# Create the third tab =================================================================================================================================================================================================
tab3 = ttk.Frame(notebook)

game1_team_list = teams
game2_team_list = teams

score_game1_label = tk.Label(tab3, text="Game 1")

score_game2_label = tk.Label(tab3, text="Game 2")

score_game1_maplabel1 = tk.Label(tab3, text="Map 1")
score_game1_maplabel2 = tk.Label(tab3, text="Map 2")
score_game1_maplabel3 = tk.Label(tab3, text="Map 3")
score_game1_maplabel4 = tk.Label(tab3, text="Map 4")
score_game1_maplabel5 = tk.Label(tab3, text="Map 5")

score_game2_maplabel1 = tk.Label(tab3, text="Map 1")
score_game2_maplabel2 = tk.Label(tab3, text="Map 2")
score_game2_maplabel3 = tk.Label(tab3, text="Map 3")
score_game2_maplabel4 = tk.Label(tab3, text="Map 4")
score_game2_maplabel5 = tk.Label(tab3, text="Map 5")



score_game1_map1_t1 = tk.Entry(tab3)
score_game1_map1_t1.insert(0, "0")
score_game1_map1_t2 = tk.Entry(tab3)
score_game1_map1_t2.insert(0, "0")
score_game1_map1_winner = AutocompleteCombobox(tab3, game1_team_list)
score_game1_map1_winner.set(teams[-1])
checkbox_game1_map1_t1 = tk.Checkbutton(tab3, command=lambda: checkbox_winner(1,1,score_game1_map1_t1))

score_game1_map2_t1 = tk.Entry(tab3)
score_game1_map2_t1.insert(0, "0")
score_game1_map2_t2 = tk.Entry(tab3)
score_game1_map2_t2.insert(0, "0")
score_game1_map2_winner = AutocompleteCombobox(tab3, game1_team_list)
score_game1_map2_winner.set(teams[-1])
checkbox_game1_map2_t1 = tk.Checkbutton(tab3, command=lambda: checkbox_winner(1,2,score_game1_map2_t1))

score_game1_map3_t1 = tk.Entry(tab3)
score_game1_map3_t1.insert(0, "0")
score_game1_map3_t2 = tk.Entry(tab3)
score_game1_map3_t2.insert(0, "0")
score_game1_map3_winner = AutocompleteCombobox(tab3, game1_team_list)
score_game1_map3_winner.set(teams[-1])
checkbox_game1_map3_t1 = tk.Checkbutton(tab3, command=lambda: checkbox_winner(1,3,score_game1_map3_t1))

score_game1_map4_t1 = tk.Entry(tab3)
score_game1_map4_t1.insert(0, "0")
score_game1_map4_t2 = tk.Entry(tab3)
score_game1_map4_t2.insert(0, "0")
score_game1_map4_winner = AutocompleteCombobox(tab3, game1_team_list)
score_game1_map4_winner.set(teams[-1])
checkbox_game1_map4_t1 = tk.Checkbutton(tab3, command=lambda: checkbox_winner(1,4,score_game1_map4_t1))

score_game1_map5_t1 = tk.Entry(tab3)
score_game1_map5_t1.insert(0, "0")
score_game1_map5_t2 = tk.Entry(tab3)
score_game1_map5_t2.insert(0, "0")
score_game1_map5_winner = AutocompleteCombobox(tab3, game1_team_list)
score_game1_map5_winner.set(teams[-1])
checkbox_game1_map5_t1 = tk.Checkbutton(tab3, command=lambda: checkbox_winner(1,5,score_game1_map5_t1))

#=============================================================
score_game2_map1_t1 = tk.Entry(tab3)
score_game2_map1_t1.insert(0, "0")
score_game2_map1_t2 = tk.Entry(tab3)
score_game2_map1_t2.insert(0, "0")
score_game2_map1_winner = AutocompleteCombobox(tab3, game2_team_list)
score_game2_map1_winner.set(teams[-1])
checkbox_game2_map1_t1 = tk.Checkbutton(tab3, command=lambda: checkbox_winner(2,1,score_game2_map1_t1))

score_game2_map2_t1 = tk.Entry(tab3)
score_game2_map2_t1.insert(0, "0")
score_game2_map2_t2 = tk.Entry(tab3)
score_game2_map2_t2.insert(0, "0")
score_game2_map2_winner = AutocompleteCombobox(tab3, game2_team_list)
score_game2_map2_winner.set(teams[-1])
checkbox_game2_map2_t1 = tk.Checkbutton(tab3, command=lambda: checkbox_winner(2,2,score_game2_map2_t1))

score_game2_map3_t1 = tk.Entry(tab3)
score_game2_map3_t1.insert(0, "0")
score_game2_map3_t2 = tk.Entry(tab3)
score_game2_map3_t2.insert(0, "0")
score_game2_map3_winner = AutocompleteCombobox(tab3, game2_team_list)
score_game2_map3_winner.set(teams[-1])
checkbox_game2_map3_t1 = tk.Checkbutton(tab3, command=lambda: checkbox_winner(2,3,score_game2_map3_t1))

score_game2_map4_t1 = tk.Entry(tab3)
score_game2_map4_t1.insert(0, "0")
score_game2_map4_t2 = tk.Entry(tab3)
score_game2_map4_t2.insert(0, "0")
score_game2_map4_winner = AutocompleteCombobox(tab3, game2_team_list)
score_game2_map4_winner.set(teams[-1])
checkbox_game2_map4_t1 = tk.Checkbutton(tab3, command=lambda: checkbox_winner(2,4,score_game2_map4_t1))

score_game2_map5_t1 = tk.Entry(tab3)
score_game2_map5_t1.insert(0, "0")
score_game2_map5_t2 = tk.Entry(tab3)
score_game2_map5_t2.insert(0, "0")
score_game2_map5_winner = AutocompleteCombobox(tab3, game2_team_list)
score_game2_map5_winner.set(teams[-1])
checkbox_game2_map5_t1 = tk.Checkbutton(tab3, command=lambda: checkbox_winner(2,5,score_game2_map5_t1))
#=============================================================

def checkbox_winner(game, map_num, widget):
    if map_num == 1:
        if game == 1 or game == 2:
            widget.delete(0, tk.END)
            widget.insert(0, "250")
    elif map_num == 2:
        if game == 1 or game == 2:
            widget.delete(0, tk.END)
            widget.insert(0, "6")
    elif map_num == 3:
        if game == 1 or game == 2:
            widget.delete(0, tk.END)
            widget.insert(0, "3")
    elif map_num == 4:
        if game == 1 or game == 2:
            widget.delete(0, tk.END)
            widget.insert(0, "250")
    else:
        if game == 1 or game == 2:
            widget.delete(0, tk.END)
            widget.insert(0, "6")


def update_winner_options():
    game1_team_list = []
    game2_team_list = []

    if game1["Team 1"] != "" and game1["Team 2"] != "":
        game1_team_list.append(game1["Team 1"])
        game1_team_list.append(game1["Team 2"])
    else:
        game1_team_list = teams

    if game2["Team 1"] != "" and game2["Team 2"] != "":
        game2_team_list.append(game2["Team 1"])
        game2_team_list.append(game2["Team 2"])
    else:
        game2_team_list = teams

    # Update the options of the score_game1_map1_winner AutocompleteCombobox
    score_game1_map1_winner.set_completion_list(game1_team_list)
    score_game1_map2_winner.set_completion_list(game1_team_list)
    score_game1_map3_winner.set_completion_list(game1_team_list)
    score_game1_map4_winner.set_completion_list(game1_team_list)
    score_game1_map5_winner.set_completion_list(game1_team_list)

    score_game2_map1_winner.set_completion_list(game2_team_list)
    score_game2_map2_winner.set_completion_list(game2_team_list)
    score_game2_map3_winner.set_completion_list(game2_team_list)
    score_game2_map4_winner.set_completion_list(game2_team_list)
    score_game2_map5_winner.set_completion_list(game2_team_list)



score_submit_button = tk.Button(tab3, text="Submit", command=lambda: score_tab_submit({"Team 1": [score_game1_map1_t1.get(), score_game1_map2_t1.get(), score_game1_map3_t1.get(), score_game1_map4_t1.get(), score_game1_map5_t1.get()], "Team 2": [score_game1_map1_t2.get(), score_game1_map2_t2.get(), score_game1_map3_t2.get(), score_game1_map4_t2.get(), score_game1_map5_t2.get()]},
                                                                                    {"Team 1": [score_game2_map1_t1.get(), score_game2_map2_t1.get(), score_game2_map3_t1.get(), score_game2_map4_t1.get(), score_game2_map5_t1.get()], "Team 2": [score_game2_map1_t2.get(), score_game2_map2_t2.get(), score_game2_map3_t2.get(), score_game2_map4_t2.get(), score_game2_map5_t2.get()]},
                                                                                    [score_game1_map1_winner.get(), score_game1_map2_winner.get(), score_game1_map3_winner.get(), score_game1_map4_winner.get(), score_game1_map5_winner.get()],
                                                                                    [score_game2_map1_winner.get(), score_game2_map2_winner.get(), score_game2_map3_winner.get(), score_game2_map4_winner.get(), score_game2_map5_winner.get()]))


score_game1_label.grid(row=1,column=0)

checkbox_game1_map1_t1.grid(row=2,column=0)
score_game1_map1_t1.grid(row=2, column=1)
score_game1_map1_t2.grid(row=2, column=2)
score_game1_map1_winner.grid(row=2, column=4)

checkbox_game1_map2_t1.grid(row=3,column=0)
score_game1_map2_t1.grid(row=3, column=1)
score_game1_map2_t2.grid(row=3, column=2)
score_game1_map2_winner.grid(row=3, column=4)

checkbox_game1_map3_t1.grid(row=4,column=0)
score_game1_map3_t1.grid(row=4, column=1)
score_game1_map3_t2.grid(row=4, column=2)
score_game1_map3_winner.grid(row=4, column=4)

checkbox_game1_map4_t1.grid(row=5,column=0)
score_game1_map4_t1.grid(row=5, column=1)
score_game1_map4_t2.grid(row=5, column=2)
score_game1_map4_winner.grid(row=5, column=4)

checkbox_game1_map5_t1.grid(row=6,column=0)
score_game1_map5_t1.grid(row=6, column=1)
score_game1_map5_t2.grid(row=6, column=2)
score_game1_map5_winner.grid(row=6, column=4)

score_game2_label.grid(row=7,column=0)

checkbox_game2_map1_t1.grid(row=10,column=0)
score_game2_map1_t1.grid(row=10, column=1)
score_game2_map1_t2.grid(row=10, column=2)
score_game2_map1_winner.grid(row=10, column=4)

checkbox_game2_map2_t1.grid(row=11,column=0)
score_game2_map2_t1.grid(row=11, column=1)
score_game2_map2_t2.grid(row=11, column=2)
score_game2_map2_winner.grid(row=11, column=4)

checkbox_game2_map3_t1.grid(row=12,column=0)
score_game2_map3_t1.grid(row=12, column=1)
score_game2_map3_t2.grid(row=12, column=2)
score_game2_map3_winner.grid(row=12, column=4)

checkbox_game2_map4_t1.grid(row=13,column=0)
score_game2_map4_t1.grid(row=13, column=1)
score_game2_map4_t2.grid(row=13, column=2)
score_game2_map4_winner.grid(row=13, column=4)

checkbox_game2_map5_t1.grid(row=14,column=0)
score_game2_map5_t1.grid(row=14, column=1)
score_game2_map5_t2.grid(row=14, column=2)
score_game2_map5_winner.grid(row=14, column=4)

score_submit_button.grid(row=15,column=0)

notebook.add(tab3, text="Score Report")

# # Create the fourth tab
# tab4 = ttk.Frame(notebook)
# label4 = tk.Label(tab4, text="Schedule")
# entry4 = tk.Entry(tab4)
# label4.pack()
# entry4.pack()
# notebook.add(tab4, text="Schedule")

notebook.pack(expand=True, fill="both")

root.wm_title("Scene Switcher")
# Load the image file
image = tk.PhotoImage(file="sceneswitchericon.png")

# Set the window icon
root.iconphoto(True, image)

root.mainloop()