#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class DefaultConfig:
    '''Default.'''

    DEBUG = True


class ProdConfig(DefaultConfig):
    '''Production.'''

    DEBUG = False
