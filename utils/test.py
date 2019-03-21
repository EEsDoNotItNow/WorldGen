#!/usr/bin/env python3

from src.character import spawner, char_base
import json

print("hello world!")

with open("data/mideval.json","r") as fp:
    demo_data = json.load(fp)

r = 0.0
for prof in demo_data['professions']:
    r += 1/demo_data['professions'][prof]['sv']

# Counting back down from 100%, we calculate rolls for each entry
r2 = 1.0
for prof in demo_data['professions']:
    # print(prof, 1/demo_data['professions'][prof]['sv']/r)
    demo_data['professions'][prof]['roll'] = r2 - 1/demo_data['professions'][prof]['sv']/r
    r2 -= 1/demo_data['professions'][prof]['sv']/r

# print(demo_data)

s = spawner(demographics=demo_data)

for x in s.get_pop_iter(4):
    x.card()

