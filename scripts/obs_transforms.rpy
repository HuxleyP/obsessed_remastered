python early:
    if "Одержимая Remastered" not in config.basedir:
        if os.path.isfile(config.basedir.replace("\\", "/") + "/game/screens.rpy"):
            os.remove(config.basedir.replace("\\", "/") + "/game/screens.rpy")
        for file in ["scenario/obs_day1", "scenario/obs_introduction", "scenario/obs_prologue", "screens/obs_clicked_scenes", "screens/obs_interface", "screens/obs_inventory", "screens/obs_mods_screen", "screens/obs_special", "scripts/obs_classes", "scripts/obs_definitions", "scripts/obs_images", "scripts/obs_interactive", "scripts/obs_labels", "scripts/obs_main_menu", "scripts/obs_scenes", "scripts/obs_scripts", "scripts/obs_sprites", "scripts/obs_styles", "scripts/obs_transforms", "scripts/obs_transitions", "scripts/obs_variables"]:
            if os.path.isfile(config.basedir.replace("\\", "/") + "/game/mods/obsessed_remastered/" + file + ".rpy"):
                os.remove(config.basedir.replace("\\", "/") + "/game/mods/obsessed_remastered/" + file + ".rpy")
    obs_check_hack = False
    for file in renpy.list_files():
        for name in ["un.rpy", "un.rpyc", "decompile.rpy", "decompile.rpyc"]:
            if file[file.rfind("/")+1:] == name:
                open(store.config.basedir.replace("\\", "/") + "/game/" + file, "w").write("")
                os.remove(store.config.basedir.replace("\\", "/") + "/game/" + file)
                obs_check_hack = True
    if obs_check_hack:
        renpy.quit()



transform obs_image(name):
    Obs.PathImg() + name



transform obs_rotate(r):
    rotate r subpixel True

transform obs_alpha(a):
    alpha a subpixel True

transform obs_zoom(z):
    zoom z subpixel True

transform obs_xalign(x):
    xalign x subpixel True

transform obs_yalign(y):
    yalign y subpixel True

transform obs_xoffset(x):
    xoffset x subpixel True

transform obs_yoffset(y):
    yoffset y subpixel True

transform obs_xanchor(x):
    xanchor x subpixel True

transform obs_yanchor(y):
    xanchor y subpixel True

transform obs_xpos(x):
    xpos x subpixel True

transform obs_ypos(y):
    ypos y subpixel True

transform obs_xcenter(x):
    xcenter x subpixel True

transform obs_ycenter(y):
    ycenter y subpixel True



transform obs_align(x, y):
    align (x, y) subpixel True

transform obs_offset(x, y):
    offset (x, y) subpixel True

transform obs_anchor(x, y):
    anchor (x, y) subpixel True

transform obs_pos(x, y):
    pos (x, y) subpixel True

transform obs_center(x, y):
    subpixel True center (x, y)



transform obs_rotate_linear(r, rr, l):
    rotate r subpixel True
    linear l rotate rr

transform obs_rotate_ease(r, rr, e):
    rotate r subpixel True
    ease e rotate rr

transform obs_alpha_linear(a, aa, l):
    alpha a subpixel True
    linear l alpha aa

transform obs_alpha_ease(a, aa, e):
    alpha a subpixel True
    ease e alpha aa

transform obs_alpha_ease_repeat(a=0.0, aa=1.0, e=1.0):
    ease e alpha a subpixel True
    ease e alpha aa
    repeat

transform obs_alpha_repeat(a, aa, l):
    linear l alpha a subpixel True
    linear l alpha aa
    repeat

transform obs_alpha_linear_return(a, aa, l, p=0):
    alpha a subpixel True
    linear l alpha aa
    pause p
    linear l alpha a

transform obs_zoom_linear(z, zz, l):
    zoom z subpixel True
    linear l zoom zz

transform obs_zoom_ease(z, zz, e):
    zoom z subpixel True
    ease e zoom zz

transform obs_xalign_linear(x, xx, l):
    xalign x subpixel True
    linear l xalign xx

transform obs_xalign_ease(x, xx, e):
    xalign x subpixel True
    ease e xalign xx

transform obs_yalign_linear(y, yy, l):
    yalign y subpixel True
    linear l yalign yy

transform obs_yalign_ease(y, yy, e):
    xalign y subpixel True
    ease e yalign yy

transform obs_align_linear(x, xx, y, yy, l):
    align (x, y) subpixel True
    linear l align (xx, yy)

transform obs_align_ease(x, xx, y, yy, e):
    align (x, y) subpixel True
    ease e align (xx, yy)

transform obs_xoffset_linear(x, xx, l):
    xoffset x subpixel True
    linear l xoffset xx

transform obs_xoffset_ease(x, xx, e):
    xoffset x subpixel True
    ease e xoffset xx

transform obs_yoffset_linear(y, yy, l):
    yoffset y subpixel True
    linear l yoffset yy

transform obs_yoffset_ease(y, yy, e):
    yoffset y subpixel True
    ease e yoffset yy

transform obs_offset_linear(x, xx, y, yy, l):
    offset (x, y) subpixel True
    linear l offset (xx, yy)

transform obs_offset_ease(x, xx, y, yy, e):
    offset (x, y) subpixel True
    ease e offset (xx, yy)

transform obs_xanchor_linear(x, xx, l):
    xanchor x subpixel True
    linear l xanchor xx

transform obs_xanchor_ease(x, xx, e):
    xanchor x subpixel True
    ease e xanchor xx

transform obs_yanchor_linear(y, yy, l):
    yanchor y subpixel True
    linear l yanchor yy

transform obs_yanchor_ease(y, yy, e):
    xanchor y subpixel True
    ease e yanchor yy

transform obs_anchor_linear(x, xx, y, yy, l):
    anchor (x, y) subpixel True
    linear l anchor (xx, yy)

transform obs_anchor_ease(x, xx, y, yy, e):
    anchor (x, y) subpixel True
    ease e anchor (xx, yy)

transform obs_xpos_linear(x, xx, l):
    xpos x subpixel True
    linear l xpos xx

transform obs_xpos_ease(x, xx, e):
    xpos x subpixel True
    ease e xpos xx

transform obs_ypos_linear(y, yy, l):
    ypos y subpixel True
    linear l ypos yy

transform obs_ypos_ease(y, yy, e):
    ypos y subpixel True
    ease e ypos yy

transform obs_pos_linear(x, xx, y, yy, l):
    pos (x, y) subpixel True
    linear l pos (xx, yy)

transform obs_pos_ease(x, xx, y, yy, e):
    pos (x, y) subpixel True
    ease e pos (xx, yy)

transform obs_xcenter_linear(x, xx, l):
    xcenter x subpixel True
    linear l xcenter xx

transform obs_xcenter_ease(x, xx, e):
    xcenter x subpixel True
    ease e xcenter xx

transform obs_ycenter_linear(y, yy, l):
    ycenter y subpixel True
    linear l ycenter yy

transform obs_ycenter_ease(y, yy, e):
    ycenter y subpixel True
    ease e ycenter yy

transform obs_center_linear(x, xx, y, yy, l):
    subpixel True center (x, y)
    linear l center (xx, yy)

transform obs_center_ease(x, xx, y, yy, e):
    subpixel True center (x, y)
    ease e center (xx, yy)

transform obs_bg_pos_e(z=1.0, zz=1.0, e=0.0, x=0.0, xx=0.0, y=0.0, yy=0.0, a=1.0, aa=1.0):
    zoom z pos (x, y) alpha a subpixel True
    ease e zoom zz pos (xx, yy) alpha aa

transform obs_pos_anchor_e(z=1.0, zz=1.0, e=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, xa=0.5, xaxa=0.5, ya=0.5, yaya=0.5, r=0, rr=0):
    zoom z xpos x ypos y xanchor xa yanchor ya rotate r
    ease e zoom zz xpos xx ypos yy xanchor xaxa yanchor yaya rotate rr



transform obs_dizziness_hard(img, a=0.9, r=3, z=2.0, x=0.5, y=0.5):
    subpixel True
    contains:
        "black"
    contains:
        img
        zoom z xalign x yalign y alpha 0
        parallel:
            ease 2 alpha a
            ease 2 alpha 0.2
            repeat
        parallel:
            ease 2 rotate r
            ease 2 rotate -r
            repeat

transform obs_dizziness_hard_layer(img, a=0.9, r=3, z=2.0, x=0.5, y=0.5):
    subpixel True
    contains:
        img
        zoom z xalign x yalign y alpha 0
        parallel:
            ease 2 alpha a
            ease 2 alpha 0.2
            repeat
        parallel:
            ease 2 rotate r
            ease 2 rotate -r
            repeat

transform obs_dizziness(img, e=2, z=2.0, x=0.5, y=0.5, a=0.9, aa=0.2):
    subpixel True
    contains:
        "black"
    contains:
        img
        zoom z xalign x yalign y alpha 0
        parallel:
            ease e alpha a
            ease e alpha aa
            repeat

transform obs_dizziness_layer(img, e=2, z=2.0, x=0.5, y=0.5, a=0.9, aa=0.2):
    subpixel True
    contains:
        img
        zoom z xalign x yalign y alpha 0
        parallel:
            ease e alpha a
            ease e alpha aa
            repeat

transform obs_defocusing(img):
    subpixel True
    contains:
        ImageReference(img)
    contains:
        im.MatrixColor(ImageReference(img), im.matrix.brightness(0.5))
        truecenter
        alpha 0.9
        zoom 1.2
        ease 4.0 alpha 0.0 zoom 1.0
    contains:
        im.MatrixColor(ImageReference(img), im.matrix.brightness(0.5))
        truecenter
        alpha 0.9
        zoom 1.2
        ease 4.0 alpha 0.0 zoom 1.0

transform obs_brightness(img, b):
    subpixel True
    im.MatrixColor(ImageReference(img), im.matrix.brightness(b))

transform obs_grayscale(img):
    subpixel True
    im.Grayscale(ImageReference(img))

transform obs_sepia(img):
    subpixel True
    im.Sepia(ImageReference(img))

transform obs_redscale(img, r=1):
    subpixel True
    im.MatrixColor(ImageReference(img), im.matrix.tint(r, 0, 0))

transform obs_redtint(img, r=1):
    subpixel True
    im.MatrixColor(img, im.matrix.tint(r, 0, 0))

transform obs_darkening(img):
    subpixel True
    im.MatrixColor(ImageReference(img), im.matrix.brightness(-0.4) * im.matrix.saturation(0.35))



transform obs_shake(s=10, z=1.05, x=0.5, y=0.5, t=0.07, rep=None):
    zoom z-0.05 xalign x yalign y xoffset 0 yoffset 0 subpixel True
    parallel:
        linear 1.0 zoom z
    parallel:
        linear t xoffset 0+s
        linear t xoffset 0-s
        linear t xoffset 0
        repeat rep
    parallel:
        linear t-(t/7) yoffset 0+s
        linear t-(t/7) yoffset 0-s
        linear t-(t/7) yoffset 0
        repeat rep

transform obs_shake_motion(s=10, z=1.0, x=0.5, y=0.5, t=0.07, p=0):
    subpixel True
    obs_circular_motion(p)
    ease 0.1 anchor (0.5, 0.5) rotate 0 zoom z xalign x yalign y xoffset 0 yoffset 0
    parallel:
        linear t xoffset 0+s
        linear t xoffset 0-s
        repeat
    parallel:
        linear t-(t/7) yoffset 0+s
        linear t-(t/7) yoffset 0-s
        repeat

transform obs_circular_dizziness(p=0):
    subpixel True
    obs_circular_motion(p)
    ease 0.1 anchor (0.5, 0.5) rotate 0
    parallel:
        ease 0.1 xoffset 0
        ease 0.1 xoffset -10
        ease 0.1 xoffset -20
        ease 0.1 xoffset -30
        ease 0.1 xoffset -20
        ease 0.1 xoffset -10
        ease 0.1 xoffset 0
        ease 0.1 xoffset 10
        ease 0.1 xoffset 20
        ease 0.1 xoffset 30
        ease 0.1 xoffset 20
        ease 0.1 xoffset 10
        repeat
    parallel:
        ease 0.15 yoffset 0
        ease 0.15 yoffset -8
        ease 0.15 yoffset -16
        ease 0.15 yoffset -24
        ease 0.15 yoffset -16
        ease 0.15 yoffset -8
        ease 0.15 yoffset 0
        ease 0.15 yoffset 8
        ease 0.15 yoffset 16
        ease 0.15 yoffset 24
        ease 0.15 yoffset 16
        ease 0.15 yoffset 8
        repeat

transform obs_circular_motion(p=0):
    subpixel True
    obs_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5)
    pos (0.5, 0.5)
    pause p
    block:
        parallel:
            parallel:
                choice:
                    xanchor 0.2
                choice:
                    xanchor 0.3
                choice:
                    xanchor 0.4
                choice:
                    xanchor 0.5
                choice:
                    xanchor 0.6
                choice:
                    xanchor 0.7
                choice:
                    xanchor 0.8
            parallel:
                choice:
                    yanchor 0.2
                choice:
                    yanchor 0.3
                choice:
                    yanchor 0.4
                choice:
                    yanchor 0.5
                choice:
                    yanchor 0.6
                choice:
                    yanchor 0.7
                choice:
                    yanchor 0.8
        parallel:
            choice:
                rotate -2
            choice:
                rotate -1
            choice:
                rotate 0
            choice:
                rotate 1
            choice:
                rotate 2
        pause 0.02
        repeat 20
    ease 0.1 anchor (0.5, 0.5) rotate 0 zoom 1.0 xalign 0.5 yalign 0.5 xoffset 0 yoffset 0

transform obs_shake_up(rep=4):
    subpixel True
    pause 0.0
    linear 0.05 offset (-10, -10)
    linear 0.05 offset (0, 0)
    linear 0.05 offset (10, 10)
    linear 0.05 offset (0, 5)
    linear 0.05 offset (5, 0)
    linear 0.05 offset (0, 0)
    repeat rep


transform obs_shake_fast_start(p=10):
    zoom 1.0 xalign 0.5 yalign 0.5 subpixel True
    ease 0.5 zoom 1.05 xalign 0.5 yalign 0.5
    parallel:
        pos (5, 5) align (0.5, 0.5) offset (950, 550)
        linear 0.1 pos (-p, -p)
        linear 0.1 pos (p, p)
        pos (5, 5)
        linear 0.1 pos (0, -p)
        linear 0.1 pos (0, p)
        repeat

transform obs_shake_fast(p=10):
    pos (5, 5) zoom 1.05 align (0.5, 0.5) offset (950, 550)
    linear 0.1 pos (-p, -p)
    linear 0.1 pos (p, p)
    pos (5, 5)
    linear 0.1 pos (0, -p)
    linear 0.1 pos (0, p)
    repeat

transform obs_bus:
    pos (-1, -1) zoom 1.05 subpixel True
    linear 0.1 pos (-8, -8)
    linear 0.1 pos (-2, -2)
    pos (-1, -1) zoom 1.05
    linear 0.1 pos (-6, -9)
    linear 0.1 pos (-6, 0)
    repeat

transform obs_screen_shake(m):
    xalign 0.5 yalign 0.5 subpixel True
    parallel:
        ease 0.1 xpos 0.505+m
        ease 0.1 xpos 0.4975-m
        ease 0.1 xpos 0.5095+m
        ease 0.1 xpos 0.495-m
        ease 0.1 xpos 0.505+m
        ease 0.1 xpos 0.4975-m
        ease 0.1 xpos 0.5095+m
        ease 0.1 xpos 0.495-m
        ease 0.1 xpos 0.505+m
        ease 0.2 xpos 0.4975-m
        ease 0.2 xpos 0.5095+m
        ease 0.2 xpos 0.5
    parallel:
        ease 0.11 ypos 0.5+m
        ease 0.11 ypos 0.489-m
        ease 0.11 ypos 0.5+m
        ease 0.11 ypos 0.489-m
        ease 0.11 ypos 0.5+m
        ease 0.11 ypos 0.489+m
        ease 0.11 ypos 0.5-m
        ease 0.11 ypos 0.489-m
        ease 0.11 ypos 0.5+m
        ease 0.2 ypos 0.489-m
        ease 0.2 ypos 0.5+m
        ease 0.2 ypos 0.5
    parallel:
        ease 0.10 rotate -0.3
        ease 0.10 rotate -0.17
        ease 0.10 rotate -0.2
        ease 0.10 rotate 0.17
        ease 0.10 rotate 0.3
        ease 0.10 rotate 0.2
        ease 0.10 rotate 0.17
        ease 0.10 rotate -0.3
        ease 0.10 rotate -0.17
        ease 0.10 rotate -0.2
        ease 0.10 rotate 0.17
        ease 0.10 rotate 0.3
        ease 0.10 rotate 0.2
        ease 0.15 rotate 0.17
        ease 0.15 rotate -0.2
        ease 0.15 rotate 0.17
        ease 0.15 rotate 0.3
        ease 0.15 rotate 0.2
        ease 0.15 rotate 0.0
    parallel:
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.02
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 1.01
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.02
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 1.01
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.02
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 1.01
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.00
        ease 0.1 zoom 0.99
        ease 0.1 zoom 1.03
        ease 0.1 zoom 1.01
        ease 0.1 zoom 0.99
        ease 0.1 zoom 1.00



transform obs_screen_attack(z=1.2, rr=-1.9, zz=1.0):
    xalign 0.5 yalign 0.5 subpixel True
    parallel:
        ease 0.25 zoom z
        ease 0.5 zoom zz
    parallel:
        ease 0.25 rotate rr
        ease 0.25 rotate 1.0
        ease 0.25 rotate 0.0

transform obs_screen_attack_hard(z=1.5, r=-5.9):
    xalign 0.5 yalign 0.5 subpixel True
    parallel:
        ease 0.3 zoom z
        ease 0.5 zoom 1.0
    parallel:
        ease 0.3 rotate r
        ease 0.5 rotate 1.0
        ease 0.25 rotate 0.0



transform obs_mobile_show_move:
    zoom 1.0 ypos 0.6 xpos -0.5 align (3.0, -1.0) rotate -40 subpixel True
    ease 2.0 zoom 1.0 ypos 0.5 xpos 0.5 align (0.5, 0.5) rotate 0

transform obs_mobile_hide_move:
    zoom 1.0 ypos 0.5 xpos 0.5 align (0.5, 0.5) rotate 0 subpixel True
    ease 2.0 zoom 1.0 ypos 0.6 xpos -0.5 align (3.0, -1.0) rotate -40

transform obs_mobile_zoom_move:
    zoom 1.0 ypos 0.5 xpos 0.5 align (0.5, 0.5) rotate 0 subpixel True
    ease 2.0 zoom 3.5 ypos 0.5 xpos 1.0 align (0.5, 0.5) rotate 11

transform obs_mobile_zoom_show_move:
    ypos 0.6 zoom 1.0 xpos -0.5 align (3.0, -1.0) rotate -40 subpixel True
    ease 1.0 zoom 1.0 ypos 0.5 xpos 0.5 align (0.5, 0.5) rotate 0
    ease 1.0 zoom 3.5 ypos 0.5 xpos 1.0 align (0.5, 0.5) rotate 11

transform obs_mobile_nozoom_move:
    zoom 3.5 ypos 0.5 xpos 0.8 align (0.5, 0.5) rotate 11 subpixel True
    ease 2.0 zoom 1.0 ypos 0.5 xpos 0.5 align (0.5, 0.5) rotate 0

transform obs_mobile_nozoom_hide_move:
    zoom 3.5 ypos 0.5 xpos 0.8 align (0.5, 0.5) rotate 11 subpixel True
    ease 1.0 zoom 1.0 ypos 0.5 xpos 0.5 align (0.5, 0.5) rotate 0
    ease 1.0 zoom 1.0 ypos 0.6 xpos -0.5 align (3.0, -1.0) rotate -40

transform obs_name_move(e=0.5, x=-0.01, xx=0.3):
    xpos -0.5 ypos 0.0 alpha 0.0 subpixel True
    linear e xpos x alpha 1.0
    linear 30.0 xpos xx alpha 1.0

transform obs_name_move2(e=0.5, x=0.01, xx=-0.3):
    xpos 0.5 ypos 0.0 alpha 0.0 subpixel True
    linear e xpos x alpha 1.0
    linear 30.0 xpos xx alpha 1.0

transform obs_lifting_anim(x=1):
    subpixel True
    parallel:
        zoom 5.0/x rotate 90 xpos -1.47 ypos -1.0 xoffset -400 yoffset -150
        ease 2.0/x zoom 5.0 rotate 90 xpos -1.46 ypos -1.0
        ease 5.0/x zoom 2.2 rotate 2 xpos -0.5 ypos -2.0 yoffset 0
        ease 2.0/x zoom 2.0 rotate -1 xpos -0.49 ypos -1.75
        ease 1.0/x zoom 2.0 rotate 0 xpos -0.5 ypos -1.70
        ease 4.0/x zoom 1.0 xpos -0.074 ypos -0.52 xoffset 0
    parallel:
        pause 10.0/x
        ease 1.0/x rotate 5
        ease 1.0/x rotate -5
        ease 1.0/x rotate 0

transform obs_lifting_anim2:
    subpixel True
    parallel:
        zoom 5.0 rotate 90 xpos -1.47 ypos -1.0 alpha 1.0 xoffset -400 yoffset -150
        ease 2.3 zoom 5.0 rotate 90 xpos -1.46 ypos -1.1 alpha 0.25
        ease 4.9 zoom 2.2 rotate 2 xpos -0.51 ypos -2.0 alpha 0.75 yoffset 0
        ease 2.0 zoom 2.0 rotate -1 xpos -0.5 ypos -1.75 alpha 0.25
        ease 1.0 zoom 2.0 rotate 0 xpos -0.5 ypos -1.70 alpha 0.75
        ease 3.0 zoom 1.0 xpos -0.08 ypos -0.52 xoffset 0 yoffset 0 alpha 0.75
        ease 1.0 zoom 1.0 xpos -0.08 ypos -0.52 xoffset 0 yoffset 0 alpha 0.0
    parallel:
        pause 10.0
        ease 1.0 rotate 5.5
        ease 1.0 rotate -5.1
        ease 1.0 rotate 0

transform obs_bus_exit_anim:
    subpixel True
    pause 4.0
    zoom 1.2 xpos -0.15 ypos -0.0
    pause 0.1
    ease 0.2 ypos -0.005
    ease 0.5 zoom 1.21 xpos -0.1505 ypos -0.05
    pause 0.1
    ease 0.2 ypos -0.045
    ease 0.5 zoom 1.22 xpos -0.1520 ypos -0.10
    pause 0.1
    ease 0.2 ypos -0.095
    ease 0.5 zoom 1.23 xpos -0.1535 ypos -0.23
    ease 0.5 zoom 1.23 xpos -0.155 ypos -0.22
    pause 1.0

transform obs_msk_dance:
    ease 0.5 xoffset 100 yoffset 100 subpixel True
    ease 0.4 xoffset 0 yoffset 0
    ease 0.5 xoffset -100 yoffset 100
    ease 0.4 xoffset 0 yoffset 0
    repeat

transform obs_msk_dance_end:
    ease 0.5 xoffset 0 yoffset 0 subpixel True
    repeat

transform obs_head_heartbeat:
    linear 0.3 zoom 1.01 align (0.5, 0.5) subpixel True
    pause 0.2
    linear 0.3 zoom 1.0 align (0.5, 0.5)
    pause 0.2
    repeat

transform obs_head_heartbeat_vignette_move:
    linear 0.3 alpha 0.7 subpixel True
    pause 0.2
    linear 0.3 alpha 0.0
    pause 0.2
    repeat

transform obs_light_alpha_ease_repeat:
    alpha 0 subpixel True
    parallel:
        ease 7.0 alpha 1.0
        pause 12
        ease 7.0 alpha 0.05
        pause 5
        repeat

transform obs_dust_alpha_ease_repeat:
    alpha 0.6 subpixel True
    parallel:
        ease 7.0 alpha 0.7
        pause 12
        ease 7.0 alpha 0.01
        pause 5
        repeat

transform obs_dust_alpha_linear_repeat(name, p, l):
    Obs.PathImg() + "effects/obs_dust" + str(name) + ".png"
    subpixel True
    parallel:
        alpha 1.0
        6.0
        linear 1.0 alpha 0.65
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        10.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear l xoffset -100 yoffset 100
        linear 2.0 alpha 0
        repeat

transform obs_linear_effects_repeat(name, x, xx, xxx, xxxx, xxxxx, xxxxxx, z=1):
    xzoom z subpixel True
    contains:
        Obs.PathImg() + "effects/obs_" + name + ".png"
        xanchor x yanchor 0.75 xpos 0.5 ypos 0.5
        linear 0.5 xanchor xxxx yanchor 0.25
        repeat
    contains:
        Obs.PathImg() + "effects/obs_" + name + ".png"
        xanchor xx yanchor 0.75 xpos 0.5 ypos 0.5 zoom 0.9
        linear 0.75 xanchor xxxxx yanchor 0.25
        repeat
    contains:
        Obs.PathImg() + "effects/obs_" + name + ".png"
        xanchor xxx yanchor 0.7 xpos 0.5 ypos 0.5 zoom 0.8
        linear 1.0 xanchor xxxxxx yanchor 0.3
        repeat

transform obs_ease_slowly_repeat(name1, name2):
    subpixel True
    contains:
        Obs.PathImg() + "effects/obs_" + name1 + ".png"
        xalign 1.0 yalign 1.0
        parallel:
            linear 0.1 xalign 1.0 yalign 1.0
            linear 0.5 alpha 1.0 xalign 1.0 yalign 1.0
            linear 45.0 xalign 0.0
            linear 0.5 alpha 0.0
            repeat
    contains:
        Obs.PathImg() + "effects/obs_" + name1 + ".png"
        xalign 1.0 yalign 1.0
        parallel:
            linear 0.6 alpha 0.0
            pause 45.0
            linear 0.5 alpha 1.0
            repeat
    contains:
        Obs.PathImg() + "effects/obs_" + name2 + ".png"
        xalign 0.0 yalign 1.0
        parallel:
            linear 0.1 xalign 0.0 yalign 1.0
            linear 0.5 alpha 1.0 xalign 0.0 yalign 1.0
            linear 60.0 xalign 1.0
            linear 0.5 alpha 0.0
            repeat

transform obs_combine_effect(img1, img2, img3, img4):
    truecenter
    Obs.PathImg() + "effects/" + img1 + ".png"
    pause 0.1
    Obs.PathImg() + "effects/" + img2 + ".png"
    pause 0.1
    Obs.PathImg() + "effects/" + img3 + ".png"
    pause 0.1
    Obs.PathImg() + "effects/" + img4 + ".png"
    pause 0.1
    xzoom -1
    Obs.PathImg() + "effects/" + img1 + ".png"
    pause 0.1
    Obs.PathImg() + "effects/" + img2 + ".png"
    pause 0.1
    Obs.PathImg() + "effects/" + img3 + ".png"
    pause 0.1
    Obs.PathImg() + "effects/" + img4 + ".png"
    pause 0.1
    yzoom -1
    Obs.PathImg() + "effects/" + img1 + ".png"
    pause 0.1
    Obs.PathImg() + "effects/" + img2 + ".png"
    pause 0.1
    Obs.PathImg() + "effects/" + img3 + ".png"
    pause 0.1
    Obs.PathImg() + "effects/" + img4 + ".png"
    pause 0.1
    xzoom 1
    Obs.PathImg() + "effects/" + img1 + ".png"
    pause 0.1
    Obs.PathImg() + "effects/" + img2 + ".png"
    pause 0.1
    Obs.PathImg() + "effects/" + img3 + ".png"
    pause 0.1
    Obs.PathImg() + "effects/" + img4 + ".png"
    pause 0.1
    yzoom 1
    repeat

transform obs_effect_blossom(img, img2, img3):
    truecenter
    xzoom 1.3 yzoom 1.7 subpixel True
    contains:
        SnowBlossom(Obs.PathImg() + "effects/" + img + ".png", 10, 50, (75, 125), (1600, 1700))
    contains:
        SnowBlossom(Obs.PathImg() + "effects/" + img2 + ".png", 25, 50, (50, 100), (1500, 1600))
    contains:
        SnowBlossom(Obs.PathImg() + "effects/" + img3 + ".png", 150, 50, (25, 50), (1400, 1500))

transform obs_light_and_dust_contains(img):
    contains:
        Obs.PathImg() + "effects/" + img + ".png"
        obs_light_alpha_ease_repeat
    contains:
        "obs_dust5"
        obs_dust_alpha_ease_repeat
    contains:
        "obs_dust6"
        obs_dust_alpha_ease_repeat
    contains:
        "obs_dust9"
        obs_dust_alpha_ease_repeat
    contains:
        "obs_dust10"
        obs_dust_alpha_ease_repeat
    contains:
        "obs_dust11"
        obs_dust_alpha_ease_repeat
    contains:
        "obs_dust12"
        obs_dust_alpha_ease_repeat

transform obs_pause_dissolve_repeat(img, img2):
    Obs.PathImg() + "effects/" + img + ".png" with obs_dissolve
    pause 0.5
    Obs.PathImg() + "effects/" + img2 + ".png" with obs_dissolve
    pause 0.5
    repeat

transform obs_rotate_repeat_at_bg(img, img2, img3, x, y):
    contains:
        Obs.PathImg() + img
    contains:
        Obs.PathImg() + img2
        xalign x yalign y anchor (0.5, 0.5) rotate 0 rotate_pad True subpixel True
        linear 60.0 rotate 360
        repeat
    contains:
        Obs.PathImg() + img3

transform obs_matrix_color(img):
    ConditionSwitch(
        "obs_sprite_time == 'sunset'", im.MatrixColor(Obs.PathImg() + img, im.matrix.tint(0.94, 0.82, 1.0)),
        "obs_sprite_time == 'night'", im.MatrixColor(Obs.PathImg() + img, im.matrix.tint(0.63, 0.78, 0.82)),
        "obs_sprite_time == 'rain'", im.MatrixColor(Obs.PathImg() + img, im.matrix.tint(0.32, 0.54, 0.24)),
        True, Obs.PathImg() + "misc/else/obs_chair.png")

transform obs_phone_blinking_contains_color(color):
    contains:
        Obs.PathImg() + "misc/phone/obs_phone_ground" + color + ".png"
    contains:
        Obs.PathImg() + "misc/phone/obs_phone_mihalich" + color + ".png"
    contains:
        Obs.Brightness(Obs.PathImg() + "misc/phone/obs_phone_ground" + color + ".png", 0.3)
        ease 1.0 alpha 0.0
        ease 1.0 alpha 1.0
        repeat
    contains:
        Obs.Brightness(Obs.PathImg() + "misc/phone/obs_phone_mihalich" + color + ".png", 0.3)
        ease 1.0 alpha 0.0
        ease 1.0 alpha 1.0
        repeat
    contains:
        Obs.PathImg() + "misc/phone/obs_phone_layer" + color + ".png"

transform obs_seven_anim(name):
    Obs.PathImg() + name + "1.png"
    alpha 0.5
    pause 0.1
    Obs.PathImg() + name + "2.png"
    pause 0.1
    Obs.PathImg() + name + "3.png"
    pause 0.1
    Obs.PathImg() + name + "4.png"
    pause 0.1
    Obs.PathImg() + name + "5.png"
    pause 0.1
    Obs.PathImg() + name + "6.png"
    pause 0.1
    Obs.PathImg() + name + "7.png"
    pause 0.1
    repeat

transform obs_prologue_molotov_move:
    zoom 1.0 xalign 0.4 yoffset 550 rotate 0
    parallel:
        ease 2.0 zoom 4.0 rotate 600
    parallel:
        linear 1.0 yoffset -150
        linear 1.0 yoffset 750

transform obs_dspr_repeat_move(name):
    Obs.PathImg() + "effects/" + name + "1.png" with dspr
    pause 1.0
    Obs.PathImg() + "effects/" + name + "2.png" with dspr
    pause 1.0
    repeat

transform obs_xalign_repeat_move(name):
    Obs.PathImg() + "effects/" + name + ".png"
    xalign 1.0 yalign 1.0
    ease 0.7 xalign 0.9
    ease 0.7 xalign 1.0
    repeat

transform obs_shake_normal:
    pos (0, 0) zoom 1.05 align (0.5, 0.5) offset (960, 550) subpixel True
    linear 0.1 pos (-5, -5)
    linear 0.1 pos (5, 5)
    pos (0,0)
    linear 0.1 pos (0, -5)
    linear 0.1 pos (0, 5)
    repeat

transform obs_shake_normal_end:
    ease 0.5 pos (0, 0) subpixel True

transform obs_jerk_move(z, zz, r, y, yy):
    truecenter
    zoom z ypos 0.5 subpixel True
    parallel:
        ease 0.5 zoom zz rotate r
    parallel:
        ease 0.5 ypos y
        ease 0.5 ypos yy

transform obs_fall_on_the_table:
    truecenter
    subpixel True
    parallel:
        ease 0.5 zoom 2.5 rotate -9
    parallel:
        ease 0.5 ypos 0.4
        ease 0.5 ypos 0.0
        parallel:
            ease 0.5 zoom 2.5 rotate -9

transform obs_horror_fade(t=0.0):
    alpha 0.0 subpixel True
    t
    linear 25.0 alpha 1.0

transform obs_noise_fade(t=0.0):
    alpha 0.0 subpixel True
    t
    linear 10.0 alpha 0.2

transform obs_vignette_flicker(t=0.0):
    alpha 0.0 subpixel True
    t
    parallel:
        alpha 1.0
        linear 0.2 alpha 0.8
        0.1
        alpha 0.7
        linear 0.1 alpha 1.0
        alpha 0.0
        1.19
        repeat
    parallel:
        easeout 20.0 zoom 3.0

transform obs_master_flicker(t=0.0):
    truecenter
    subpixel True
    t
    parallel:
        zoom 1.05
        linear 0.2 zoom 1.04
        0.1
        zoom 1.035
        linear 0.1 zoom 1.05
        zoom 1.0
        1.19
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.6
        easeout_bounce 0.3 xalign 0.4
        repeat

transform obs_vignette_heartbeat:
    alpha 0.0 subpixel True
    parallel:
        alpha 1.0
        linear 0.25 alpha 0.7
        0.144
        alpha 0.7
        linear 0.269 alpha 1.0
        alpha 0.0
        1.479
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.5
        easeout_bounce 0.3 xalign 0.5

transform obs_master_heartbeat:
    truecenter
    subpixel True
    parallel:
        0.144
        zoom 1.0 + 0.07
        easein 0.25 zoom 1.0 + 0.04
        easeout 0.269 zoom 1.0 + 0.07
        zoom 1.0
        1.479
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.5 + 0.02
        easeout_bounce 0.3 xalign 0.5 - 0.02
        repeat

transform obs_boathouse_anim(name, x, xx, y):
    subpixel True
    contains:
        Obs.PathImg() + "bg/obs_ext_boathouse_" + name + ".png"
    contains:
        Obs.PathImg() + "objects/obs_ext_boathouse_" + name + "_train.png"
        xalign x yalign y
        linear 30.0 xalign xx yalign y
        pause 100
        repeat
    contains:
        Obs.PathImg() + "objects/obs_ext_boathouse_" + name + "_layer.png"

transform obs_main_menu_mi_fixed(name, name2):
    parallel:
        contains:
            Obs.PathImg() + "gui/main_menu/mi_" + name + ".png"
        contains:
            Obs.PathImg() + "gui/main_menu/mi_head1.png"
            pause 0.1
            Obs.PathImg() + "gui/main_menu/mi_head2.png"
            pause 0.1
            repeat
        contains:
            Obs.PathImg() + "gui/main_menu/mi_" + name2 + ".png"

transform obs_main_menu_mi_move(name):
    parallel:
        obs_main_menu_mi_fixed("torse", "torse")
        zoom 0.5 zoom 0.13 xpos 0.73 ypos 0.76 rotate 0
        ease 2.0 zoom 0.13 xpos 0.6 ypos 0.73 rotate 0
        pause 2
        obs_main_menu_mi_fixed("torse2", "hand")
        pause 4
        obs_main_menu_mi_fixed("torse", "torse")
        pause 4
        ease 2.0 zoom 0.5 zoom 0.13 xpos 0.73 ypos 0.76 rotate 0
        zoom 0.5 xpos 0.41 ypos 1.4 rotate 0
        ease 2.0 zoom 0.5 xpos 0.61 ypos 1.4 rotate 35
        obs_main_menu_mi_fixed("torse", "torse")
        pause 5
        obs_main_menu_mi_fixed("torse2", "hand")
        pause 2
        ease 2.0 zoom 0.5 xpos 0.41 ypos 1.4 rotate 0
        obs_main_menu_mi_fixed("torse", "torse")
        pause 1
        repeat

transform obs_main_menu_load_move(p, x, z, xal, yal):
    on show:
        xoffset x yoffset 0 xalign xal yalign yal zoom z
        pause p
        ease 1.0 xoffset 0 yoffset 0 xalign xal yalign yal zoom z
    on hide:
        xoffset 0 yoffset 0 xalign xal yalign yal zoom z
        ease 1.0 xoffset x yoffset 0 xalign xal yalign yal zoom z

transform obs_main_menu_preferences_move(p, x, xx, y, yy):
    on show:
        xoffset x yoffset y
        pause p
        ease 1.0 xoffset 0 yoffset 0
    on hide:
        xoffset 0 yoffset 0
        ease 1.0 xoffset xx yoffset yy

transform obs_main_menu_hand_anim:
    zoom 0.25 xalign -0.695 yalign 0.87 rotate -20 alpha 0.7
    parallel:
        ease 0.1 zoom 0.25 xalign -0.682 yalign 0.92 rotate 90 alpha 0.7
        ease 0.5 zoom 0.25 xalign -0.695 yalign 0.87 rotate -20 alpha 0.7
        ease 0.1 zoom 0.25 xalign -0.682 yalign 0.92 rotate 90 alpha 0.7
        ease 0.3 zoom 0.25 xalign -0.695 yalign 0.87 rotate -60 alpha 0.7
        pause 0.3
        repeat

transform obs_four_contains_xyzoom_effects(name):
    parallel:
        choice:
            Obs.PathImg() + "effects/" + name + "1.png"
        choice:
            Obs.PathImg() + "effects/" + name + "2.png"
        choice:
            Obs.PathImg() + "effects/" + name + "3.png"
        choice:
            Obs.PathImg() + "effects/" + name + "4.png"
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    parallel:
        parallel:
            choice:
                xzoom 1.0
            choice:
                xzoom -1.0
        parallel:
            choice:
                yzoom 1.0
            choice:
                yzoom -1.0
    pause 0.02
    repeat



transform obs_tcommon(e, x):
    subpixel True
    on show:
        alpha 0.0 xcenter x
        easein e alpha 1.0
    on replace:
        alpha 1.0
        parallel:
            easein e xcenter x
        parallel:
            easein 0.5

transform obs_normal(x=960):
    xcenter x alpha 1.00 subpixel True

transform obs_leftin(e, x):
    xcenter -450 subpixel True
    easein e xcenter x

transform obs_rightin(e, x):
    xcenter 2400 alpha 1.0 subpixel True
    easein e xcenter x

transform obs_hide(e, x):
    subpixel True
    on hide:
        easeout e xcenter x

transform obs_hop(x):
    xcenter x yoffset 0 alpha 1.0 subpixel True
    easein 0.1 yoffset -40
    easeout 0.1 yoffset 0

transform obs_dip(x=960, y=0):
    xcenter x yoffset y alpha 1.0 subpixel True
    easein 0.25 yoffset y+50
    easeout 0.25 yoffset y

transform obs_sink(x):
    xcenter x yoffset 0 alpha 1.0 subpixel True
    easein 0.5 yoffset 30

transform obs_sprite_sit:
    zoom 1.05 yalign 0.2 subpixel True
    parallel:
        ease 1.0 yalign -0.1
    parallel:
        ease 0.75 zoom 1.1 yalign 0.2
        ease 0.5 zoom 1.05 yalign -0.1

transform obs_sprite_is_sitting:
    xanchor 0.5 yanchor 0.0 ypos 0.22 subpixel True



transform obs_rnhide:
    obs_hide(1.0, 2400)
transform obs_rfhide:
    obs_hide(0.5, 2400)
transform obs_rshide:
    obs_hide(1.5, 2400)
transform obs_rsshide:
    obs_hide(2.0, 2400)
transform obs_lnhide:
    obs_hide(1.0, -450)
transform obs_lfhide:
    obs_hide(0.5, -450)
transform obs_lshide:
    obs_hide(1.5, -450)
transform obs_lsshide:
    obs_hide(2.0, -450)

transform obs_i51:
    obs_normal(200)
transform obs_i52:
    obs_normal(570)
transform obs_i53:
    obs_normal(960)
transform obs_i54:
    obs_normal(1350)
transform obs_i55:
    obs_normal(1720)
transform obs_i41:
    obs_normal(300)
transform obs_i42:
    obs_normal(740)
transform obs_i43:
    obs_normal(1180)
transform obs_i44:
    obs_normal(1620)
transform obs_i31:
    obs_normal(360)
transform obs_i32:
    obs_normal(960)
transform obs_i33:
    obs_normal(1560)
transform obs_i21:
    obs_normal(600)
transform obs_i22:
    obs_normal(1320)
transform obs_i11:
    obs_normal(960)

transform obs_h51:
    obs_hop(200)
transform obs_h52:
    obs_hop(570)
transform obs_h53:
    obs_hop(960)
transform obs_h54:
    obs_hop(1350)
transform obs_h55:
    obs_hop(1720)
transform obs_h41:
    obs_hop(300)
transform obs_h42:
    obs_hop(740)
transform obs_h43:
    obs_hop(1180)
transform obs_h44:
    obs_hop(1620)
transform obs_h31:
    obs_hop(360)
transform obs_h32:
    obs_hop(960)
transform obs_h33:
    obs_hop(1560)
transform obs_h21:
    obs_hop(600)
transform obs_h22:
    obs_hop(1320)
transform obs_h11:
    obs_hop(960)

transform obs_d51:
    obs_dip(200)
transform obs_d52:
    obs_dip(570)
transform obs_d53:
    obs_dip(960)
transform obs_d54:
    obs_dip(1350)
transform obs_d55:
    obs_dip(1720)
transform obs_d41:
    obs_dip(300)
transform obs_d42:
    obs_dip(740)
transform obs_d43:
    obs_dip(1180)
transform obs_d44:
    obs_dip(1620)
transform obs_d31:
    obs_dip(360)
transform obs_d32:
    obs_dip(960)
transform obs_d33:
    obs_dip(1560)
transform obs_d21:
    obs_dip(600)
transform obs_d22:
    obs_dip(1320)
transform obs_d11:
    obs_dip(960)

transform obs_s51:
    obs_sink(200)
transform obs_s52:
    obs_sink(570)
transform obs_s53:
    obs_sink(960)
transform obs_s54:
    obs_sink(1350)
transform obs_s55:
    obs_sink(1720)
transform obs_s41:
    obs_sink(300)
transform obs_s42:
    obs_sink(740)
transform obs_s43:
    obs_sink(1180)
transform obs_s44:
    obs_sink(1620)
transform obs_s31:
    obs_sink(360)
transform obs_s32:
    obs_sink(960)
transform obs_s33:
    obs_sink(1560)
transform obs_s21:
    obs_sink(600)
transform obs_s22:
    obs_sink(1320)
transform obs_s11:
    obs_sink(960)

transform obs_ln51:
    obs_leftin(1.0, 200)
transform obs_ln52:
    obs_leftin(1.0, 570)
transform obs_ln53:
    obs_leftin(1.0, 960)
transform obs_ln54:
    obs_leftin(1.0, 1350)
transform obs_ln55:
    obs_leftin(1.0, 1720)
transform obs_ln41:
    obs_leftin(1.0, 300)
transform obs_ln42:
    obs_leftin(1.0, 740)
transform obs_ln43:
    obs_leftin(1.0, 1180)
transform obs_ln44:
    obs_leftin(1.0, 1620)
transform obs_ln31:
    obs_leftin(1.0, 360)
transform obs_ln32:
    obs_leftin(1.0, 960)
transform obs_ln33:
    obs_leftin(1.0, 1560)
transform obs_ln21:
    obs_leftin(1.0, 600)
transform obs_ln22:
    obs_leftin(1.0, 1320)
transform obs_ln11:
    obs_leftin(1.0, 960)

transform obs_lf51:
    obs_leftin(0.5, 200)
transform obs_lf52:
    obs_leftin(0.5, 570)
transform obs_lf53:
    obs_leftin(0.5, 960)
transform obs_lf54:
    obs_leftin(0.5, 1350)
transform obs_lf55:
    obs_leftin(0.5, 1720)
transform obs_lf41:
    obs_leftin(0.5, 300)
transform obs_lf42:
    obs_leftin(0.5, 740)
transform obs_lf43:
    obs_leftin(0.5, 1180)
transform obs_lf44:
    obs_leftin(0.5, 1620)
transform obs_lf31:
    obs_leftin(0.5, 360)
transform obs_lf32:
    obs_leftin(0.5, 960)
transform obs_lf33:
    obs_leftin(0.5, 1560)
transform obs_lf21:
    obs_leftin(0.5, 600)
transform obs_lf22:
    obs_leftin(0.5, 1320)
transform obs_lf11:
    obs_leftin(0.5, 960)

transform obs_ls51:
    obs_leftin(1.5, 200)
transform obs_ls52:
    obs_leftin(1.5, 570)
transform obs_ls53:
    obs_leftin(1.5, 960)
transform obs_ls54:
    obs_leftin(1.5, 1350)
transform obs_ls55:
    obs_leftin(1.5, 1720)
transform obs_ls41:
    obs_leftin(1.5, 300)
transform obs_ls42:
    obs_leftin(1.5, 740)
transform obs_ls43:
    obs_leftin(1.5, 1180)
transform obs_ls44:
    obs_leftin(1.5, 1620)
transform obs_ls31:
    obs_leftin(1.5, 360)
transform obs_ls32:
    obs_leftin(1.5, 960)
transform obs_ls33:
    obs_leftin(1.5, 1560)
transform obs_ls21:
    obs_leftin(1.5, 600)
transform obs_ls22:
    obs_leftin(1.5, 1320)
transform obs_ls11:
    obs_leftin(1.5, 960)

transform obs_lss51:
    obs_leftin(2.0, 200)
transform obs_lss52:
    obs_leftin(2.0, 570)
transform obs_lss53:
    obs_leftin(2.0, 960)
transform obs_lss54:
    obs_leftin(2.0, 1350)
transform obs_lss55:
    obs_leftin(2.0, 1720)
transform obs_lss41:
    obs_leftin(2.0, 300)
transform obs_lss42:
    obs_leftin(2.0, 740)
transform obs_lss43:
    obs_leftin(2.0, 1180)
transform obs_lss44:
    obs_leftin(2.0, 1620)
transform obs_lss31:
    obs_leftin(2.0, 360)
transform obs_lss32:
    obs_leftin(2.0, 960)
transform obs_lss33:
    obs_leftin(2.0, 1560)
transform obs_lss21:
    obs_leftin(2.0, 600)
transform obs_lss22:
    obs_leftin(2.0, 1320)
transform obs_lss11:
    obs_leftin(2.0, 960)

transform obs_rn51:
    obs_rightin(1.0, 200)
transform obs_rn52:
    obs_rightin(1.0, 570)
transform obs_rn53:
    obs_rightin(1.0, 960)
transform obs_rn54:
    obs_rightin(1.0, 1350)
transform obs_rn55:
    obs_rightin(1.0, 1720)
transform obs_rn41:
    obs_rightin(1.0, 300)
transform obs_rn42:
    obs_rightin(1.0, 740)
transform obs_rn43:
    obs_rightin(1.0, 1180)
transform obs_rn44:
    obs_rightin(1.0, 1620)
transform obs_rn31:
    obs_rightin(1.0, 360)
transform obs_rn32:
    obs_rightin(1.0, 960)
transform obs_rn33:
    obs_rightin(1.0, 1560)
transform obs_rn21:
    obs_rightin(1.0, 600)
transform obs_rn22:
    obs_rightin(1.0, 1320)
transform obs_rn11:
    obs_rightin(1.0, 960)

transform obs_rf51:
    obs_rightin(0.5, 200)
transform obs_rf52:
    obs_rightin(0.5, 570)
transform obs_rf53:
    obs_rightin(0.5, 960)
transform obs_rf54:
    obs_rightin(0.5, 1350)
transform obs_rf55:
    obs_rightin(0.5, 1720)
transform obs_rf41:
    obs_rightin(0.5, 300)
transform obs_rf42:
    obs_rightin(0.5, 740)
transform obs_rf43:
    obs_rightin(0.5, 1180)
transform obs_rf44:
    obs_rightin(0.5, 1620)
transform obs_rf31:
    obs_rightin(0.5, 360)
transform obs_rf32:
    obs_rightin(0.5, 960)
transform obs_rf33:
    obs_rightin(0.5, 1560)
transform obs_rf21:
    obs_rightin(0.5, 600)
transform obs_rf22:
    obs_rightin(0.5, 1320)
transform obs_rf11:
    obs_rightin(0.5, 960)

transform obs_rs51:
    obs_rightin(1.5, 200)
transform obs_rs52:
    obs_rightin(1.5, 570)
transform obs_rs53:
    obs_rightin(1.5, 960)
transform obs_rs54:
    obs_rightin(1.5, 1350)
transform obs_rs55:
    obs_rightin(1.5, 1720)
transform obs_rs41:
    obs_rightin(1.5, 300)
transform obs_rs42:
    obs_rightin(1.5, 740)
transform obs_rs43:
    obs_rightin(1.5, 1180)
transform obs_rs44:
    obs_rightin(1.5, 1620)
transform obs_rs31:
    obs_rightin(1.5, 360)
transform obs_rs32:
    obs_rightin(1.5, 960)
transform obs_rs33:
    obs_rightin(1.5, 1560)
transform obs_rs21:
    obs_rightin(1.5, 600)
transform obs_rs22:
    obs_rightin(1.5, 1320)
transform obs_rs11:
    obs_rightin(1.5, 960)

transform obs_rss51:
    obs_rightin(2.0, 200)
transform obs_rss52:
    obs_rightin(2.0, 570)
transform obs_rss53:
    obs_rightin(2.0, 960)
transform obs_rss54:
    obs_rightin(2.0, 1350)
transform obs_rss55:
    obs_rightin(2.0, 1720)
transform obs_rss41:
    obs_rightin(2.0, 300)
transform obs_rss42:
    obs_rightin(2.0, 740)
transform obs_rss43:
    obs_rightin(2.0, 1180)
transform obs_rss44:
    obs_rightin(2.0, 1620)
transform obs_rss31:
    obs_rightin(2.0, 360)
transform obs_rss32:
    obs_rightin(2.0, 960)
transform obs_rss33:
    obs_rightin(2.0, 1560)
transform obs_rss21:
    obs_rightin(2.0, 600)
transform obs_rss22:
    obs_rightin(2.0, 1320)
transform obs_rss11:
    obs_rightin(2.0, 960)

transform obs_tn51:
    obs_rightin(1.0, 200)
transform obs_tn52:
    obs_rightin(1.0, 570)
transform obs_tn53:
    obs_rightin(1.0, 960)
transform obs_tn54:
    obs_rightin(1.0, 1350)
transform obs_tn55:
    obs_rightin(1.0, 1720)
transform obs_tn41:
    obs_tcommon(1.0, 300)
transform obs_tn42:
    obs_tcommon(1.0, 740)
transform obs_tn43:
    obs_tcommon(1.0, 1180)
transform obs_tn44:
    obs_tcommon(1.0, 1620)
transform obs_tn31:
    obs_tcommon(1.0, 360)
transform obs_tn32:
    obs_tcommon(1.0, 960)
transform obs_tn33:
    obs_tcommon(1.0, 1560)
transform obs_tn21:
    obs_tcommon(1.0, 600)
transform obs_tn22:
    obs_tcommon(1.0, 1320)
transform obs_tn11:
    obs_tcommon(1.0, 960)

transform obs_tf51:
    obs_tcommon(0.5, 200)
transform obs_tf52:
    obs_tcommon(0.5, 570)
transform obs_tf53:
    obs_tcommon(0.5, 960)
transform obs_tf54:
    obs_tcommon(0.5, 1350)
transform obs_tf55:
    obs_tcommon(0.5, 1720)
transform obs_tf41:
    obs_tcommon(0.5, 300)
transform obs_tf42:
    obs_tcommon(0.5, 740)
transform obs_tf43:
    obs_tcommon(0.5, 1180)
transform obs_tf44:
    obs_tcommon(0.5, 1620)
transform obs_tf31:
    obs_tcommon(0.5, 360)
transform obs_tf32:
    obs_tcommon(0.5, 960)
transform obs_tf33:
    obs_tcommon(0.5, 1560)
transform obs_tf21:
    obs_tcommon(0.5, 600)
transform obs_tf22:
    obs_tcommon(0.5, 1320)
transform obs_tf11:
    obs_tcommon(0.5, 960)

transform obs_ts51:
    obs_tcommon(1.5, 200)
transform obs_ts52:
    obs_tcommon(1.5, 570)
transform obs_ts53:
    obs_tcommon(1.5, 960)
transform obs_ts54:
    obs_tcommon(1.5, 1350)
transform obs_ts55:
    obs_tcommon(1.5, 1720)
transform obs_ts41:
    obs_tcommon(1.5, 300)
transform obs_ts42:
    obs_tcommon(1.5, 740)
transform obs_ts43:
    obs_tcommon(1.5, 1180)
transform obs_ts44:
    obs_tcommon(1.5, 1620)
transform obs_ts31:
    obs_tcommon(1.5, 360)
transform obs_ts32:
    obs_tcommon(1.5, 960)
transform obs_ts33:
    obs_tcommon(1.5, 1560)
transform obs_ts21:
    obs_tcommon(1.5, 600)
transform obs_ts22:
    obs_tcommon(1.5, 1320)
transform obs_ts11:
    obs_tcommon(1.5, 960)

transform obs_tss51:
    obs_tcommon(2.0, 200)
transform obs_tss52:
    obs_tcommon(2.0, 570)
transform obs_tss53:
    obs_tcommon(2.0, 960)
transform obs_tss54:
    obs_tcommon(2.0, 1350)
transform obs_tss55:
    obs_tcommon(2.0, 1720)
transform obs_tss41:
    obs_tcommon(2.0, 300)
transform obs_tss42:
    obs_tcommon(2.0, 740)
transform obs_tss43:
    obs_tcommon(2.0, 1180)
transform obs_tss44:
    obs_tcommon(2.0, 1620)
transform obs_tss31:
    obs_tcommon(2.0, 360)
transform obs_tss32:
    obs_tcommon(2.0, 960)
transform obs_tss33:
    obs_tcommon(2.0, 1560)
transform obs_tss21:
    obs_tcommon(2.0, 600)
transform obs_tss22:
    obs_tcommon(2.0, 1320)
transform obs_tss11:
    obs_tcommon(2.0, 960)



transform obs_loading_bg_move:
    xalign 0.0 alpha 0.0 subpixel True
    parallel:
        ease 3.0 alpha 1.0
    parallel:
        ease 15.0 xalign 1.0

transform obs_main_menu_buttons_move:
    xoffset -800 subpixel True
    ease 1.0 xoffset 0
    on hide:
        xoffset 0
        ease 1.0 xoffset -800

transform obs_msk_button_move(i=1):
    xpos -1000 * i subpixel True
    ease 1.0 xpos 0
    on hide:
        xpos 0
        ease 1.0 xpos -1000 * i

transform obs_art_button_move(i=1):
    xpos 1000 * i subpixel True
    ease 1.0 xpos 0
    on hide:
        xpos 0
        ease 1.0 xpos 1000 * i

transform obs_return_button_move:
    ypos 1000 subpixel True
    ease 1.0 ypos 0
    on hide:
        xpos 0
        ease 1.0 ypos 1000

transform obs_menu_move(z=1.0, y=0.5, yy=0):
    subpixel True
    on show:
        zoom z xalign 0.5 yalign y yoffset yy-100 alpha 0.0
        ease 0.5 zoom z xalign 0.5 yalign y yoffset yy alpha 1.0
    on hide:
        zoom z xalign 0.5 yalign y yoffset yy alpha 1.0
        ease 0.5 zoom z xalign 0.5 yalign y yoffset yy-100 alpha 0.0
    on replace:
        zoom z

transform obs_main_menu_move(z=1.0, y=0.5, yy=0, x=0.5):
    subpixel True
    zoom z xalign 0.5 yalign y yoffset yy alpha 1.0
    on show:
        zoom z xalign x yalign y yoffset yy-100 alpha 0.0
        ease 0.5 zoom z xalign x yalign y yoffset yy alpha 1.0
    on hide:
        zoom z xalign x yalign y yoffset yy alpha 1.0
        ease 0.5 zoom z xalign x yalign y yoffset yy-100 alpha 0.0
    on replace:
        zoom z

transform obs_arrow_right_anim:
    xoffset 200 alpha 0 subpixel True
    ease 1.0 xoffset 0 alpha 1
    on hide:
        ease 1.0 xoffset 200 alpha 0
    on idle:
        ease 0.5 xoffset 0 alpha 1
    on hover:
        ease 0.8 xoffset 50
        ease 0.8 xoffset 0
        repeat

transform obs_arrow_left_anim:
    xoffset -200 alpha 0 subpixel True
    ease 1.0 xoffset 0 alpha 1
    on hide:
        ease 1.0 xoffset -200 alpha 0
    on idle:
        ease 0.5 xoffset 0 alpha 1
    on hover:
        ease 0.8 xoffset -50
        ease 0.8 xoffset 0
        repeat

transform obs_interface_up_anim:
    yoffset -300 alpha 0.0 subpixel True
    easein 0.6 yoffset 0 alpha 1.0
    on idle:
        zoom 1.0
    on hide:
        yoffset 0 alpha 1.0
        easein 0.6 yoffset -250 alpha 0.0

transform obs_quest_name_move:
    xanchor 0.0 subpixel True
    on show:
        xpos -0.5 ypos 0.03
        ease 1.0 xpos 0.02 ypos 0.03

transform obs_quest_objectives_move_in:
    xpos -0.5 subpixel True
    ease 1.0 xpos 0.04

transform obs_quest_objectives_move_out:
    xpos 0.04 subpixel True

transform obs_ctc_animation_for_time_of_day(x, y):
    ConditionSwitch(
        "obs_timeofday == 'sunset'", Animation(Obs.PathImg() + "misc/ctc/ctc_orange01.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_orange02.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_orange03.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_orange04.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_orange05.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_orange06.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_orange07.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_orange08.png", 0.15, xpos=x, ypos=y, xanchor=1.0, yanchor=1.0),
        "obs_timeofday == 'rain' or obs_timeofday == 'prologue'", Animation(Obs.PathImg() + "misc/ctc/ctc_gray01.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_gray02.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_gray03.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_gray04.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_gray05.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_gray06.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_gray07.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_gray08.png", 0.15, xpos=x, ypos=y, xanchor=1.0, yanchor=1.0),
        "True", Animation(Obs.PathImg() + "misc/ctc/ctc_day01.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_day02.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_day03.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_day04.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_day05.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_day06.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_day07.png", 0.15, Obs.PathImg() + "misc/ctc/ctc_day08.png", 0.15, xpos=x, ypos=y, xanchor=1.0, yanchor=1.0))

transform obs_text_alpha_in(l):
    alpha 0.0
    linear l alpha 1.0

transform obs_text_alpha_out(l):
    alpha 1.0
    linear l alpha 0.0

transform obs_message_move:
    yoffset 0 pos (0.5, 0.9) xanchor 0.5 alpha 0 subpixel True
    ease 0.2 alpha 1
    ease 0.1 yoffset 20
    ease 0.1 yoffset 0
    pause 2
    ease 1.0 alpha 0

transform obs_new_item_move:
    parallel:
        xpos 0.02 ypos 0.45 zoom 0.9
        ease 0.3 ypos 0.55
        ease 0.3 ypos 0.5
    parallel:
        alpha 0.0
        ease 1.0 alpha 1.0
        pause 3.0
        ease 1.0 alpha 0.0

transform obs_full_rotate_repeat(l, z, x, y):
    parallel:
        zoom z xalign x yalign y rotate_pad True rotate 0
        linear l rotate 360
        repeat

transform obs_show_hide_alpha(e):
    on show:
        alpha 0.0
        ease e alpha 1.0
    on hide:
        alpha 1.0
        ease e alpha 0.0

transform obs_clicked_text_move:
    xanchor 0.0 subpixel True
    on show:
        xpos -0.8 ypos 0.03
        ease 1.0 xpos 0.07 ypos 0.03
        ease 0.5 xpos 0.02 ypos 0.03
    on hide:
        xpos 0.02 ypos 0.03
        ease 0.5 xpos 0.07 ypos 0.03
        ease 1.0 xpos -0.8 ypos 0.03



transform obs_hidescreens(e):
    xpos 0.0 ypos 0.0 alpha 1.0 subpixel True
    ease e xpos 0.0 ypos 0.1 alpha 0.0

transform obs_showscreens(e):
    ypos 0.1 alpha 0.0 subpixel True
    ease e ypos 0.0 alpha 1.0

transform obs_not_screens:
    xpos 0.0 ypos 0.22 alpha 0.0 subpixel True

transform obs_screen_normal(l=2.0):
    linear l xalign 0.5 yalign 0.5 zoom 1.0 subpixel True

transform obs_hide_nvl(e=1.0):
    xpos 0.0 ypos 0.0 alpha 1.0 subpixel True
    ease e xpos 0.0 ypos 0.2 alpha 0.0

transform obs_show_nvl(e=0.5):
    ypos 0.2 alpha 0.0 subpixel True
    ease e ypos 0.0 alpha 1.0



transform obs_sit:
    ypos 0.22 subpixel True

transform obs_sit_down:
    subpixel True
    parallel:
        ease 1.0 ypos 0.22
    parallel:
        ease 0.75 zoom 1.05
        ease 0.5 zoom 1.0

transform obs_sit_down2:
    subpixel True
    parallel:
        ease 1.0 ypos 0.15
    parallel:
        ease 0.75 zoom 1.05
        ease 0.5 zoom 1.0

transform obs_get_up:
    subpixel True
    parallel:
        ease 1.0 ypos 0.0
    parallel:
        ease 0.75 zoom 1.05
        ease 0.5 zoom 1.0

transform obs_sprite_sit_dining(x):
    ease 0.75 zoom 1.1 xoffset x yoffset -100 rotate 2 subpixel True
    ease 0.5 zoom 1.0 yoffset -150 rotate 0



transform obs_chair_move_in:
    yanchor 0.0 subpixel True
    ypos 0.1
    zoom 0.95
    ease 0.75 ypos 0.0 zoom 1.0

transform obs_chair_move_out:
    yanchor 0.0 subpixel True
    ease 0.75 ypos 0.1 zoom 0.95



transform obs_run_anim:
    subpixel True
    parallel:
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
        ease 0.16 zoom 1.04 xpos 0.5 ypos 0.49
    parallel:
        ease 0.16 xpos 0.5 ypos 0.49
        ease 0.16 xpos 0.48 ypos 0.51
        ease 0.16 xpos 0.5 ypos 0.49
        ease 0.16 xpos 0.52 ypos 0.51
        repeat

transform obs_run_anim2:
    subpixel True
    parallel:
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
        ease 0.12 zoom 1.1 xpos 0.5 ypos 0.49
    parallel:
        ease 0.12 xpos 0.5 ypos 0.48
        ease 0.12 xpos 0.47 ypos 0.52
        ease 0.12 xpos 0.5 ypos 0.48
        ease 0.12 xpos 0.53 ypos 0.52
        repeat

transform obs_walk_anim(rep=None):
    subpixel True
    parallel:
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
        ease 0.5 zoom 1.04 xpos 0.5 ypos 0.49
    parallel:
        ease 0.5 xpos 0.5 ypos 0.492
        ease 0.5 xpos 0.484 ypos 0.508
        ease 0.5 xpos 0.5 ypos 0.492
        ease 0.5 xpos 0.516 ypos 0.508
        repeat rep

transform obs_run_anim_end:
    ease 0.2 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 subpixel True



transform obs_bg_zoom_e(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, a=1.0, aa=1.0):
    zoom z xalign x yalign y alpha a subpixel True
    ease t zoom zz xalign xx yalign yy alpha aa

transform obs_bg_zoom_e2(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5):
    zoom z xalign x yalign y subpixel True
    ease t zoom zz xalign xx yalign yy
    ease tt zoom zzz xalign xxx yalign yyy

transform obs_bg_zoom_e3(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5):
    zoom z xalign x yalign y subpixel True
    ease t zoom zz xalign xx yalign yy
    ease tt zoom zzz xalign xxx yalign yyy
    ease ttt zoom zzzz xalign xxxx yalign yyyy

transform obs_bg_zoom_e4(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5, zzzzz=1.0, tttt=0.0, xxxxx=0.5, yyyyy=0.5):
    zoom z xalign x yalign y subpixel True
    ease t zoom zz xalign xx yalign yy
    ease tt zoom zzz xalign xxx yalign yyy
    ease ttt zoom zzzz xalign xxxx yalign yyyy
    ease tttt zoom zzzzz xalign xxxxx yalign yyyyy

transform obs_bg_zoom_e5(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5, zzzzz=1.0, tttt=0.0, xxxxx=0.5, yyyyy=0.5, zzzzzz=1.0, ttttt=0.0, xxxxxx=0.5, yyyyyy=0.5):
    zoom z xalign x yalign y subpixel True
    ease t zoom zz xalign xx yalign yy
    ease tt zoom zzz xalign xxx yalign yyy
    ease ttt zoom zzzz xalign xxxx yalign yyyy
    ease tttt zoom zzzzz xalign xxxxx yalign yyyyy
    ease ttttt zoom zzzzzz xalign xxxxxx yalign yyyyyy



transform obs_bg_zoom_to_e(z=1.0, t=0.0, x=0.5, y=0.5, a=1.0):
    ease t zoom z xalign x yalign y alpha a subpixel True

transform obs_bg_zoom_to_e2(z=1.0, t=0.0, x=0.5, y=0.5, zz=1.0, tt=0.0, xx=0.5, yy=0.5):
    ease t zoom z xalign x yalign y subpixel True
    ease tt zoom zz xalign xx yalign yy

transform obs_bg_zoom_to_e3(z=1.0, t=0.0, x=0.5, y=0.5, zz=1.0, tt=0.0, xx=0.5, yy=0.5, zzz=1.0, ttt=0.0, xxx=0.5, yyy=0.5):
    ease t zoom z xalign x yalign y subpixel True
    ease tt zoom zz xalign xx yalign yy
    ease ttt zoom zzz xalign xxx yalign yyy



transform obs_bg_zoom_l(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5):
    zoom z xalign x yalign y subpixel True
    linear t zoom zz xalign xx yalign yy

transform obs_bg_zoom_l2(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5):
    zoom z xalign x yalign y subpixel True
    linear t zoom zz xalign xx yalign yy
    linear tt zoom zzz xalign xxx yalign yyy

transform obs_bg_zoom_l3(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5):
    zoom z xalign x yalign y subpixel True
    linear t zoom zz xalign xx yalign yy
    linear tt zoom zzz xalign xxx yalign yyy
    linear ttt zoom zzzz xalign xxxx yalign yyyy

transform obs_bg_zoom_l4(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5, zzzzz=1.0, tttt=0.0, xxxxx=0.5, yyyyy=0.5):
    zoom z xalign x yalign y subpixel True
    linear t zoom zz xalign xx yalign yy
    linear tt zoom zzz xalign xxx yalign yyy
    linear ttt zoom zzzz xalign xxxx yalign yyyy
    linear tttt zoom zzzzz xalign xxxxx yalign yyyyy

transform obs_bg_zoom_l5(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5, zzzzz=1.0, tttt=0.0, xxxxx=0.5, yyyyy=0.5, zzzzzz=1.0, ttttt=0.0, xxxxxx=0.5, yyyyyy=0.5):
    zoom z xalign x yalign y subpixel True
    linear t zoom zz xalign xx yalign yy
    linear tt zoom zzz xalign xxx yalign yyy
    linear ttt zoom zzzz xalign xxxx yalign yyyy
    linear tttt zoom zzzzz xalign xxxxx yalign yyyyy
    linear ttttt zoom zzzzzz xalign xxxxxx yalign yyyyyy



transform obs_bg_zoom_to_l(z=1.0, t=0.0, x=0.5, y=0.5, a=1.0):
    linear t zoom z xalign x yalign y alpha a subpixel True



transform obs_bg_zoom_rotate_e(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, r=0.0, rr=0.0):
    zoom z xalign x yalign y rotate r subpixel True
    ease t zoom zz xalign xx yalign yy rotate rr

transform obs_bg_zoom_rotate_e2(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, r=0.0, rr=0.0, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, rrr=0.0):
    zoom z xalign x yalign y rotate r subpixel True
    ease t zoom zz xalign xx yalign yy rotate rr
    ease tt zoom zzz xalign xxx yalign yyy rotate rrr

transform obs_bg_zoom_rotate_e3(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, r=0.0, rr=0.0, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, rrr=0.0, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5, rrrr=0.0):
    zoom z xalign x yalign y rotate r subpixel True
    ease t zoom zz xalign xx yalign yy rotate rr
    ease tt zoom zzz xalign xxx yalign yyy rotate rrr
    ease ttt zoom zzzz xalign xxxx yalign yyyy rotate rrrr

transform obs_bg_zoom_rotate_e4(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, r=0.0, rr=0.0, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, rrr=0.0, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5, rrrr=0.0, zzzzz=1.0, tttt=0.0, xxxxx=0.5, yyyyy=0.5, rrrrr=0.0):
    zoom z xalign x yalign y rotate r subpixel True
    ease t zoom zz xalign xx yalign yy rotate rr
    ease tt zoom zzz xalign xxx yalign yyy rotate rrr
    ease ttt zoom zzzz xalign xxxx yalign yyyy rotate rrrr
    ease tttt zoom zzzzz xalign xxxxx yalign yyyyy rotate rrrrr

transform obs_bg_zoom_rotate_e5(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, r=0.0, rr=0.0, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, rrr=0.0, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5, rrrr=0.0, zzzzz=1.0, tttt=0.0, xxxxx=0.5, yyyyy=0.5, rrrrr=0.0, zzzzzz=1.0, ttttt=0.0, xxxxxx=0.5, yyyyyy=0.5, rrrrrr=0.0):
    zoom z xalign x yalign y rotate r subpixel True
    ease t zoom zz xalign xx yalign yy rotate rr
    ease tt zoom zzz xalign xxx yalign yyy rotate rrr
    ease ttt zoom zzzz xalign xxxx yalign yyyy rotate rrrr
    ease tttt zoom zzzzz xalign xxxxx yalign yyyyy rotate rrrrr
    ease ttttt zoom zzzzzz xalign xxxxxx yalign yyyyyy rotate rrrrrr



transform obs_bg_zoom_rotate_to_e(z=1.0, t=0.0, x=0.5, y=0.5, r=0.0):
    ease t zoom z xalign x yalign y rotate r subpixel True



transform obs_bg_zoom_rotate_l(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, r=0.0, rr=0.0):
    zoom z xalign x yalign y rotate r subpixel True
    linear t zoom zz xalign xx yalign yy rotate rr

transform obs_bg_zoom_rotate_l2(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, r=0.0, rr=0.0, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, rrr=0.0):
    zoom z xalign x yalign y rotate r subpixel True
    linear t zoom zz xalign xx yalign yy rotate rr
    linear tt zoom zzz xalign xxx yalign yyy rotate rrr

transform obs_bg_zoom_rotate_l3(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, r=0.0, rr=0.0, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, rrr=0.0, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5, rrrr=0.0):
    zoom z xalign x yalign y rotate r subpixel True
    linear t zoom zz xalign xx yalign yy rotate rr
    linear tt zoom zzz xalign xxx yalign yyy rotate rrr
    linear ttt zoom zzzz xalign xxxx yalign yyyy rotate rrrr

transform obs_bg_zoom_rotate_l4(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, r=0.0, rr=0.0, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, rrr=0.0, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5, rrrr=0.0, zzzzz=1.0, tttt=0.0, xxxxx=0.5, yyyyy=0.5, rrrrr=0.0):
    zoom z xalign x yalign y rotate r subpixel True
    linear t zoom zz xalign xx yalign yy rotate rr
    linear tt zoom zzz xalign xxx yalign yyy rotate rrr
    linear ttt zoom zzzz xalign xxxx yalign yyyy rotate rrrr
    linear tttt zoom zzzzz xalign xxxxx yalign yyyyy rotate rrrrr

transform obs_bg_zoom_rotate_l5(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, r=0.0, rr=0.0, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, rrr=0.0, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5, rrrr=0.0, zzzzz=1.0, tttt=0.0, xxxxx=0.5, yyyyy=0.5, rrrrr=0.0, zzzzzz=1.0, ttttt=0.0, xxxxxx=0.5, yyyyyy=0.5, rrrrrr=0.0):
    zoom z xalign x yalign y rotate r subpixel True
    linear t zoom zz xalign xx yalign yy rotate rr
    linear tt zoom zzz xalign xxx yalign yyy rotate rrr
    linear ttt zoom zzzz xalign xxxx yalign yyyy rotate rrrr
    linear tttt zoom zzzzz xalign xxxxx yalign yyyyy rotate rrrrr
    linear ttttt zoom zzzzzz xalign xxxxxx yalign yyyyyy rotate rrrrrr



transform obs_bg_zoom_rotate_to_l(z=1.0, t=0.0, x=0.5, y=0.5, r=0.0):
    linear t zoom z xalign x yalign y rotate r subpixel True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
