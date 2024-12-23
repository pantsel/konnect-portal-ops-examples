import pytest
from src.kptl.helpers.utils import read_file_content, encode_content, sort_key_for_numbered_files, slugify

def test_read_file_content(tmpdir):
    # Create a temporary file
    file = tmpdir.join("test_file.txt")
    file.write("Test content")

    # Read the file content using the function
    content = read_file_content(str(file))

    assert content == b"Test content"

def test_encode_content():
    # Test encoding a string
    content = "test content"
    encoded_content = encode_content(content)
    assert encoded_content == "dGVzdCBjb250ZW50"

    # Test encoding bytes
    content_bytes = b"test content"
    encoded_content_bytes = encode_content(content_bytes)
    assert encoded_content_bytes == "dGVzdCBjb250ZW50"

def test_sort_key_for_numbered_files():
    # Test sorting with numeric prefixes
    filenames = ["1_file.md", "2.1_file.md", "2_file.md", "10_file.md", "file.md"]
    sorted_filenames = sorted(filenames, key=sort_key_for_numbered_files)
    assert sorted_filenames == ["1_file.md", "2_file.md", "2.1_file.md", "10_file.md", "file.md"]

    # Test sorting with non-numeric prefixes
    filenames = ["file.md", "another_file.md"]
    sorted_filenames = sorted(filenames, key=sort_key_for_numbered_files)
    assert sorted_filenames == ["file.md", "another_file.md"]

def test_slugify():
    # Test slugifying a title
    title = "This is a Test Title!"
    slug = slugify(title)
    assert slug == "this-is-a-test-title"

    # Test slugifying a title with special characters
    title = "Title with special characters: @#&*()!"
    slug = slugify(title)
    assert slug == "title-with-special-characters"