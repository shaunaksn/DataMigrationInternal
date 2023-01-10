import sqlizer
import os


def schema_detection(file_type, file_path, table_name, database_type):
    """
    This function is used for detecting the source schema and generating target DDL(schema detection)
    parameters :
    1. file_type : type of the input source file
    2. file_path : absolute location path of the source file
    3. table_name : expected name of the target table
    4. database_type : target database system
    """
    with open(file_path, mode='rb') as file_content:
        converter = sqlizer.File(file_content, database_type, file_type, file_path, table_name)
        converter.convert(wait=True)
        output_sql = converter.download_result_file().text.split('INSERT')[0].replace(' CHARACTER SET utf8', '')
        print(output_sql)


if __name__ == '__main__':
    """ 
    Accepting input parameters and calling the schema_detection function
    """
    while True:
        fileType = input('Enter file type from the following: '
                         'xlsx, xls, csv, txt, xml, json \n').lower()

        if fileType not in ['xlsx', 'xls', 'csv', 'txt', 'xml', 'json']:
            print('Enter valid file type.\n')
            continue
        else:
            break

    while True:
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
    databaseType = 'SQLServer'

    schema_detection(fileType, abs_file_path, tableName, databaseType)
