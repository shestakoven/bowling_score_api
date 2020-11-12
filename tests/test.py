import unittest
from bowling import Scorer, GlobalRules


class GameResultTest(unittest.TestCase):

    def test_normal(self):
        result = Scorer('Х4/34-4-5X17X1/5-')
        score = result.get_score()
        self.assertEqual(score, 119)

    def test_x(self):
        result = Scorer('xxxxxxxxxx')
        score = result.get_score()
        self.assertEqual(score, 200)

    def test_spare(self):
        with self.assertRaisesRegex(BaseException, 'Неверно указан результат: '):
            Scorer('////////////////////').get_score()

    def test_invalid_symbols(self):
        with self.assertRaisesRegex(BaseException, 'Результат содержит недопустимые символы'):
            Scorer('12asdxp132').get_score()

    def test_more_frames(self):
        with self.assertRaisesRegex(BaseException, 'Количество фреймов должно быть равно десяти!'):
            Scorer('112233444433221112').get_score()

    def test_less_symbols(self):
        with self.assertRaisesRegex(BaseException, 'Количество фреймов должно быть равно десяти!'):
            Scorer('11223344443322').get_score()

    def test_int(self):
        result = Scorer(11111111111111111111)
        score = result.get_score()
        self.assertEqual(score, 20)

    def test_global_rules(self):
        result = GlobalRules('ХXX347/21--------')
        score = result.get_score()
        self.assertEqual(score, 92)

    def test_global_rules_ends_x(self):
        result = GlobalRules('ХXX347/21------X')
        score = result.get_score()
        self.assertEqual(score, 102)

    def test_global_rules_ends_spare(self):
        result = GlobalRules('ХXX347/21-------/')
        score = result.get_score()
        self.assertEqual(score, 102)


if __name__ == '__main__':
    unittest.main()
