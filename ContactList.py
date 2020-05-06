class ContactList(list):
    def search_by_name(self, name):
        namelist = []
        for self.name in self:
            if name in self.name:
                namelist.append(self.name)
        return namelist
                
all_contacts = ContactList(input('Введите список имен через запятую: ').split(','))
print(all_contacts.search_by_name(input('Введите имя для списка: ')))


