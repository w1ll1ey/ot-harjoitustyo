import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
        
    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(500)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 15.00)
        
    def test_saldo_vahenee_ottaessa(self):
        self.maksukortti.ota_rahaa(500)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.00)
        
    def test_liian_suuri_rahankaytto_ei_onnistu(self):
        self.maksukortti.ota_rahaa(1100)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
        
    def test_ota_rahaa_palauttaa_true(self): 
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
        
    def test_ota_rahaa_palauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)