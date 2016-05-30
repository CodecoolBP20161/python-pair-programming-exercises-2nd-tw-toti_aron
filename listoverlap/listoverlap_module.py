def listoverlap(list1, list2):
    common_elements = []
    for i in list1:
        for j in list2:
            if i == j and j not in common_elements:
                common_elements.append(j)

    return common_elements


def main():
    list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    common_elements = listoverlap(list1, list2)
    print(common_elements)
    return


if __name__ == '__main__':
    main()
