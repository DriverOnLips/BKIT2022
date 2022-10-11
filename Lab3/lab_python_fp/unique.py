# TODO


class Unique(object):
    def __init__(self, items, **kwargs):
        self.position = 0
        self.items = [str(i) for i in items]
        self.element = items[self.position]
        self.output = []
        try:
            self.ignore_case = kwargs["ignore_case"]
            if self.ignore_case:
                self.elements = [self.element.lower(), self.element.upper()]
            else:
                self.elements = [str(self.element)]
        except:
            self.ignore_case = False
            self.elements = [str(self.element)]
        self.output.append(self.element)

    def __next__(self):
        self.position += 1
        for i in range(self.position, len(self.items)):
            self.position = i
            if self.items[self.position] not in self.elements:
                if self.ignore_case:
                    self.element = self.items[self.position]
                    self.elements.extend([self.element.lower(), self.element.upper()])
                    self.output.append(self.element)
                    return self.element
                else:
                    self.element = self.items[self.position]
                    self.elements.append(self.element)
                    self.output.append(self.element)
                    return self.element

    def __iter__(self):
        return self

    def filling(self):
        element = next(self)
        while element is not None:
            element = next(self)
        return self.output
