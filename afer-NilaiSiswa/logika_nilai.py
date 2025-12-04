def hitung_nilai_akhir(uts: float, uas: float, tugas: float) -> float:
    """
    Menghitung nilai akhir berdasarkan bobot:
    UTS: 30%, UAS: 50%, Tugas: 20%
    """
    return (0.3 * uts) + (0.5 * uas) + (0.2 * tugas)

def tentukan_grade(nilai_akhir: float) -> str:
    """
    Menentukan grade huruf berdasarkan skor nilai akhir.
    """
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 75:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    else:
        return "D"