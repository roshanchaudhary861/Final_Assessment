import sys

def analyze_file(filename):
    correct_cat = "OURS"
    total_entries = 0
    total_time = 0
    other_cat_count = 0
    other_cat_with_water = 0
    correct_cat_entries = []
    with open(filename) as f:
        for line in f:
            if line.strip() == "END":
                break
            cat, entry_time, exit_time = line.strip().split(",")
            entry_time = int(entry_time)
            exit_time = int(exit_time)
            duration = exit_time - entry_time
            if cat == correct_cat:
                total_entries += 1
                total_time += duration
                correct_cat_entries.append(duration)
            else:
                other_cat_count += 1
                if duration < 2:
                    other_cat_with_water += 1
    if total_entries == 0:
        print("No entries for the correct cat found.")
    else:
        print(f" Log File Analysis\n","="*18,"\n")
        print(f"Cat Visits:   {total_entries}")
        print(f"other Visits: {other_cat_count}","\n")
        
        print(f"Total Time in House: {int(total_time/60)} hours, {int(total_time//60)} minutes","\n")
        print(f"Average Visit Length: {int(total_time / total_entries)} minutes")
        print(f"Longest Visit:        {max(correct_cat_entries)} minutes")
        print(f"Shortest Visit:       {min(correct_cat_entries)} minutes","\n")
        print("```")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing command line argument!")
    else:
        try:
            analyze_file(sys.argv[1])
        except FileNotFoundError:      
            print(f"Cannot open""!")
