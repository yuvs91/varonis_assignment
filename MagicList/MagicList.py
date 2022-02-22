class MagicList(list):

    def __init__(self, cls_type=None):
        self.cls_type = cls_type
        super().__init__(self)

    def __setitem__(self, key, value):
        if len(self) == key:
            super().append(value)
        else:
            super().__setitem__(key, value)

    def __getitem__(self, key):
        if len(self) == key:
            if self.cls_type():
                super().append(self.cls_type())

        return super().__getitem__(key)