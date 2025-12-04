def hitung_kehadiran(hadir, sakit):
    total = hadir + sakit
    if total == 0:
        return 0
    return (hadir / total) * 100
