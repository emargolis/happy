#!/usr/bin/env python

#
#    Copyright (c) 2015-2017 Nest Labs, Inc.
#    All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

##
#    @file
#       A Happy command line utility that creates virtual link.
#
#       The command is executed by instantiating and running HappyLinkAdd class.
#

import getopt
import sys

import happy.HappyLinkAdd
from happy.Utils import *

if __name__ == "__main__":
    options = happy.HappyLinkAdd.option()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:qp",
                                   ["help", "type=", "quiet", "tap"])

    except getopt.GetoptError as err:
        print happy.HappyLinkAdd.HappyLinkAdd.__doc__
        print hred(str(err))
        sys.exit(hred("%s: Failed to parse arguments." % (__file__)))

    for o, a in opts:
        if o in ("-h", "--help"):
            print happy.HappyLinkAdd.HappyLinkAdd.__doc__
            sys.exit(0)

        elif o in ("-q", "--quiet"):
            options["quiet"] = True

        elif o in ("-t", "--type"):
            options["type"] = a

        elif o in ("-p", "--tap"):
            options["tap"] = True

        else:
            assert False, "unhandled option"

    if len(args) == 1:
        options["type"] = args[0]

    cmd = happy.HappyLinkAdd.HappyLinkAdd(options)
    cmd.start()
