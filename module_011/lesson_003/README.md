# Lesson 3: Batch File Renaming

## Overview

Renaming a large number of files manually is tedious and error-prone. In this lesson, you will learn:

   - How to use Python to batch rename files in a directory automatically.

   - Methods to construct new file names (for example, adding a common prefix or suffix, or replacing parts of the name).

   - The importance of verifying and possibly backing up files before bulk operations, to avoid accidental data loss.

### Detailed Explanation

- **Listing and Filtering Files:**

    Python's `os.listdir()` function returns all entries in a given directory. You can combine this with `os.path.isfile()` to filter only files (ignoring subfolders). If you only want to rename files of a certain type (e.g., only `.cfg` configuration files), you can check that the filename ends with that extension before renaming.

- **Renaming Files Programmatically:**

    The `os.rename(src, dst)` function (or equivalently, `pathlib.Path.rename`) is used to rename a file from the `src` name to the `dst` name. To batch rename, you can loop over each file and generate a new name for it. For example, to add a prefix "old_" to every filename, you can set `new_name = "old_" + filename`. To change an extension or add a suffix, you might do something like `new_name = filename + ".bak"` (appending a suffix).

- **Safety Considerations:**

    When renaming multiple files, especially in bulk, it's wise to double-check your logic on a small sample or test directory first. Ensure the new names don't conflict with existing filenames in the directory. A good practice is to print out the proposed new names (a "dry run") before actually renaming, so you can confirm the changes. Also, if something goes wrong or the script is interrupted mid-way, you might end up with partially renamed files – so consider that in a real-world scenario (for this lesson's simple scripts, we'll assume it runs to completion).

## Objectives

- Learn to retrieve and iterate over file names in a directory using Python.

- Construct new file names according to a specified rule (such as adding a prefix/suffix or altering the extension).

- Implement a Python script that renames a batch of files automatically, and test it on a sample directory to ensure it works as expected.

## Instructions

1. Read the explanation to understand how Python can be used to gather file names and rename files. Think about a scenario in your work (for example, updating configuration file names to include a date or device name) where this could be useful.

2. Run the `batch_rename_configs.py` script. This example will ask you for a target directory path and a prefix string. It will then go through that directory and rename each file by adding the given prefix to the beginning of the filename. Try it out in a test folder with some sample files (you can create a few dummy files to see how it works). After running, use your file explorer or `ls` command to verify the files have new names.

3. Practice Exercise: Modify the `batch_rename_configs.py` script to implement different renaming rules. For instance, you could change it to add a suffix instead of a prefix (e.g., rename `config1.txt` to `config1_backup.txt`), or to only rename files with a certain extension (hint: check `if filename.endswith('.cfg'):` inside the loop). Another idea is to use numbering – for example, rename files to `file1.txt`, `file2.txt`, ... and so on. Test your modified script on a safe set of files to ensure it behaves as expected.