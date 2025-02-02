# MediaSizeOrHashMatcher

MediaSizeOrHashMatcher is a Python tool for finding matching files between two directories based on file size and content hash. It supports both regular files and video files with specialized video hash comparison.

## Features

- **File Size Matching**: Finds files with identical sizes between directories
- **Approximate Size Matching**: Option to match files with sizes within 1% tolerance
- **Hash Comparison**: 
  - MD5 hash for regular files
  - VideoHash for video files (MP4, AVI, MOV, MKV)
- **Parallel Processing**: Utilizes multiple CPU cores for faster hash comparison
- **Comprehensive Output**: Detailed summary of matching files

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/MediaSizeOrHashMatcher.git
cd MediaSizeOrHashMatcher
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```bash
python MediaSizeOrHashMatcher.py REFERENCE_DIR CANDIDATES_DIR [OPTIONS]
```

### Arguments

- `REFERENCE_DIR`: Directory containing reference files
- `CANDIDATES_DIR`: Directory containing candidate files to match

### Options

- `--approximate`: Enable approximate size matching with 1% tolerance
- `--videos`: Use video hash comparison for video files
- `--n_jobs`: Number of parallel jobs for hash matching (default: 3)

### Example Commands

1. Basic usage:
```bash
python MediaSizeOrHashMatcher.py /path/to/reference /path/to/candidates
```

2. With approximate size matching:
```bash
python MediaSizeOrHashMatcher.py /path/to/reference /path/to/candidates --approximate
```

3. With video hash comparison:
```bash
python MediaSizeOrHashMatcher.py /path/to/reference /path/to/candidates --videos
```

4. Using 8 parallel jobs:
```bash
python MediaSizeOrHashMatcher.py /path/to/reference /path/to/candidates --n_jobs 8
```

## Requirements

- Python 3.6+
- Required packages:
  - tqdm
  - joblib
  - videohash

## How It Works

1. **File Size Matching**:
   - Scans both directories and creates a list of files with their sizes
   - Matches files with identical sizes (or within 1% tolerance if --approximate is used)

2. **Hash Comparison**:
   - For files with matching sizes:
     - Regular files: Computes MD5 hash
     - Video files: Computes VideoHash (if --videos is enabled)
   - Compares hashes to find exact matches

3. **Parallel Processing**:
   - Uses joblib to parallelize hash computation and comparison
   - Number of parallel jobs can be controlled with --n_jobs

## Output

The program provides a detailed summary of matching files, including:
- Reference file path
- Number of matches found
- Paths of matching files

Example output:
```
Matching Files Summary:
-----------------------

Reference file: /path/to/reference/video.mp4
Found one match: /path/to/candidates/video_copy.mp4

Reference file: /path/to/reference/document.pdf
Found 2 matches:
  - /path/to/candidates/doc1.pdf
  - /path/to/candidates/doc2.pdf
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature/bugfix
3. Commit your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- tqdm for progress bars
- joblib for parallel processing
- videohash for video comparison
