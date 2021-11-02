dark_green = fill = color(r=26, g=124, b=39)
dark_pink = color(r=233, g=36, b=89)
orange = color(r=255, g=153, b=51)
yellow = color(r=255, g=255, b=0)
white = fill1 = color(r=255, g=255, b=255)


outer_petals = rectangle(w=212.5, h=212.5, fill=dark_pink,
                         stroke='none') | repeat(8, rotate(22.5))
show(outer_petals)

mid_petals = rectangle(w=182, h=182, stroke='none',
                       fill=orange) | rotate(11.25) | repeat(8, rotate(22.5))
show(mid_petals)

inner_petals = rectangle(w=155, h=155, stroke='none',
                         fill=yellow) | repeat(8, rotate(22.5))
show(inner_petals)

p1 = point(x=104, y=7)
p2 = point(x=104, y=-7)
p3 = point(x=111, y=-12)
p4 = point(x=111, y=12)
inner_circle = circle(r=100, fill=dark_green, stroke=dark_pink, stroke_width=10)
show(inner_circle)

inner_circle = circle(r=50, fill=dark_green, stroke=dark_pink, stroke_width=10)
show(inner_circle)
inner_sqr_rot_a = rectangle(w=35.36, h=35.36, x=18,
                            y=18, fill=orange, stroke='none')
inner_sqr_rot_b = rectangle(w=35.36, h=35.36, x=18, y=18,
                            fill=yellow, stroke='none') | rotate(45)

inner_sqr_rot = combine(
    [inner_sqr_rot_a, inner_sqr_rot_b]) | repeat(4, rotate(90))
show(inner_sqr_rot)

p1 = point(x=0, y=0)
p2 = point(x=35.36, y=35.36)
p3 = point(x=35.36, y=0)

inner_sqr_rot_cover = polygon([p1, p2, p3], fill=orange, stroke='none')
show(inner_sqr_rot_cover)

inner_most_poo = ellipse(
    w=6, h=3, x=5, y=0, fill=dark_pink) | repeat(8, rotate(45))
show(inner_most_poo)


inner_sqr_rot_a = rectangle(w=35.36, h=35.36, x=18,
                            y=18, fill=orange, stroke='none')
inner_sqr_rot_b = rectangle(w=35.36, h=35.36, x=18, y=18,
                            fill=yellow, stroke='none') | rotate(45)

inner_sqr_rot = combine(
    [inner_sqr_rot_a, inner_sqr_rot_b]) | repeat(4, rotate(90))
show(inner_sqr_rot)

p1 = point(x=0, y=0)
p2 = point(x=35.36, y=35.36)
p3 = point(x=35.36, y=0)

inner_sqr_rot_cover = polygon([p1, p2, p3], fill=orange, stroke='none')
show(inner_sqr_rot_cover)
