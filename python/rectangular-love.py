from hypothesis import given
import hypothesis.strategies as st

def rectangle_from_coords_height_and_width(x, y, height, width):
    return {"x": x, "y": y, "height": height, "width": width}

def overlap(first, second):
    """Finds overlaps between the first and second rectangle.

    An overlap is equivalent to at least one vertical and one
    horizontal boundary being contained within the bounds of
    the other rectangle. A line segment is within the bounds
    of a rectangle if it is parallel to one of the sides, and
    also has position greater than the lesser side along the
    dimension perpendicular to its direction, and less than
    the greater side along that same dimension."""

    def direction(line):
        differ_in_x = line[0][0] != line[1][0]
        differ_in_y = line[0][1] != line[1][1]

        # the endpoints must differ on only one dimension for this to be
        # either a vertical or horizontal line.
        assert not (differ_in_x and differ_in_y)

        if differ_in_x:
            return "horizontal"
        elif differ_in_y:
            return "vertical"

    def _side(base, offset, dimension):
        assert dimension in ("x", "y")

        if dimension == "x":
            other_end = (base[0] + offset, base[1])
        elif dimension == "y":
            other_end = (base[0], base[1] + offset)

        return (base, other_end)


    def left_side(rectangle):
        base_x = rectangle["x"]
        base_y = rectangle["y"]
        return _side((base_x, base_y), rectangle["height"], "y")

    def right_side(rectangle):
        base_x = rectangle["x"] + rectangle["width"]
        base_y = rectangle["y"]

        return _side((base_x, base_y), rectangle["height"], "y")

    def bottom_side(rectangle):
        base_x = rectangle["x"]
        base_y = rectangle["y"]

        return _side((base_x, base_x), rectangle["width"], "x")

    def top_side(rectangle):
        base_x = rectangle["x"]
        base_y = rectangle["y"] + rectangle["height"]

        return _side((base_x, base_y), rectangle["width"], "x")

    def side_from_name(side, rectangle):
        if side == "left":
            return left_side(rectangle)
        if side == "right":
            return right_side(rectangle)
        if side == "bottom":
            return bottom_side(rectangle)
        if side == "top":
            return top_side(rectangle)

    def side_contained(side, this_rect=first, other_rect=second):
        return within_bounds(side_from_name(side, this_rect), other_rect)

    def within_bounds(line, rectangle):
        line_direction = direction(line)

        if line_direction == "horizontal":
            lower_bound = rectangle["y"]
            midpoint = line[0][1]
            upper_bound = rectangle["y"] + rectangle["height"]
        elif line_direction == "vertical":
            lower_bound = rectangle["x"]
            midpoint = line[0][0]
            upper_bound = rectangle["x"] + rectangle["width"]

        prop = lower_bound <= midpoint <= upper_bound
        print lower_bound, midpoint, upper_bound, prop

        return prop

    contained_sides = []
    for base_rect, other_rect in [[first, second], [second, first]]:
        for side in ["left", "right", "bottom", "top"]:
            if side_contained(side, base_rect, other_rect):
                contained_sides.append(side_from_name(side, base_rect))

    assert len(contained_sides) in range(9) # must allow up to 8 contained sides

    if len(contained_sides) in (4, 6, 8): # overlap partially, share an edge, fully contained
        horizontal_sides = filter(lambda s: direction(s) == "horizontal", contained_sides)
        vertical_sides = filter(lambda s: direction(s) == "vertical", contained_sides)

        left =   min(vertical_sides,   key=lambda x: x[0][0])
        right =  max(vertical_sides,   key=lambda x: x[0][0])
        bottom = min(horizontal_sides, key=lambda x: x[0][1])
        top =    max(horizontal_sides, key=lambda x: x[0][1])

        # we cannot use the left or right side's length, as it may extend further
        # than the intersection. we have to construct entirely new sides based on
        # the height, width, and boundaries established by the sides.
        height = abs(top[0][1] - bottom[0][1])
        width = abs(right[0][0] - left[0][0])

        print bottom
        x = left[0][0]
        y = bottom[0][1]

        return rectangle_from_coords_height_and_width(x, y, height, width)

strategies = [
    st.integers(),            # x1
    st.integers(),            # y1
    st.integers(),            # x2
    st.integers(),            # y2
    st.integers(min_value=0), # height1
    st.integers(min_value=0), # width1
    st.integers(min_value=0), # height2
    st.integers(min_value=0)  # width2
]

def run_overlap_with_constructed_rects(x1, y1, x2, y2, height1, width1, height2, width2):
    first = rectangle_from_coords_height_and_width(x1, y1, height1, width1)
    second = rectangle_from_coords_height_and_width(x2, y2, height2, width2)

    print first, second

    return overlap(first, second)

@given(*strategies)
def overlap_doesnt_shit_itself_on_random_inputs(x1, y1, x2, y2, height1, width1, height2, width2):
    run_overlap_with_constructed_rects(x1, y1, x2, y2, height1, width1, height2, width2)

manual_test_cases = [
    [0, 0, 1, 1, 10, 10, 10, 10], # partial overlap
    [0, 0, 1, 1, 20, 20, 10, 10], # fully contained
    [0, 0, 1, 0, 1, 1, 1, 1] # share edge
]

for manual_test_case in manual_test_cases:
    print run_overlap_with_constructed_rects(*manual_test_case)

#for _ in xrange(100):
#    overlap_doesnt_shit_itself_on_random_inputs()
