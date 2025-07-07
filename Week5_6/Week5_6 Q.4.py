def copy_file():
    input_file = input("Enter the input file name (to read from): ")
    output_file = input("Enter the output file name (to write to): ")

    try:
        # Try to open the input file
        with open(input_file, 'r') as infile:
            content = infile.read()

        try:
            # Check if output file already exists
            with open(output_file, 'x') as outfile:
                outfile.write(content)
            print(f"\nFile copied successfully to '{output_file}'.")
        except FileExistsError:
            print(f"\nError: The file '{output_file}' already exists. Choose a different name.")

    except FileNotFoundError:
        print(f"\n Error: The file '{input_file}' does not exist. Please check the file name and try again.")

# Run the function
copy_file()
