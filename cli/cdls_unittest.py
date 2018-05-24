#!/usr/bin/python3

from src.cli import Cli
import unittest
from os import linesep

class CdLsTest(unittest.TestCase):
    def setUp(self):
        self.cli = Cli()

    def test_ls(self):
        self.cli.process_input('cd cd_ls_test')
        result = self.cli.process_input('ls')
        self.assertEqual(result.get_output(),
        		'dir2' + linesep + 'dir1' + linesep)
    
        self.cli.process_input('cd dir1')
        result = self.cli.process_input('ls')
        self.assertEqual(result.get_output(), 'file1' + linesep)
    
    def test_cd_dots(self):
        self.cli.process_input('cd cd_ls_test')
        self.cli.process_input('cd dir1')
        self.cli.process_input('cd ..')
        result = self.cli.process_input('ls dir1')
        self.assertEqual(result.get_output(), 'file1' + linesep)
        
    def test_cd_tilde(self):
        self.cli.process_input('cd cd_ls_test')
        self.cli.process_input('cd dir1')
        self.cli.process_input('cd ~')
        result = self.cli.process_input('ls cd_ls_test')
        self.assertEqual(result.get_output(), 'dir2' + linesep + 'dir1' + linesep)

if __name__ == '__main__':
    unittest.main()

