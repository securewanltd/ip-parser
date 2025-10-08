def split_ip_list(input_file, lines_per_file=130000, output_prefix="custom-list-part"):
    with open(input_file, 'r') as infile:
        file_count = 1
        current_lines = []

        for i, line in enumerate(infile, 1):
            current_lines.append(line)
            if i % lines_per_file == 0:
                output_file = f"{output_prefix}{file_count}.txt"
                with open(output_file, 'w') as outfile:
                    outfile.writelines(current_lines)
                print(f"{output_file} yazıldı. ({len(current_lines)} satır)")
                current_lines = []
                file_count += 1

        # Kalan satırları da yaz
        if current_lines:
            output_file = f"{output_prefix}{file_count}.txt"
            with open(output_file, 'w') as outfile:
                outfile.writelines(current_lines)
            print(f"{output_file} yazıldı. ({len(current_lines)} satır)")

# Kullanım
split_ip_list("ip-list.txt")
