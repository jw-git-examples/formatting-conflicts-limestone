# test whether calculated colors will have coords within sRGB gamut
name = "Impossible colors"
background = (10, 0, 0)
foreground = (80, 0, 0)
shades = {
    "too_bright": 1.6,
}
colors = {
    "blue":   (65, -15, -60),
}
color_variants = {
    "too_bright":   (1.8, 1),
    "too_saturated": (1, 2.1),
}

