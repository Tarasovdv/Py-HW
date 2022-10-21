def book_logger(arr):
    with open('log.csv', 'a') as file:
        for item in arr:
            file.write('Name:  {}; Phone number {}'
                    .format((" ").join(item[0:3]), item[3]))
        file.write('\n')
        
        
def Record_contact(a):
    with open('log.csv', 'a') as file:
        file.write('Name:  {}; Phone number {}'
                    .format((" ").join(a[0:3]), a[3]))
        file.write('\n')

            