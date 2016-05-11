class stock(object):
    def f(self):
        data = {
            'name': 'Stock',
            '$name': lambda x: data.update({'name': x}),
            'PEratio': 6,
            '$PEratio': lambda x: data.update({'PEratio': x})
        }
        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return None
        return cf
    run = f(1)


# print s1.data

class BlueChip(stock):
    #def run(self, a): return super(animal, self).run(a)
    def f(self):
        data = {
            'name': 'BlueChip',
            '$name': lambda x: data.update({'name': x}),
            'yearDiv': 135,
            '$yearDiv': lambda x: data.update({'yearDiv': x}),
            'PEratio': 21.13,

        }
        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return super(BlueChip, self).run(d)
        return cf
    run = f(1)

