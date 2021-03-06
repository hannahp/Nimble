# MayaCommandLink.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

import functools

from nimble.NimbleEnvironment import NimbleEnvironment

#___________________________________________________________________________________________________ MayaCommandLink
class MayaCommandLink(object):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, connection):
        self._connection = connection
        self._commands   = None

        if NimbleEnvironment.inMaya():
            import maya.cmds as mc
            self._commands = mc

#===================================================================================================
#                                                                               I N T R I N S I C

#___________________________________________________________________________________________________ __getattr__
    def __getattr__(self, item):
        if item.startswith('_'):
            raise AttributeError

        if self._commands:
            return getattr(self._commands, item)

        return functools.partial(self._connection.maya, item)



