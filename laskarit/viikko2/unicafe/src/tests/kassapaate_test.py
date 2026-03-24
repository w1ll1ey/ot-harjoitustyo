import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_kassassa_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_oikea_maara_edullisia_lounaita(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_oikea_maara_maukkaita_lounaita(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_edullinen_kateinen_kasvattaa_rahaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
    
    def test_edullinen_kateinen_antaa_vaihtorahan_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        
    def test_edullisen_kateisella_osto_kasvattaa_niiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_edullinen_kateinen_rahat_ei_riita_ei_kasvata_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_edullinen_kateinen_rahat_ei_riita_antaa_kaiken_takaisin(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)
        
    def test_edullinen_kateinen_rahat_ei_riita_ei_kasvata_niiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_maukas_kateinen_kasvattaa_rahaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
    
    def test_maukas_kateinen_antaa_vaihtorahan_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)
        
    def test_maukkaasti_kateisella_osto_kasvattaa_niiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_maukas_kateinen_rahat_ei_riita_ei_kasvata_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_maukas_kateinen_rahat_ei_riita_antaa_kaiken_takaisin(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(390), 390)
        
    def test_maukas_kateinen_rahat_ei_riita_ei_kasvata_niiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)
        
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullinen_kortilla_veloitetaan_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)
    
    def test_edullinen_kortilla_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_edullinen_kortilla_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_edullinen_kortti_rahat_ei_riita_ei_veloita(self):
        maksukortti = Maksukortti(230)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        
        self.assertEqual(maksukortti.saldo_euroina(), 2.3)
    
    def test_edullinen_kortti_rahat_ei_riita_palauttaa_false(self):
        maksukortti = Maksukortti(230)
        
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)
    
    def test_edullinen_kortti_rahat_ei_riita_ei_kasvata_lounaiden_maaraa(self):
        maksukortti = Maksukortti(230)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_edullinen_osto_ei_kasvata_kassaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_maukas_kortilla_veloitetaan_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)
    
    def test_maukas_kortilla_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_maukas_kortilla_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_maukas_kortti_rahat_ei_riita_ei_veloita(self):
        maksukortti = Maksukortti(390)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        
        self.assertEqual(maksukortti.saldo_euroina(), 3.9)
    
    def test_maukas_kortti_rahat_ei_riita_palauttaa_false(self):
        maksukortti = Maksukortti(390)
        
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)
    
    def test_maukas_kortti_rahat_ei_riita_ei_kasvata_lounaiden_maaraa(self):
        maksukortti = Maksukortti(230)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_maukas_osto_ei_kasvata_kassaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        
    def test_kortille_ladattaessa_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 15.00)
        
    def test_kortille_ladattaessa_kassan_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005.0)
    
    def test_negatiivista_summaa_ei_ladata_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
        
    def test_negatiivinen_summa_ladattaessa_ei_kasvata_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)