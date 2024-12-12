import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Начало теста")
        cls.all_results={}

    @classmethod
    def tearDownClass(cls):
        #выводим все результаты тестов в столбец
        for num, value in cls.all_results.items():
            print(value)
        print("Тест завершен")

    def setUp(self):
        self.r1 = rt.Runner("Усейн",10)
        self.r2 = rt.Runner("Андрей", 9)
        self.r3 = rt.Runner("Ник", 3)

    #тест1
    def test_rt1(self):
        sp = {}
        t = rt.Tournament(90,self.r1,self.r3)
        rez = t.start()
        for num, value in rez.items():
            sp[num] = value.name
        self.assertTrue(sp[max(sp)]=="Ник") #проверяем зовут ли последнего Ник
        self.all_results[1]=sp

    # тест2
    def test_rt2(self):
        sp = {}
        t = rt.Tournament(90,self.r2,self.r3)
        rez = t.start()
        for num, value in rez.items():
            sp[num] = value.name
        self.assertTrue(sp[max(sp)]=="Ник") #проверяем зовут ли последнего Ник
        self.all_results[2]=sp

    # тест3
    def test_rt3(self):
        sp = {}
        t = rt.Tournament(90,self.r1,self.r2,self.r3)
        rez = t.start()
        for num, value in rez.items():
            sp[num] = value.name
        self.assertTrue(sp[max(sp)]=="Ник") #проверяем зовут ли последнего Ник
        self.all_results[3]=sp


if __name__=="__main__":
    unittest.main()

'''
!!!Дополнительное задание!!!

В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка!
Ошибка в том, что важен порядок участников, заявленных на турнир!
Если заявить их на турнир как Усейн, Андрей, Ник - то первый придет Усейн, что логично!
Если заявить Андрей, Усейн, Ник - то первый придет Андрей, несмотря на меньшую скорость чем у Усейна! Это неправильно!
Решить это можно путем сортировки по скорости участников на турнир в модуле runner_and_tournament.py
Делается это так:
Надо добавить строчку кода в Tournament при инциализации класса def __init__
self.participants.sort(key=lambda Runner: Runner.speed, reverse=True)
Так мы отсортируем перед турниром участников по скорости!
С этой строкой кода можно в любом порядке добавлять участников! ПРОВЕРЕНО! Работает!
'''