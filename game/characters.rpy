define ILORA = Character("ILORA")
define ICARUS = Character("ICARUS")
define SEONGJIN = Character("SEONGJIN")

# image hiyori = Live2D("sprites/hiyori", base=.8, loop=True)
# show hiyori m01 onlayer sprites
# init python:
#     def MyLive2D(*args, fallback=Placeholder(text="no live2d"), **kwargs):
#         if renpy.has_live2d():
#             return Live2D(*args, **kwargs)
#         else:
#             return fallback
# image icarus = MyLive2D("images/ywtsm icarus", fallback="images/icarus.png")
image icarus = "images/icarus.png"

transform icarus_transform:
    zoom 1.5
    xalign 0.5
    yalign -6.0
    alpha 0.95
    linear 1.0 alpha 1.0
    linear 1.0 alpha 0.95
    linear .5 alpha 0.9
    linear 1.0 alpha 1.0
    linear 1.0 alpha 0.97
    linear 1.0 alpha 0.87
    linear .5 alpha 0.9
    repeat