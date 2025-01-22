import argparse
import os
import hashlib
from tqdm import tqdm

def get_file_size(filepath):
    return os.path.getsize(filepath)

def get_file_hash(filepath):
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main(reference_dir, candidates_dir, approximate=False):
    # Get reference files
    refdict = {}
    all_ref_files = []
    for root, _, files in os.walk(reference_dir):
        all_ref_files.extend([os.path.join(root, f) for f in files])
    
    for filename in tqdm(all_ref_files, desc="Processing reference files"):
        filepath = os.path.abspath(filename)
        refdict[filepath] = get_file_size(filepath)

    # Get candidate files
    candidict = {}
    all_cand_files = []
    for root, _, files in os.walk(candidates_dir):
        all_cand_files.extend([os.path.join(root, f) for f in files])
    
    for filename in tqdm(all_cand_files, desc="Processing candidate files"):
            filepath = os.path.abspath(os.path.join(root, filename))
            if filepath not in refdict:  # Skip if file is in reference dict
                candidict[filepath] = get_file_size(filepath)

    # Match files by size
    sizematchdict = {}
    for ref_path, ref_size in refdict.items():
        if approximate:
            matches = [cand_path for cand_path, cand_size in candidict.items() 
                      if abs(cand_size - ref_size) <= (ref_size * 0.01)]  # 1% tolerance
        else:
            matches = [cand_path for cand_path, cand_size in candidict.items() 
                      if cand_size == ref_size]
        if matches:
            sizematchdict[ref_path] = matches

    # Match files by hash for those with same size
    hashmatchdict = {}
    for ref_path, candidate_paths in tqdm(sizematchdict.items(), desc="Comparing file hashes"):
        ref_hash = get_file_hash(ref_path)
        hash_matches = []
        for cand_path in candidate_paths:
            if get_file_hash(cand_path) == ref_hash:
                hash_matches.append(cand_path)
        if hash_matches:
            hashmatchdict[ref_path] = hash_matches

    # Print summary
    print("\nMatching Files Summary:")
    print("-----------------------")
    if not hashmatchdict:
        print("No matching files found.")
    else:
        for ref_path, matches in hashmatchdict.items():
            print(f"\nReference file: {ref_path}")
            if len(matches) == 1:
                print(f"Found one match: {matches[0]}")
            else:
                print(f"Found {len(matches)} matches:")
                for match in matches:
                    print(f"  - {match}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Match files between directories based on size')
    parser.add_argument('reference_dir', help='Directory containing reference files')
    parser.add_argument('candidates_dir', help='Directory containing candidate files to match')
    parser.add_argument('--approximate', action='store_true', 
                      help='Enable approximate size matching with 1% tolerance')
    
    args = parser.parse_args()
    main(args.reference_dir, args.candidates_dir, args.approximate)
