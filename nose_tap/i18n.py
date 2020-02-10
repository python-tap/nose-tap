# Copyright (c) 2020, Matt Layman

import gettext
import os

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
translate = gettext.translation('nose_tap', localedir, fallback=True)
_ = translate.gettext
