import os
from string import digits
import wget
import requests as req
from pathlib import Path
import pickle
import json
def addmedia(media_type, id, window, name):
    def cata():
        classnamealt = id
        remove_digits = str.maketrans('', '', digits)
        classname = classnamealt.translate(remove_digits)
        url = "http://143.47.248.77/web/#/details?id=" + id + "&serverId=5ffad972b3e34394a756f1ec62428de1"
        backurl = "http://143.47.248.77/Items/" + id + "/Images/Primary"
        output_file = os.getcwd() + "\\posters\\anime\\" + id + ".jpg"
        output_path = os.getcwd() + "\\posters\\anime\\"
        try:
            Path(output_path).mkdir()
        except:
            print("Skipping Folder Creation Folder Already Exists")
        try:
            Path(output_file).touch()
            data = req.get(backurl)
            with open(output_file, 'wb')as file:
                file.write(data.content)
            poster = "'\\\\posters\\\\anime\\\\" + id + ".jpg'"
        except:
            print("Skipping File Creation File Already Exists")
        with open(os.getcwd() + "\\animecount.conf", 'r') as ac:
            count = ac.read()
        count = count
        print(count)
        newcount = int(count) + 1
        with open(os.getcwd() + "\\animecount.conf", 'w') as ac:
            ac.write(str(newcount))
        with open(os.getcwd() + "\\animecount.conf", 'r') as acs:
            animecounts = acs.read()
        with open(os.getcwd() + "\\animemcount.conf", 'r') as amcs:
            animemcounts = amcs.read()
        with open(os.getcwd() + "\\tvscount.conf", 'r') as tvscs:
            tvshowcounts = tvscs.read()
        tabscount = """
function getanimecount() {var animecount = '""" + animecounts + """';return animecount;};
function getamcount() {var amcount = '""" + animemcounts + """';return amcount;};
function gettvscount() {var tvscount = '""" + tvshowcounts + """';return tvscount;};       
"""
        with open(os.getcwd() + "\\morejs.js", 'w') as mjs:
            mjs.write(tabscount)
        maintemplate = """
        <div class='""" + classname + """ lr ' id='anime""" + str(newcount) + """'>
        <a href='""" + url + """'>
        <p>""" + name + """<br><font size="1"></font></p>
        </a>
        </div>"""
        subtemplate = """
        .""" + classname + """{
        background: linear-gradient(rgba(0, 0, 0, 0),rgba(0, 0, 0, 0.09)),url(""" + poster + """);
        background-size: cover;
        width: 194px;
        height: 300px;
        position: relative;
        float: left;
        max-width: 200px;
        padding:6px;}"""
        with open(os.getcwd() + "\\anime.html", 'r') as animehtml:
            animehtml_read = animehtml.read()
        with open(os.getcwd() + "\\anime.html", 'w') as animehtml:
            maintemplate = maintemplate + animehtml_read
            print(maintemplate)
            animehtml.write(maintemplate)
        with open(os.getcwd() + "\\media.css", 'a') as mediacss:
            mediacss.write(subtemplate)
    def catam():
        classnamealt = id
        remove_digits = str.maketrans('', '', digits)
        classname = classnamealt.translate(remove_digits)
        url = "http://143.47.248.77/web/#/details?id=" + id + "&serverId=5ffad972b3e34394a756f1ec62428de1"
        backurl = "http://143.47.248.77/Items/" + id + "/Images/Primary"
        output_file = os.getcwd() + "\\posters\\animemovie\\" + id + ".jpg"
        output_path = os.getcwd() + "\\posters\\animemovie\\"
        try:
            Path(output_path).mkdir()
        except:
            print("Skipping Folder Creation Folder Already Exists")
        try:
            Path(output_file).touch()
            data = req.get(backurl)
            with open(output_file, 'wb')as file:
                file.write(data.content)
            poster = "'\\\\posters\\\\animemovie\\\\" + id + ".jpg'"
        except:
            print("Skipping File Creation File Already Exists")
        with open(os.getcwd() + "\\animemcount.conf", 'r') as ac:
            count = ac.read()
        count = count
        print(count)
        newcount = int(count) + 1
        with open(os.getcwd() + "\\animemcount.conf", 'w') as ac:
            ac.write(str(newcount))
        with open(os.getcwd() + "\\animecount.conf", 'r') as acs:
            animecounts = acs.read()
        with open(os.getcwd() + "\\animemcount.conf", 'r') as amcs:
            animemcounts = amcs.read()
        with open(os.getcwd() + "\\tvscount.conf", 'r') as tvscs:
            tvshowcounts = tvscs.read()
        tabscount = """
function getanimecount() {var animecount = '""" + animecounts + """';return animecount;};
function getamcount() {var amcount = '""" + animemcounts + """';return amcount;};
function gettvscount() {var tvscount = '""" + tvshowcounts + """';return tvscount;};       
"""
        with open(os.getcwd() + "\\morejs.js", 'w') as mjs:
            mjs.write(tabscount)
        maintemplate = """
        <div class='""" + classname + """ lr ' id='anime""" + str(newcount) + """'>
        <a href='""" + url + """'>
        <p>""" + name + """<br><font size="1"></font></p>
        </a>
        </div>"""
        subtemplate = """
        .""" + classname + """{
        background: linear-gradient(rgba(0, 0, 0, 0),rgba(0, 0, 0, 0.09)),url(""" + poster + """);
        background-size: cover;
        width: 194px;
        height: 300px;
        position: relative;
        float: left;
        max-width: 200px;
        padding:6px;}"""
        with open(os.getcwd() + "\\animemovies.html", 'r') as animehtml:
            animehtml_read = animehtml.read()
        with open(os.getcwd() + "\\animemovies.html", 'w') as animehtml:
            maintemplate = maintemplate + animehtml_read
            print(maintemplate)
            animehtml.write(maintemplate)
        with open(os.getcwd() + "\\media.css", 'a') as mediacss:
            mediacss.write(subtemplate)
    def cattvs():
        classnamealt = id
        remove_digits = str.maketrans('', '', digits)
        classname = classnamealt.translate(remove_digits)
        url = "http://143.47.248.77/web/#/details?id=" + id + "&serverId=5ffad972b3e34394a756f1ec62428de1"
        backurl = "http://143.47.248.77/Items/" + id + "/Images/Primary"
        output_file = os.getcwd() + "\\posters\\tvshow\\" + id + ".jpg"
        output_path = os.getcwd() + "\\posters\\tvshow\\"
        try:
            Path(output_path).mkdir()
        except:
            print("Skipping Folder Creation Folder Already Exists")
        try:
            Path(output_file).touch()
            data = req.get(backurl)
            with open(output_file, 'wb')as file:
                file.write(data.content)
            poster = "'\\\\posters\\\\tvshow\\\\" + id + ".jpg'"
        except:
            print("Skipping File Creation File Already Exists")
        with open(os.getcwd() + "\\tvscount.conf", 'r') as ac:
            count = ac.read()
        count = count
        print(count)
        newcount = int(count) + 1
        with open(os.getcwd() + "\\tvscount.conf", 'w') as ac:
            ac.write(str(newcount))
        with open(os.getcwd() + "\\animecount.conf", 'r') as acs:
            animecounts = acs.read()
        with open(os.getcwd() + "\\animemcount.conf", 'r') as amcs:
            animemcounts = amcs.read()
        with open(os.getcwd() + "\\tvscount.conf", 'r') as tvscs:
            tvshowcounts = tvscs.read()
        tabscount = """
function getanimecount() {var animecount = '""" + animecounts + """';return animecount;};
function getamcount() {var amcount = '""" + animemcounts + """';return amcount;};
function gettvscount() {var tvscount = '""" + tvshowcounts + """';return tvscount;};       
"""
        with open(os.getcwd() + "\\morejs.js", 'w') as mjs:
            mjs.write(tabscount)
        maintemplate = """
        <div class='""" + classname + """ lr ' id='anime""" + str(newcount) + """'>
        <a href='""" + url + """'>
        <p>""" + name + """<br><font size="1"></font></p>
        </a>
        </div>"""
        subtemplate = """
        .""" + classname + """{
        background: linear-gradient(rgba(0, 0, 0, 0),rgba(0, 0, 0, 0.09)),url(""" + poster + """);
        background-size: cover;
        width: 194px;
        height: 300px;
        position: relative;
        float: left;
        max-width: 200px;
        padding:6px;}"""
        with open(os.getcwd() + "\\tvshows.html", 'r') as animehtml:
            animehtml_read = animehtml.read()
        with open(os.getcwd() + "\\tvshows.html", 'w') as animehtml:
            maintemplate = maintemplate + animehtml_read
            print(maintemplate)
            animehtml.write(maintemplate)
        with open(os.getcwd() + "\\media.css", 'a') as mediacss:
            mediacss.write(subtemplate)
    cat = media_type
    if cat == "Anime":
        cata()    
    elif cat == "Anime_Movies":
        catam()
    elif cat == "TV_Shows":
        cattvs()
    else:
        addmedia(media_type, id, window, name)
    return