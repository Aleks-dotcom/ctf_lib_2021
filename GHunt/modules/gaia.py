#!/usr/bin/env python3

import json
import sys
import os
from datetime import datetime
from io import BytesIO
from os.path import isfile
from pathlib import Path
from pprint import pprint

import httpx
from PIL import Image
from geopy.geocoders import Nominatim

import config
from lib.banner import banner
import lib.gmaps as gmaps
import lib.youtube as ytb
from lib.utils import *


def gaia_hunt(gaiaID):
    banner()

    if not gaiaID:
        exit("Please give a valid GaiaID.\nExample : 113127526941309521065")

    if not isfile(config.data_path):
        exit("Please generate cookies and tokens first, with the check_and_gen.py script.")

    internal_auth = ""
    internal_token = ""

    cookies = {}

    with open(config.data_path, 'r') as f:
        out = json.loads(f.read())
        internal_auth = out["internal_auth"]
        internal_token = out["keys"]["internal"]
        cookies = out["cookies"]

    client = httpx.Client(cookies=cookies, headers=config.headers)

    is_within_docker = within_docker()
    if is_within_docker:
        print("[+] Docker detected, profile pictures will not be saved.")

    geolocator = Nominatim(user_agent="nominatim")

    # get name & profile picture
    account = get_account_data(client, gaiaID, internal_auth, internal_token, config)
    name = account["name"]

    if name:
        print(f"Name : {name}")

    # profile picture
    profile_pic_url = account["profile_pic_url"]
    req = client.get(profile_pic_url)

    profile_pic_img = Image.open(BytesIO(req.content))
    profile_pic_hash = image_hash(profile_pic_img)
    is_default_profile_pic = detect_default_profile_pic(profile_pic_hash)

    if not is_default_profile_pic and not is_within_docker:
        print("\n[+] Custom profile picture !")
        print(f"=> {profile_pic_url}")
        if config.write_profile_pic and not is_within_docker:
            open(Path(config.profile_pics_dir) / f'{gaiaID}.jpg', 'wb').write(req.content)
            print("Profile picture saved !")
    else:
        print("\n[-] Default profile picture")

    print(f"\nGaia ID : {gaiaID}")

    # check YouTube
    if name:
        confidence = None
        data = ytb.get_channels(client, name, config.data_path,
                                config.gdocs_public_doc)
        if not data:
            print("\n[-] YouTube channel not found.")
        else:
            confidence, channels = ytb.get_confidence(data, name, profile_pic_hash)
            
            if confidence:
                print(f"\n[+] YouTube channel (confidence => {confidence}%) :")
                for channel in channels:
                    print(f"- [{channel['name']}] {channel['profile_url']}")
                possible_usernames = ytb.extract_usernames(channels)
                if possible_usernames:
                    print("\n[+] Possible usernames found :")
                    for username in possible_usernames:
                        print(f"- {username}")
            else:
                print("\n[-] YouTube channel not found.")

    # reviews
    reviews = gmaps.scrape(gaiaID, client, cookies, config, config.headers, config.regexs["review_loc_by_id"], config.headless)

    if reviews:
        confidence, locations = gmaps.get_confidence(geolocator, reviews, config.gmaps_radius)
        print(f"\n[+] Probable location (confidence => {confidence}) :")

        loc_names = []
        for loc in locations:
            loc_names.append(
                f"- {loc['avg']['town']}, {loc['avg']['country']}"
            )

        loc_names = set(loc_names)  # delete duplicates
        for loc in loc_names:
            print(loc)
