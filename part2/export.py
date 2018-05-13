import reports

answers = [reports.get_most_played(file_name), reports.sum_sold(file_name),reports.get_selling_avg(file_name),reports.count_longest_title(file_name), reports.get_date_avg(file_name),get_game(file_name, title) ]

with open(export_file, 'w') as export:
    for answer in answers:
        export.write(str(answer) + '\n')
# Export functions
