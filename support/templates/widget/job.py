#!/usr/bin/env python

from jobs import AbstractJob


class {{ name|capitalize }}(AbstractJob):

    def __init__(self, conf):
        self.interval = conf['interval']

    def get(self):
        return {}