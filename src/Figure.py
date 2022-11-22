
class Figure:

    @property
    def area(self):
        return 0

    def add_area(self, figure):
        if not (isinstance(figure, Figure)):
            raise ValueError
        else:
            all_area = self.area + figure.area
            return all_area
