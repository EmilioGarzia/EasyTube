#!/bin/bash

# check the ffmpeg is installed function
function check_ffmpeg(){
    command -v ffmpeg > /dev/null 2>&1 || { echo >&2 "ffmpeg is not installed, please install ffmpeg and restart this converter."; exit 1; }
}

# conversion function using ffmpeg
function ffmpeg_conversion(){
    file=$1                                 # full path of input file
    dir=$2                                  # input directory
    file_basename=$(basename -- $file)      # basename of the input file

    # Convert audio file in mp3 file with ffmpeg
    ffmpeg -i "${file}" -vn -acodec libmp3lame -ar 44100 -ac 2 -b:a 192k "${directory}/Converted/$file_basename"
}

# funct
function remove_space_in_name(){
    directory = $1

    for file in "$directory"/*; do
        if [ -e "$file" ]; then
            original_file_name=$(basename "$file")

            if [[ "$original_file_name" == *" "* ]]; then
                new_file_name=$(echo "$original_file_name" | tr ' ' '_')
                new_path="$directory/$new_file_name"
                mv "$file" "$new_path"
            fi
        fi
    done
}

check_ffmpeg

# input directory
directory=$1

remove_space_in_name "$directory"

# Create output directory if not exist
mkdir -p "${directory}/Converted"

# Iterate all file in the input directory and covert them into Converted directory
for input_file in "$directory"/*; do
    # the conversion function must be runned in background "&"
    ffmpeg_conversion "${input_file}" $directory &
done

# wait all background process are terminated
wait

# Goodbye Message
echo "All files are converted!" 
echo "Press ENTER to close Converter..."
read 