# Initialize variables
total_boxes = 0
remaining_candles = 0

# Loop from age 1 to 100
for age in range(1, 101):
    # Calculate the number of candles needed for the current year
    candles_needed = age

    # Check if there are remaining candles from previous years
    if remaining_candles >= candles_needed:
        remaining_candles -= candles_needed
    else:
        # Calculate how many boxes to buy and update the remaining candles
        # Round up to the nearest box
        boxes_to_buy = (candles_needed - remaining_candles + 23) // 24
        total_boxes += boxes_to_buy
        remaining_candles = (boxes_to_buy * 24) - \
            (candles_needed - remaining_candles)

    # Print only if boxes are bought
    if boxes_to_buy > 0:
        print(f"Before birthday {age}, buy {boxes_to_buy} box(es)")

# Print the total number of boxes and
# remaining candles after celebrating the 100th birthday
print(f"Total number of boxes: {total_boxes}, \
      Remaining candles: {remaining_candles}")
