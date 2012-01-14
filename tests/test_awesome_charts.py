
import unittest

from awesome import AwesomeBar

class TestAwesomeBar(unittest.TestCase):

    def test_smarty_modifier_contrast(self):
        self.assertEquals(
            AwesomeBar.smarty_modifier_contrast('#000000'),
            'white'
        )

        self.assertEquals(
            AwesomeBar.smarty_modifier_contrast('#ffffff'),
            'black'
        )
