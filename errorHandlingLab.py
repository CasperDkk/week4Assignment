def read_and_modify_file(input_filename, output_filename):
    try:
        # Attempt to open the input file for reading
        with open(input_filename, 'r') as infile:
            # Read lines from the input file
            lines = infile.readlines()

        # Modify the content (e.g., convert to uppercase)
        modified_lines = [line.upper() for line in lines]

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"Modified content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Ask the user for the input filename
    input_filename = input("Enter the filename to read from (e.g., 'input.txt'): ")
    
    # Specify the output filename
    output_filename = "output.txt"
    
    # Call the function to read and modify the file
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()