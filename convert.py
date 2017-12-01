if __name__ == '__main__':
    with open('contacts.csv', 'r') as file:
        csv = file.read()

    contacts = csv.split('\n')
    contacts = [contact.split(',') for contact in contacts]
    print(contacts)

    contacts = contacts[:-1]

    header = contacts[0]
    contacts = contacts[1:]

    carPhoneIdx = header.index('Car Phone')
    homePhoneIdx = header.index('Home Phone')
    businessPhoneIdx = header.index('Business Phone')

    print(carPhoneIdx, homePhoneIdx, businessPhoneIdx)

    for contact in contacts:
        nr = contact[carPhoneIdx]
        if nr != '':
            if contact[homePhoneIdx] == '':
                contact[homePhoneIdx] = nr
                contact[carPhoneIdx] = ''
                print('moved to home')
                continue
            elif contact[businessPhoneIdx] == '':
                contact[businessPhoneIdx] = nr
                contact[carPhoneIdx] = ''
                print('moved to business')
                continue
            else:
                print('failed on')
                print(contact)
                exit(1)

    with open('contacts_converted.csv', 'w') as file:
        file.write(','.join(header))
        for line in contacts:
            file.write('\n')
            file.write(','.join(line))
