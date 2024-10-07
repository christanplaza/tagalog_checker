from tagalog_checker.checker import check_file_for_tagalog_terms

result = check_file_for_tagalog_terms('positive_example.txt')
print(result)

result = check_file_for_tagalog_terms('negative_example.txt')
print(result)
