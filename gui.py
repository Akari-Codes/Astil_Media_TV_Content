import tvmedia_controller as controller
import os
from string import digits
import wget
import requests as req
from pathlib import Path
import pickle
import json
import webview
import time
def get_gui(data):
    with open(Path(os.getcwd() + "/web/" + data + ".html"), 'r') as data_html:
        html = data_html.read()
    return html
global media
media = []
global media_type
media_type = ""
global media_name
media_name = []
def process_media(id,name,window):
    y = 0
    window.load_html("<p>Processing Media...</p>")
    for x in media:
        name = media_name[y]
        id = x
        controller.addmedia(media_type, window, name, id)
        y = y + 1
    window.load_html("<p>Processing Media Complete!</p>")
    time.sleep(2)
    window.load_html(get_gui("start"))
class Api:
    def media_list(self,mode,id="",name=""):
        if mode == "add_media":
            media.append(id)
            media_name.append(name)
        elif mode == "process_media":
            process_media(id,name,window)
    def exit(self):
        window.hide()
        window.destroy()
        quit()
    def media_page(self):
        media_type = window.dom.get_element("#media_type").value
        window.load_html(get_gui("media_add"))
        window.dom.get_element("#mt_title").text = "Add " + media_type.replace("_", " ") + " Media"
if __name__ == "__main__":
    html = get_gui("start")
    api = Api()
    window = webview.create_window("TV Content", html=html, js_api=api)
    webview.start(debug=True)