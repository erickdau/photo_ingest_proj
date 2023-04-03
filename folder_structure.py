def folder_struc(choice, datastr):

    if choice == 1:  # YYYY-MM-DD
        return datastr[0:4] + '-' + datastr[5:7] + '-' + datastr[8:10]

    elif choice == 2:  # MM-DD
        return datastr[5:7] + '-' + datastr[8:10]

    elif choice == 3:  # YYYY/MM/DD
        return datastr[0:4] + '/' + datastr[5:7] + '/' + datastr[8:10]

    elif choice == 4:  # YYYYMMDD
        return datastr[0:4] + datastr[5:7] + datastr[8:10]
