fires = input().split("#")
amount_of_water = int(input())
total_fire = 0
total_effort = 0
high = range(81, 126)
medium = range(51, 81)
low = range(1, 51)
fireout_cells = []

for cell in fires:
    type_of_fire, cell_value = cell.split(" = ")
    cell_value = int(cell_value)
    if type_of_fire == "High":
        if cell_value in high:
            if cell_value <= amount_of_water:
                amount_of_water -= cell_value
                total_effort += cell_value * 0.25
                total_fire += cell_value
                fireout_cells.append(cell_value)
    elif type_of_fire == "Medium":
        if cell_value in medium:
            if cell_value <= amount_of_water:
                amount_of_water -= cell_value
                total_effort += cell_value * 0.25
                total_fire += cell_value
                fireout_cells.append(cell_value)
    elif type_of_fire == "Low":
        if cell_value in low:
            if cell_value <= amount_of_water:
                amount_of_water -= cell_value
                total_effort += cell_value * 0.25
                total_fire += cell_value
                fireout_cells.append(cell_value)

print("Cells:")
for cells in fireout_cells:
    print(f" - {cells}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")


