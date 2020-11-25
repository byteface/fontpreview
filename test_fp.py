import unittest
import os
from fontpreview import FontPreview, FontBanner, FontLogo, FontWall, FontPage, FontPageTemplate

# Enter the file font to test and check exists
font = input('Enter path of font file to test: ')
if not os.path.exists(font):
    raise OSError("file font {0} doesn't exists".format(font))


class TestFontPreview(unittest.TestCase):
    fp, fb, fl = FontPreview(font), FontBanner(font), FontLogo(font, 'Fl')
    fw, fpage, fpage_t = FontWall([fb]), FontPage(), FontPageTemplate(3508)

    def test_instance(self):
        # test if instance has been created
        self.assertIsInstance(self.fp, FontPreview)
        self.assertIsInstance(self.fb, FontBanner)
        self.assertIsInstance(self.fl, FontLogo)
        self.assertIsInstance(self.fw, FontWall)
        self.assertIsInstance(self.fpage, FontPage)
        self.assertIsInstance(self.fpage_t, FontPageTemplate)

    def test_set_color_with_name(self):
        # change background color
        self.fp.bg_color = self.fb.bg_color = self.fl.bg_color = 'blue'
        # change background color
        self.fp.fg_color = self.fb.fg_color = self.fl.fg_color = 'yellow'
        # test draw it
        self.fp.draw()
        self.fb.draw()
        self.fl.draw()

    def test_set_color_with_tuple(self):
        # change background color
        self.fp.bg_color = self.fb.bg_color = self.fl.bg_color = (51, 153, 193)
        # change background color
        self.fp.fg_color = self.fb.fg_color = self.fl.fg_color = (253, 194, 45)
        # test draw it
        self.fp.draw()
        self.fb.draw()
        self.fl.draw()

    def test_set_dimension(self):
        # test dimension of FontPreview object
        self.fp.dimension = (1000, 1000)
        # test draw it
        self.fp.draw()
        # test dimension of FontBanner object
        self.fb.set_orientation((1000, 1000))
        # test draw it
        self.fb.draw()
        # test dimension of FontBanner object and font position
        self.fb.set_orientation('landscape', 'lcenter')
        # test draw it
        self.fb.draw()
        # test dimension of FontLogo object
        self.fl.new_size((75, 75))
        self.fl.new_size((100, 100))
        self.fl.new_size((150, 150))
        self.fl.new_size((170, 170))
        # test draw it
        self.fp.draw()


if __name__ == '__main__':
    unittest.main()
