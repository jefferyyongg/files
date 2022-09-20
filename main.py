__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from genericpath import isfile
import os
import shutil

dir_cache = os.getcwd() + "\cache"


def clean_cache():
    dir_cache
    if not os.path.exists(dir_cache):
        os.mkdir(dir_cache)
    else:
        for f in os.listdir(dir_cache):
            os.remove(os.path.join(dir_cache, f))


def cache_zip(dir_zip, dir_cache):
    shutil.unpack_archive(dir_zip, dir_cache)


def cached_files():
    cache_list = []
    dir_cache
    for f in os.listdir(dir_cache):
        cache_list.append(dir_cache + f"\{f}")
    return cache_list


def find_password(cached_files):
    password = "password"
    for f in cached_files:
        with open(f, "r") as data:
            lines = data.readlines()
            for l in lines:
                if password in l:
                    password = l.split(" ")
                    return password[1].strip()
