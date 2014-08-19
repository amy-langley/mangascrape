from collections import namedtuple

TargetDescriptor = namedtuple(
    'TargetDescriptor', ['width', 'height', 'pixel_depth', 'is_color'])

# 70px of vertical space for UI

FIRST_EDITION = TargetDescriptor(
    width=600, height=730, pixel_depth=4, is_color=False)
NOOK = TargetDescriptor(
    width=600, height=730, pixel_depth=4, is_color=False)
SIMPLE_TOUCH = TargetDescriptor(
    width=600, height=730, pixel_depth=4, is_color=False)
GLOW_LIGHT = TargetDescriptor(
    width=758, height=954, pixel_depth=4, is_color=False)

COLOR = TargetDescriptor(
    width=600, height=954, pixel_depth=24, is_color=True)
TABLET = TargetDescriptor(
    width=600, height=954, pixel_depth=24, is_color=True)
HD = TargetDescriptor(
    width=900, height=1370, pixel_depth=24, is_color=True)
HD_PLUS = TargetDescriptor(
    width=1280, height=1850, pixel_depth=24, is_color=True)

ACCEPTED_FORMATS = ['pdf', 'epub']
