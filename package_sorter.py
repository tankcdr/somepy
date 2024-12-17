# Function to determine which stack a package belongs to
def sort(width, height, length, mass):
     # Define thresholds
    BULKY_VOLUME_THRESHOLD = 1000000  # cm³
    BULKY_DIMENSION_THRESHOLD = 150   # cm
    HEAVY_MASS_THRESHOLD = 20         # kg

    # Calculate the package volume
    volume = width * height * length

    # Determine if the package is bulky
    is_bulky = (volume >= BULKY_VOLUME_THRESHOLD) or \
               (width >= BULKY_DIMENSION_THRESHOLD or 
                height >= BULKY_DIMENSION_THRESHOLD or 
                length >= BULKY_DIMENSION_THRESHOLD)

    # Determine if the package is heavy
    is_heavy = mass >= HEAVY_MASS_THRESHOLD

    # Apply the dispatch rules
    if is_bulky and is_heavy:
        return "REJECTED"  # Both bulky and heavy
    elif is_bulky or is_heavy:
        return "SPECIAL"   # Either bulky or heavy
    else:
        return "STANDARD"  # Neither bulky nor heavy


# Test Cases
if __name__ == "__main__":
    # Example tests
    print(sort(100, 50, 200, 30))  # REJECTED (Both bulky and heavy)
    print(sort(150, 150, 150, 25)) # REJECTED (Both bulky and heavy)
    print(sort(50, 50, 50, 10))    # STANDARD (Neither bulky nor heavy)
    print(sort(100, 100, 100, 20)) # REJECTED (Both bulky and heavy)
    print(sort(10, 10, 10, 5))     # STANDARD (Neither bulky nor heavy)
    print(sort(200, 50, 50, 15))   # SPECIAL (Bulky but not heavy)