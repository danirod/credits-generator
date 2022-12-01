#!/usr/bin/env python3

import csv
import glob

def processes(dir):
  def outer_wrapper(func):
    def wrapper():
      full = set()
      for file in glob.glob(dir):
        data = csv.DictReader(open(file).readlines())
        users = func(data)
        full = full.union(users)
      clear = list(full)
      clear.sort()
      return clear
    return wrapper
  return outer_wrapper

@processes('youtube/*.csv')
def dump_youtube(data):
  return [x['Miembro'] for x in data]

@processes('twitch/*.csv')
def dump_twitch_subscribers(data):
  return [x['Username'] for x in data if x['Sub Type'] in ['prime','recurring'] and x['Username'] != 'danirod_']

@processes('gift/*.csv')
def dump_gifters(data):
  # this data is parsed manually from the streamlabs feed
  return [x['Member'] for x in data]

@processes('twitch/*.csv')
def dump_twitch_gifts(data):
  return [x['Username'] for x in data if x['Sub Type'] == 'gift']

def print_single_column(names):
  print()
  for name in names:
    print(f" {name}")
  print()

def print_double_column(names):
  print()
  if len(names) % 2 != 0:
    names = names + [""]
  for i in range(len(names) // 2):
    left, right = names[i*2], names[i*2+1]
    print(f" {left:<25} {right}")
  print()

#      12345678901234567890123456789012345678901234567890
print("MUCHAS GRACIAS A LOS MIEMBROS Y SUSCRIPTORES")
print("POR AYUDARME A CREAR ESTE TIPO DE CONTENIDOS")
print()
print("MIEMBROS DE YOUTUBE")
print_single_column(dump_youtube())
print("SUSCRIPTORES DE TWITCH")
print_double_column(dump_twitch_subscribers())
print("Y A LA GENTE QUE REGALA SUSCRIPCIONES:")
print_double_column(dump_gifters())
print("ESTE MES HAN SIDO INVITADOS:")
print_double_column(dump_twitch_gifts())