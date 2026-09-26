import garden_math as g
#or from garden_math import side_length, whole_side_length

def main() -> None:
    """Ask for garden areas and display their side lengths."""
  
    number_of_gardens = int(input("How many gardens? "))

    for i in range(number_of_gardens):
        area = float(input("Enter the area of garden " + str(i + 1)+": "))
        if area < 0:
            print("Error: Area cannot be negative.")
        else:
            print("Side length:", g.side_length(area))
            print("Whole side length:", g.whole_side_length(area))

main()
