particles = (('NUM', 'NAME', 'MASS', 'CHARGE', 'SPIN', 'TYPENO'),
       (0, 'UP', 2.3, 2.0/3, 1.0/2, 10),
       (1, 'DOWN', 4.8, -1.0/3, 1.0/2, 10),
       (2, 'ELECTRON', 0.511, -1.0, 1.0/2, 20),
       (3, 'ELECTRON NEUTRINO', 0.0, 0.0, 1.0/2, 20),
       (4, 'CHARM', 1275.0, 2.0/3, 1.0/2, 10),
       (5, 'STRANGE', 95.0, -1.0/3, 1.0/2, 10),
       (6, 'MUON', 105.7, -1.0, 1.0/2, 20),
       (7, 'MUON NEUTRINO', 0.0, 0.0, 1.0/2, 20),
       (8, 'TOP', 173070.0, 2.0/3, 1.0/2, 10),
       (9, 'BOTTOM', 4180.0, -1.0/3, 1.0/2, 10),
       (10, 'TAU', 1777.0, -1.0, 1.0/2, 20),
       (11, 'TAU NEUTRINO', 0.0, 0.0, 1.0/2, 20),
       (12, 'GLUON', 0.0, 0.0, 1.0, 30),
       (13, 'PHOTON', 0.0, 0.0, 1.0, 30),
       (14, 'Z BOSON', 91200.0, 0.0, 1.0, 30),
       (15, 'W BOSON', 80400.0, 1.0, 1.0, 30),
       (16, 'HIGGS', 126000.0, 0.0, 0.0, 30))

type_part = (('TYPENO', 'TYPENAME', 'FORCE'),
        (10, 'QUARK', 'STRONG'),
        (20, 'LEPTON', 'WEAK'), 
		(30, 'BOSON', 'CARRIER'))


# select name, mass from particles
print "\nselect name, mass from particles: ", [[i[1], i[2]] for i in particles[1::]]

# select name, mass from particles where mass > 1 GeV (1000 MeV)
print "\nselect name, mass from particles where mass > 1 Gev (1000 MeV): ", [[i[1], i[2]] for i in particles[1::] if i[2] > 1000]

# select name, mass, spin from particles where mass > 1 GeV and spin  = 1.0/2 order by mass
print "\nselect name, mass, spin from particles where mass > 1 GeV and spin  = 1.0/2 order by mass: ", sorted([[i[1], i[2],i[4]] for i in particles[1::] if i[2] > 1000 and i[4] == 1.0/2], key = lambda x: int(x[1]))

# select name, mass from particles where mass > 1 GeV  order by mass
print "\nselect name, mass from particles where mass > 1 GeV order by mass: ", sorted([[i[1], i[2]] for i in particles[1::] if i[2] > 1000], key = lambda x: int(x[1]))

# select name, mass from particles where mass > 1 GeV order by mass desc
print "\nselect name, mass from particles where mass > 1 GeV order by mass desc: ", sorted([[i[1], i[2]] for i in particles[1::] if i[2] > 1000], key = lambda x: int(x[1]), reverse=True)


# select name, typename from particles p join type_part t on(p.typeno = t.typeno)
print "\nselect name, typename from particles p join type_part t on(p.typeno = t.typeno): ", [ [i[1], j[1]] for i in particles[1::] for j in type_part[1::] if i[5] == j[0] ]

# select name, typename from particles p join type_part t on(p.typeno = t.typeno) where mass > 1000
print "\nselect name, typename from particles p join type_part t on(p.typeno = t.typeno) where mass > 1000: ", [ [i[1], j[1]] for i in particles[1::] for j in type_part[1::] if i[5] == j[0] and i[2]>1000]


# select typeno, avg(mass) from particles group by typeno
print "\nselect typeno, avg(mass) from particles group by typeno: "
for type_particle in { t[5] for t in particles[1::] }: print (lambda typeno, avgMass: [typeno, avgMass])(type_particle, (lambda l: round(sum(l) / len(l), 2))(map(float,[ p[2] for p in particles[1::] if p[5] == type_particle ])))

# select typeno, avg(mass) from particles group by typeno having avg(mass) > 1000
print "\nselect typeno, avg(mass) from particles group by typeno having avg(mass) > 1000:"
for type_particle in { t[5] for t in particles[1::] }: print (lambda typeno, avgMass: (typeno, avgMass) if avgMass > 1000 else '')(type_particle, (lambda l: round(sum(l) / len(l), 2))(map(float,[ p[2] for p in particles[1::] if p[5] == type_particle ])))

