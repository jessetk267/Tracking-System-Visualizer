class ErrorField:
    def __init__(self):
        self.points = []
        self.errors = []

    def add_sample(self, point, error):
        self.points.append(point)
        self.errors.append(error)

    def to_polydata(self):
        cloud = pv.PolyData(np.array(self.points))
        cloud["error"] = np.array(self.errors)
        return cloud
