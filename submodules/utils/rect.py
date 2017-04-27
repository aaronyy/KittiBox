class Rect(object):
    def __init__(self, cx, cy, width, height, confidence):
        self.cx = cx
        self.cy = cy
        self.width = width
        self.height = height
        self.confidence = confidence
        self.true_confidence = confidence
    def overlaps(self, other):
        if abs(self.cx - other.cx) > (self.width + other.width) / 1.5:
            return False
        elif abs(self.cy - other.cy) > (self.height + other.height) / 2.0:
            return False
        else:
            return True
    def distance(self, other):
        return sum(map(abs, [self.cx - other.cx, self.cy - other.cy,
                       self.width - other.width, self.height - other.height]))
    def intersection(self, other):
        left = max(self.cx - self.width/2., other.cx - other.width/2.)
        right = min(self.cx + self.width/2., other.cx + other.width/2.)
        width = max(right - left, 0)
        top = max(self.cy - self.height/2., other.cy - other.height/2.)
        bottom = min(self.cy + self.height/2., other.cy + other.height/2.)
        height = max(bottom - top, 0)
        return width * height
    def area(self):
        return self.height * self.width
    def union(self, other):
        return self.area() + other.area() - self.intersection(other)
    def iou(self, other):
        return self.intersection(other) / self.union(other)
    def __eq__(self, other):
        return (self.cx == other.cx and 
            self.cy == other.cy and
            self.width == other.width and
            self.height == other.height and
            self.confidence == other.confidence)

class Box(object):
    def __init__(self, cx, cy, cz, width, height, depth, confidence):
        self.cx = cx
        self.cy = cy
        self.cz = cz
        self.width = width
        self.height = height
        self.depth = depth
        self.confidence = confidence
        self.true_confidence = confidence
    def overlaps(self, other):
        if abs(self.cx - other.cx) > (self.width + other.width) / 1.5:
            return False
        elif abs(self.cy - other.cy) > (self.height + other.height) / 2.0:
            return False
        elif abs(self.cz - other.cz) > (self.depth + other.depth) / 2.0:
            return False
        else:
            return True
    def distance(self, other):
        return sum(map(abs, [
            self.cx - other.cx, self.cy - other.cy, self.cz - other.cz,
                       self.width - other.width, self.height - other.height, self.depth - other.depth]))
    def intersection(self, other):
        left = max(self.cx - self.width/2., other.cx - other.width/2.)
        right = min(self.cx + self.width/2., other.cx + other.width/2.)
        width = max(right - left, 0)
        top = max(self.cy - self.height/2., other.cy - other.height/2.)
        bottom = min(self.cy + self.height/2., other.cy + other.height/2.)
        height = max(bottom - top, 0)
        start = max(self.cz - self.depth/2., other.cz - other.depth/2.)
        end = min(self.cz + self.depth/2., other.cz + other.depth/2.)
        depth = max(end - start, 0)
        return width * height * depth
    def area(self):
        return self.height * self.width * self.depth
    def union(self, other):
        return self.area() + other.area() - self.intersection(other)
    def iou(self, other):
        return self.intersection(other) / self.union(other)
    def __eq__(self, other):
        return (self.cx == other.cx and 
            self.cy == other.cy and
            self.cz == other.cz and
            self.width == other.width and
            self.height == other.height and
            self.depth == other.depth and
            self.confidence == other.confidence)
