import unittest
import client as client

pathOfClientFile = "client.txt"

dataNombreForeachlin = 4;

fileName = "client.txt"

class TestTraitementdeDonnee(unittest.TestCase):
    def test_get_file_name(self):
        self.assertEquals(client.get_file_name(pathOfClientFile), fileName)

    def testIfExistFile(self):
        self.assertTrue(client.isExisteFile(pathOfClientFile))

    def testifEmptyFile(self):
        self.assertTrue(client.isEmPtyFile(pathOfClientFile))

    def test_checkDataNumberForEachLine(self):
        self.assertNoEquals(client.checkDataNumberForEachLin(pathOfClientFile), dataNombreForeachlin)

if __name__ =='__main__':
    unittest.main
        
