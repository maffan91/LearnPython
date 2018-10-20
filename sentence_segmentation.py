import helper_functions as helper

document = "This is called indexing. You use an index to fetch an element. All sequences can be indexed in this way. When you use a negative index, Python counts from the right; that is, from the last element. The last element is at position –1 (not –0, as that would be the same as the first element):"
v = helper.build_vocabulary(document)
print(helper.split_sentences(document))
