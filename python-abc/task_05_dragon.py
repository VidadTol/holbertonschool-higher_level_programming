#!/usr/bin/env python3
"""
This module defines mixin classes SwimMixin and FlyMixin,
and a Dragon class that uses these mixins.
    """


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
