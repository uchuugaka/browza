from selenium import selenium
import unittest, HTMLTestRunner, os, re, sys, time
suite = unittest.TestSuite()
loader = unittest.TestLoader()

class TestClass(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(*self.browser)
        self.selenium.start()
    
    def tearDown(self):
        self.selenium.stop()
    

class TestClassCases(TestClass):
    def test_Do_Things(self):
        self.selenium.open("/")
    


def set_testcase_browser(obj, browser):
    try:
        child_tests = obj._tests
    except AttributeError:
        obj.browser = browser
        return
    for child in child_tests:
        set_testcase_browser(child, browser)
    return browser_list


if __name__ == "__main__":
    print sys.platform
    if sys.platform == 'darwin':
        directory = "/Users/along/Desktop/Browsers/"
        local_url = "localhost"
        site_url = "http://www.google.com/"
        browsers = os.listdir('/Users/along/Desktop/Browsers/')
        browsers.remove(".DS_Store")
        print browsers
        browser_list = []
        for browser in browsers:
            directory_browser = (directory +  browser)
            if re.match("Firefox", browser):
                browser_list.append(
                    [ local_url, 4444, "*custom %s/Contents/MacOS/firefox-bin" % directory_browser, site_url
                    ])
            elif re.match("Safari", browser):
                browser_list.append(
                [ local_url, 4444, "*custom %s/Contents/MacOS/Safari" % directory_browser, site_url
                ])
            elif re.match("Chrome", browser):
                browser_list.append([local_url, 4444, "*custom %s/Chrome.app/Contents/MacOS/Chrome" % directory_browser, site_url
                ])
    for browsers in browser_list:
        browser_suite = loader.loadTestsFromTestCase(TestClassCases)
        set_testcase_browser(browser_suite, browsers)
        suite.addTest(browser_suite)
    fp = file('results.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream = fp,
                title = 'Browza Test',
                description = str(time.strftime("%I:%M:%S %p", time.localtime())) + ' - Version 0.1a',
                )
    runner.run(suite)