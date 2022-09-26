import json
import os


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(THIS_DIR, "Concave_Geometric factor.json")


f = open(json_file_path)
data = json.load(f)

possible_geometry = ["beam", "cylinder"]
possible_loading = ["tensile", "clamped"]
calculated_wire_aspect_ratio = [2, 4, 6, 8, 10, 100]
calculated_crack_aspect_ratio = [-0.05, -0.10, -0.15, -0.20, -0.25, -0.30, -0.35, -0.40, -0.45, -0.50, -0.55, -0.60,
                                 -0.65, -0.70, -0.75, -0.80, -0.85, -0.90, -0.95, -1.0, 0.0, 0.05, 0.10, 0.15, 0.20, 0.25,
                                 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.0]
calculated_crack_depth = [0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70]


class GF_extractor():
    def __init__(self, geometry, loading, wire_aspect_ratio, crack_aspect_ratio, crack_depth):
        self.geometry = geometry
        self.loading = loading
        self.wire_aspect_ratio = wire_aspect_ratio
        self.crack_aspect_ratio = crack_aspect_ratio
        self.crack_depth = crack_depth

    def gf_center(self):
        for i in data:
            if i['geometry'] == self.geometry and i['loading'] == self.loading and i['wire_aspect_ratio'] == self.wire_aspect_ratio and i['crack_aspect_ratio'] == self.crack_aspect_ratio and i['crack_depth'] == self.crack_depth:
                # print(i['GF_center'])
                GF_center = i['GF_center']
                break

        return GF_center


    def gf_surface(self):
        for i in data:
            if i['geometry'] == self.geometry and i['loading'] == self.loading and i['wire_aspect_ratio'] == self.wire_aspect_ratio and i['crack_aspect_ratio'] == self.crack_aspect_ratio and i['crack_depth'] == self.crack_depth:
                # print(i['GF_surface'])
                GF_surface = i['GF_surface']
                break

        return GF_surface



    @property
    def geometry(self):
        return self._geometry

    @geometry.setter
    def geometry(self, new_geometry):
        if new_geometry in possible_geometry:
            self._geometry = new_geometry
        else:
            raise ValueError("Sorry, the GF for this geometry is not available yet")

    @property
    def loading(self):
        return self._loading

    @loading.setter
    def loading(self, new_loading):
        if new_loading in possible_loading:
            self._loading = new_loading
        else:
            raise ValueError("Sorry, the GF for this loading condition is not available yet")

    @property
    def wire_aspect_ratio(self):
        return self._wire_aspect_ratio

    @wire_aspect_ratio.setter
    def wire_aspect_ratio(self, new_wire_aspect_ratio):
        if new_wire_aspect_ratio in calculated_wire_aspect_ratio:
            self._wire_aspect_ratio = new_wire_aspect_ratio
        else:
            raise ValueError("Sorry, the GF for this wire aspect ratio is not calculated. Kindly make use of the "
                             "GF_extractor_fitted method to find the fitted GF.")

    @property
    def crack_aspect_ratio(self):
        return self._crack_aspect_ratio

    @crack_aspect_ratio.setter
    def crack_aspect_ratio(self, new_crack_aspect_ratio):
        if new_crack_aspect_ratio in calculated_crack_aspect_ratio:
            self._crack_aspect_ratio = new_crack_aspect_ratio
        else:
            raise ValueError("Sorry, the GF for this crack aspect ratio is not calculated. Kindly make use of the "
                             "GF_extractor_fitted method to find the fitted GF.")

    @property
    def crack_depth(self):
        return self._crack_depth

    @crack_depth.setter
    def crack_depth(self, new_crack_depth):
        if new_crack_depth in calculated_crack_depth:
            self._crack_depth = new_crack_depth
        else:
            raise ValueError("Sorry, the GF for this crack depth is not calculated. Kindly make use of the "
                             "GF_extractor_fitted method to find the fitted GF.")


# p0 = GF_extractor(geometry="cylinder", loading="tensile", wire_aspect_ratio=4, crack_aspect_ratio=-1.0, crack_depth=0.35)
# p1 = GF_extractor('Cylinder', "Clamped", 10, 0.45, 0.2)
# p2 = GF_extractor('Beam', "Tensile", 100, 0.25, 0.65)
# p3 = GF_extractor('3pb', 100, 0.25, 0.65)
# p4 = GF_extractor('Beam', 77, 0.25, 0.65)
# p5 = GF_extractor('Beam', 100, 0.23, 0.65)

# p5 = GF_extractor_fitted('Beam', 100, 0.23, 0.65)


# print(p0.geometry, p0.crack_aspect_ratio)

# p0.gf_center()
# x = p0.gf_surface()
#
# print(x+2)




