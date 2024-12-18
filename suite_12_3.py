import test_12_1 as test1
import test_12_2 as test2
import unittest as ut

is_frozen = False

My_Test_Suite = ut.TestSuite()

My_Test_Suite.addTest(ut.TestLoader().loadTestsFromTestCase(test1.RunnerTest))
My_Test_Suite.addTest(ut.TestLoader().loadTestsFromTestCase(test2.TournamentTest))

runner = ut.TextTestRunner(verbosity = 2)
runner.run(My_Test_Suite)

