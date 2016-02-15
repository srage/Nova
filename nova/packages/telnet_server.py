# -*- encoding: utf-8 -*-
'''
The telnet protocol is insecure and unencrypted. The use of an unencrypted
transmission medium could allow a user with access to sniff network traffic the
ability to steal credentials. The ssh package provides an encrypted session and
stronger security and is included in most Linux distributions.
'''
from __future__ import absolute_import
from nova import *
import logging


def __virtual__():
    '''
    Compatibility Check
    '''
    if 'Linux' in __salt__['grains.get']('kernel'):
        return True
    return False


def audit():
    ret = _rpmquery('telnet-server')
    if 'not installed' in ret:
        return True
    return False
