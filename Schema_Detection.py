import sqlizer
import os
import sys


def file_to_sql(file_type, file_path, table_name, database_type):
    with open(file_path, mode='rb') as file_content:
        converter = sqlizer.File(file_content, database_type, file_type, file_path, table_name)
        converter.convert(wait=True)
        output_sql = converter.download_result_file().text.split('INSERT')[0].replace(' CHARACTER SET utf8', '')
        print(output_sql)


if __name__ == '__main__':

    while (True):
        fileType = input('Enter file type from the following: '
                         'xlsx, xls, csv, txt, xml, json \n').lower()

        if fileType not in ['xlsx', 'xls', 'csv', 'txt', 'xml', 'json']:
            print('Enter valid file type.\n')
            continue
        else:
            break

    while (True):
        filePath = input('Enter File Path without the filename: ')

        os.chdir(filePath)

        fileName = input('Enter file name with extension: ')

        if os.path.isabs(filePath) is False:
            print('Enter valid file path.')
            continue
        elif os.path.isfile(fileName) is False:
            print('Enter valid file name.')
            continue
        else:
            break

    abs_file_path = os.path.abspath(filePath + '/' + fileName)
    tableName = input('Enter DDL Table name: ').upper()
    databaseType = 'MySQL'

    file_to_sql(fileType, abs_file_path, tableName, databaseType)
