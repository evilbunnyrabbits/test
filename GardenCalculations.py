bag_volume = 2
east_side = 27
west_side = 60.5
north_side = 37

def calculate_volume(length, width, height):
    length = length
    width = width
    height = height
    volume = length * width * height
    return volume

def convert_cubic_inch_to_foot(cubic_inches):
    cubic_inches = cubic_inches
    cubic_feet = cubic_inches/1728
    return cubic_feet

#mulch
west = calculate_volume(length=726, width=36, height=1.5)
north = calculate_volume(length=444, width=36, height=1)
east = calculate_volume(length=324, width=36, height=1)

#garden beds
garden_bed_inches = calculate_volume(length=48, width=47.9, height=12)
garden_bed_feet = convert_cubic_inch_to_foot(cubic_inches=garden_bed_inches)

mulch_total_volume_inches = west + north + east
mulch_total_volume_feet = convert_cubic_inch_to_foot(mulch_total_volume_inches)

#elevated garden bed:
e_garden_bed = calculate_volume(length=46, width=13, height=13)
e_garden_bed_feet = convert_cubic_inch_to_foot(cubic_inches=e_garden_bed)
e_garden_bed_bags_needed = round(e_garden_bed_feet / 2)
print('Elevated Garden Bed Volume = {} square feet'.format(e_garden_bed_feet, 2))
print('Total bags\'s needed: ' + str(e_garden_bed_bags_needed))
print()

#laurel purchases
total_circumference = west_side + north_side + east_side
laurel_spacing = 4
total_laurels_needed = total_circumference/laurel_spacing
print('Total circumference: ' + str(total_circumference) + '\'')
print('Total Laurel\'s needed: ' + str(round(total_laurels_needed)))
print()

print('Mulch Project')
print('Total volume = ' + str(mulch_total_volume_feet) + ' cubic feet')
print('You will need to purchase ' + str(round(mulch_total_volume_feet/bag_volume)) + ' bags of material')
print()

print('Garden Beds Project')
print('Total volume = ' + str(round(garden_bed_feet, 2)))
print('You will need to purchase ' + str(round(garden_bed_feet/bag_volume)) + ' bags of material per planter')