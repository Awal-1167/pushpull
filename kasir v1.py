harga_barang= int(input("harga per baju baru"))

if (harga_barang < 50000):
	print("harganya segitu bang Rp.",harga_barang)


elif harga_barang >= 50000 :
	persentase_diskon = int(input("diskon 20000 "))
	if (harga_barang > 50000):
		harga_diskon = harga_barang * persentase_diskon/100 
		harga_akhir = harga_barang - harga_diskon
		
		print(f"harga diskon nah Rp.{harga_akhir}")

	if (harga_barang > 100000):
		harga_diskon = harga_akhir * 10/100
		harga_akhir = harga_akhir - harga_diskon
		
		print(f"udah sama diskon 10% nih segini Rp.{harga_akhir}")