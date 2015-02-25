#! /usr/bin/env python

'''
    Command Line Utility to power on the selected VM
'''


import requests
import json
from icfd_library import vm_poweroff


if __name__ == '__main__':

    import sys
    from pprint import pprint
    from argparse import ArgumentParser, FileType

    p = ArgumentParser()
    p.add_argument('vmid',                          # Name stored in namespace
                   metavar = 'Virtual Machine ID',            # Arguement name displayed to user
                   help = 'The ICFD vmid.',
                   type = str
                    )

    ns = p.parse_args()

    result = vm_poweroff(ns.vmid)

    pprint (result)

