#! /usr/bin/env python

'''
    Command Line Utility to return a details for the selected VM
'''


import requests
import json
from icfd_library import vm_details

if __name__ == '__main__':

    import sys
    from pprint import pprint
    from argparse import ArgumentParser, FileType

    p = ArgumentParser()
    p.add_argument('vmid',                          # Name stored in namespace
                   metavar = 'Virtual Machine ID',            # Arguement name displayed to user
                   help = 'The ICFD vmid to return details for.',
                   type = str
                    )

    ns = p.parse_args()

    result = vm_details(ns.vmid)

    pprint (result)

