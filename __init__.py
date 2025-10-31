# -*- coding: utf-8 -*-
#
# Copyright © 2025 Audun Lund Johansen
#
# License: GNU AGPL, version 3 or later; http://www.gnu.org/copyleft/agpl.html

from aqt.addcards import AddCards
from anki.hooks import wrap


def reset_min_size(self):
    """
    Undo the setting of the minimum size.
    Called after setupEditor to override Anki's default minimum size.
    """
    self.setMinimumHeight(0)
    self.setMinimumWidth(0)


# Wrap the setupEditor method to reset minimum size
AddCards.setupEditor = wrap(AddCards.setupEditor, reset_min_size)
