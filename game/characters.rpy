define ILORA = Character("ILORA")
define ICARUS = Character("ICARUS")
define SEONGJIN = Character("SEONGJIN")

# image icarus = "images/icarus.png"
image icarus = "images/icarus.png"
image i = Live2D("images/icarus", base=0.5, default_fade=0.5, loop=True, fade=True, seamless=True)
define transition = Fade(0.5, 1, 0.5, color="#fff")
define flash = Fade(0.5, 0.1, 1, color="#fff")
define fadehold = Fade(0.5, 1.0, 0.5)
define fade = Fade(0.5, 0.0, 0.5)
define blink = Fade(0.1, 0, 0.1)

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