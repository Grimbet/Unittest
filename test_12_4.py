import unittest
import new_runner as runner
import logging as log


class RunnerTest(unittest.TestCase):
    log.basicConfig(level=log.INFO, filemode='w', filename='runner_tests.log', encoding="utf-8")
    is_frozen = False

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            r = runner.Runner("Andrey",-2)
            log.info(f'test_walk для {r.name} выполнен успешно', exc_info=True)
            for i in range(10):
                r.walk()
            self.assertEqual(r.distance, 50)
        except ValueError as ex:
            log.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            r = runner.Runner(15)
            log.info(f'test_run для {r.name} выполнен успешно', exc_info=True)
            for i in range(10):
                r.run()
            self.assertEqual(r.distance, 100)
        except TypeError as ex:
            log.warning('Неверный тип данных для имени объекта Runner', exc_info=True)


    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r1 = runner.Runner("Name1")
        r2 = runner.Runner("Name2")
        for i in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == "__main__":
    unittest.main()