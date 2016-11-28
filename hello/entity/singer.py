#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Singer:
    sang = ''

    def __init__(self, sang):
        self.sang = sang

    def sing(self):
        print("我会唱", self.sang)
