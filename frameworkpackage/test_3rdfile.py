from logfile import logclass

class TestExample(logclass):
    def test_2ndtest(self):
        log = self.getthelogs()
        log.info('This is my first test case')
        log.info('this case is not starting')
        if 'anshul' in 'anshuljain':
            assert True
            log.info('test case pass')
        else:
            log.error('test case fail')
            assert False