#!/usr/bin/env python3
from .light_spellbook import light_spell_record
from .dark_spellbook import dark_spell_record


check_light = light_spell_record
check_dark = dark_spell_record


__all__ = ["check_light", "check_dark"]
