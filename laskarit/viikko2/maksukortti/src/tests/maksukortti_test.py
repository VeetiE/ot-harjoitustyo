from maksukortti import Maksukortti
import unittest
class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")


    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_edullisesti()
        self.assertEqual("Kortilla on rahaa 2 euroa", str(self.kortti))
    
    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.assertEqual("Kortilla on rahaa 2 euroa", str(self.kortti))
        
    def test_kortille_voi_ladata_rahaa(self):
    	self.kortti.lataa_rahaa(25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")
    
    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
    	self.kortti.lataa_rahaa(200)
    	self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")
    
    def test_kortille_negatiivisen_summan_lataus_ei_muuta_arvoa(self):
    	self.kortti.lataa_rahaa(-10)
    	self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")
    	
    def test_kortilla_on_tasan_maukkaan_verran_voi_ostaa_vain_maukkaan(self):
    	self.kortti.syo_edullisesti()
    	self.kortti.syo_maukkaasti()
    	self.kortti.lataa_rahaa(0.5)
    	self.assertEqual(str(self.kortti), "Kortilla on rahaa 4.0 euroa")
