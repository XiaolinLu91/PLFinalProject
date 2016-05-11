# PLFinalProject
Kartik Chitturi kc29563
Xiaolin Lu xl4723

Test codes for python closures:
(Part 3:)
ml> (exec 'from Stocks import stock; s1 = stock(); toReturn = s1.run('PEratio') ')
ml> (exec 'from Stocks import stock; s1 = stock(); s1.run('$PEratio')(8); s1.run('PEratio') ')
ml> (exec 'from Stocks import stock, BlueChip; b1 = BlueChip(); toReturn = b1.run('yearDiv') ')

Test codes for java stream operations:
(Part 4: need to compile Stock.java, Sector.java and ListComprehension.java first)
ml> (exec 'import Stock, Sector, ListComprehension; s1 = ListComprehension(); s1.selectStocks()')
ml> (exec 'import Stock, Sector, ListComprehension; s1 = ListComprehension(); s1.filterStocks(10.0, 100.0)')
ml> (exec 'import Stock, Sector, ListComprehension; s1 = ListComprehension(); s1.avgDEratio()')
ml> (exec 'import Stock, Sector, ListComprehension; s1 = ListComprehension(); s1.allSector()')
ml> (exec 'import Stock, Sector, ListComprehension; s1 = ListComprehension(); s1.orderStocks()')

For python lambda (part 5), running PythonListComprehension.py

For the Swift part, running mini-lisp.py will go through the file test_program.swift
