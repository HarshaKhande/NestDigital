# -*- coding: utf-8 -*-

import names

def main():
    
        source(findFile("scripts", "common.py"))

        startBrowser(
        "http://127.0.0.1:8000"
        )

        login(
        "admin",
        "admin123"
        )
