from statistics import covariance


def hitung(tinggi_badan, berat_badan):
    
    convert = tinggi_badan/100
    
    jumlah_beban = berat_badan / (convert * convert)

    limit_float = round(jumlah_beban, 2) # limit menampilkan angka di belakang koma
    
    if limit_float < 17:
        return (limit_float, "Kurus, kekurangan berat badan berat") #return tuple
    
    elif 17 < limit_float < 18.4:
        return (limit_float, "Kurus, kekurangan berat badan ringan")

    elif  18.5 <  limit_float < 25:
        return (limit_float, "normal, berat badan ideal")

    elif 25.1 < limit_float < 27:
        return (limit_float, "Gemuk, kelebihan berat badan tingkat ringan")


    