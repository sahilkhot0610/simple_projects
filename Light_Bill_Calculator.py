units = int(input("Enter the number of units used : "))

vij_aakar_1 = 3.96
indhan_aakar_1 = 0.350
vij_aakar_2 = 10.80
indhan_aakar_2 = 0.650
vij_aakar_3 = 15.03
indhan_aakar_3 = 0.850

def vij_1(units):
    vij_aakar = 0
    indhan_aakar = 0
    vij_aakar = vij_aakar_1 * units
    indhan_aakar = indhan_aakar_1 * units

    return vij_aakar, indhan_aakar

def vij_2(units):
    vij_aakar = 0
    indhan_aakar = 0

    vij_aakar += (100 * vij_aakar_1) 
    indhan_aakar += indhan_aakar_1 * 100

    units_remaining = units - 100
    vij_aakar += (units_remaining * vij_aakar_2)
    indhan_aakar += indhan_aakar_2 * units_remaining
    return vij_aakar, indhan_aakar

def vij_3(units):
    vij_aakar = 0
    indhan_aakar = 0

    vij_aakar += (100 * vij_aakar_1) 
    indhan_aakar = indhan_aakar_1 * 100

    vij_aakar += (200 * vij_aakar_2)
    indhan_aakar += indhan_aakar_2 * 200

    units_remaining = units - 300
    vij_aakar += (units_remaining * vij_aakar_3)
    indhan_aakar += indhan_aakar_3 * units_remaining

    return vij_aakar, indhan_aakar

def grand_total(units):
    stir_aakar = 140.00
    vahan_aakar = 1.60 * float(units)
    if(units <= 100):
        total_vij, total_indhan = vij_1(units)

    elif(units <= 300 and units > 100):
        total_vij, total_indhan = vij_2(units)

    elif(units > 300 and units <= 500):
        total_vij, total_indhan = vij_3(units)

    total_before_tax = stir_aakar + total_vij + total_indhan + vahan_aakar
    vij_shukla = 0.16 * total_before_tax
    total_amount = total_before_tax + vij_shukla 

    print(f"stri aakar : {stir_aakar}")
    print(f"vij aakar : {total_vij}")
    print(f"vahan aakar : {vahan_aakar}")
    print(f"indhan aakar : {total_indhan}")
    print(f"vij shukla : {vij_shukla}")

    print(f"Total amount : {total_amount}")
    
grand_total(units)




    

