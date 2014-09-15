__author__ = 'Tyraan'
"""
#####################################################################################################################
mailtools package :interface to mail server transfers ,used by pymail2 ,PyMailGUI, and PyMailCGI;
does load ,sending parsing composing,and deleting ,with part attachments ,encodings (of both the email and Unicdode kind),etc.;
the parser,fetcher ,and sender classes are designed to be mixed-in to subclasses which use their  methods ,or used as embeded or starn
alone objects.

this package also includes convenience subclasses for silent mode, and more;
loads all mail text if pop server  doesn't do top;
doesn't handle thread or UI here , and allows askPassword to differ per subclass;
progress callback funcs get statuts; and calls raise exception on error--client must handle in GUI/ohter ;
this change from file to package: nested modules imported here for bwcompat;

"""

from .mailFethcer import *
from .mailSender import *
from .mailParser import *


__all__ ='mailFetcher','mailSender','mailParser'

