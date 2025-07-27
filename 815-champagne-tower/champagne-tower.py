class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize the top row with the total poured amount
        previous_row = [poured]

        # Build each row from 1 up to query_row
        for row in range(1, query_row + 1):
            # Prepare a new row with row+1 glasses, initially empty
            current_row = [0.0] * (row + 1)
            # For each glass in the previous row, compute overflow
            for glass_index in range(row):
                overflow = previous_row[glass_index] - 1.0
                if overflow > 0:
                    # Split the overflow equally to the two glasses below
                    current_row[glass_index] += overflow * 0.5
                    current_row[glass_index + 1] += overflow * 0.5
            # Move on: current becomes previous for next iteration
            previous_row = current_row

        # The amount in the target glass cannot exceed 1
        return min(1.0, previous_row[query_glass])