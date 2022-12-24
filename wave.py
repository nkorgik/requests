class WaveMeshClass:
    
    def transform(self, coordinates: tuple) -> tuple:
        x, y = coordinates
        y = y + 10*math.sin(x/40)

        return x, y

    def transform_rectangle(self, coordinates: tuple) -> tuple:
        x0, y0, x1, y1 = coordinates
        return (*self.transform((x0,y0)), *self.transform((x1,y0)), *self.transform((x1,y1)), *self.transform((x0,y1)))

    def getmesh(self, img):
        self.height = img.height
        self.width = img.width
        gridspace = 20

        grid = []
        for x in range(0, self.width, gridspace):
            for y in range(0, self.height, gridspace):
                grid.append((x, y, x+gridspace, y+gridspace))

        target_grid = [self.transform_rectangle(box) for box in grid]

        return [t for t in zip(grid, target_grid)]