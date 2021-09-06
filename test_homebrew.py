from unittest import main, TestCase

class HomeBrewTest(TestCase):
    def setUp(self):
        pass

    def test_unittest_runs(slef):
        pass

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_force_fail(self):
        assert 2 == 3
        
if __name__ == "__main__":
    main()