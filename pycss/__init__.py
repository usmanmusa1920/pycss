# -*- coding: utf-8 -*-
"""
    =====================
    @ pycss software
    =====================

    PYCSS

    Pycss it is python text-style ✅ not python textile! 🤔 it actually print your text on terminal in different kind of colors.

    TODO: To print text with color using python print, instead of using `print` function, use any of the following functions (purple, blue, cyan, green, yellow, red, normal, bold, underline, log_style)
        >>> from pycss import (purple, blue, cyan, green, yellow, red, normal, bold, underline)

        >>> purple('I am purple in color')
        >>> blue('I am blue in color')
        >>> cyan('I am cyan in color')
        >>> green('I am green in color')
        >>> yellow('I am yellow in color')
        >>> red('I am red in color')
        >>> normal('I am a normal text')
        >>> bold('I make text bold')
        >>> underline('I underline text')
    
    TODO: To print logging text with color
        >>> from pycss import log_style
        
        >>> log_style('I am info logger')
        >>> log_style('I am yellow logger', col='yellow')
        >>> log_style('I am error logger', log='error')
"""

from datetime import datetime

__title__ = 'pycss'
__version__ = '0.0.1'
__author__ = 'Usman Musa'
__author_email__ = 'usmanmusa1920@gmail.com'
__author_website__ = 'https://usmanmusa1920.github.io'
__repository__ = 'https://github.com/usmanmusa1920/pycss'
__url__ = 'https://pycss.readthedocs.io'
__license__ = 'MIT'
__copyright__ = f'Copyright (C) 2023 - {datetime.today().year} Usman Musa'
__description__ = 'Pycss it is python text-style ✅ not python textile! 🤔 it actually print your text on terminal in different kind of colors.'


from .tcolor import *
from .lcolor import log_style


__all__ = [
    'purple',
    'blue',
    'cyan',
    'green',
    'yellow',
    'red',
    'normal',
    'bold',
    'underline',
    'log_style',
]
