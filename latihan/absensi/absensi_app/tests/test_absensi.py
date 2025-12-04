from services.absensi_service import hitung_kehadiran

def test_hitung_kehadiran():
    assert hitung_kehadiran(5, 5) == 50
    assert hitung_kehadiran(10, 0) == 100
    assert hitung_kehadiran(0, 10) == 0
    assert hitung_kehadiran(0, 0) == 0
