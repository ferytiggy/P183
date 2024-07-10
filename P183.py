# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:04:42 2024

@author: Aidan
"""

from tkinter import *
import requests
import json

root=Tk()
root.title("P183")
root.geometry("450x450")
root.configure(background="white")

city_name_label = Label(root, text="Nombre de la capital")
city_name_label.place(relx=0.15, rely=0.1, anchor=CENTER)
city_entry = Entry(root)
city_entry.place(relx=0.15, rely=0.2, anchor=CENTER)
country_name = Label(root, text="País:")
country_name.place(relx=0.15, rely=0.4, anchor=CENTER)
country_region = Label(root, text="Región=")
country_region.place(relx=0.15, rely=0.5, anchor=CENTER)
country_language = Label(root, text="Idioma=")
country_language.place(relx=0.15, rely=0.6, anchor=CENTER)
country_population = Label(root, text="Población=")
country_population.place(relx=0.15, rely=0.7, anchor=CENTER)
country_land = Label(root, text="Area=")
country_land.place(relx=0.15, rely=0.8, anchor=CENTER)

def city_details():
    api_request = requests.get("https://restcountries.eu/rest/v2/capital/" + city_entry.get())
    api_output_json = json.loads(api_request.content)
    nombre = api_output_json[0]["name"]
    region = api_output_json[0]["region"]
    idioma = api_ouput_json[0]["language"]
    poblacion = api_output_json[0]["population"]
    area = api_output_json[0]["country_area"]
    
    country_name["text"] = "Nombre:" + nombre
    country_region["text"] = "Región:" + region
    country_language["text"] = "Idioma:" + idioma
    country_population["text"] = "Población:" + poblacion
    country_land["text"] = "Area:" + area
    
Boton = Button(root, text="Detalles del país", command=city_details)
Boton.place(relx=0.15, rely=0.3, anchor=CENTER)

root.mainloop()
    
