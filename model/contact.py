from sys import maxsize

class Contact:

    def __init__(self, home = None, all_phones_from_home_page = None,all_email_from_home_page = None, firstname = None, middlename = None, email = None, lastname = None, nickname = None, title = None, company = None, address = None, homephone = None, mobilephone = None, workphone = None, fax = None, email2 = None, email3 = None , homepage = None , byear = None , ayear = None, address2 = None, secondaryphone = None, notes = None, id = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.all_email_from_home_page = all_email_from_home_page
        self.home = home

    def __repr__(self):
        return '%s:%s:%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s' % (self.id, self.firstname, self.lastname, self.middlename,self.nickname,self.title,self.company,
                                                        self.address,self.homephone, self.mobilephone, self.workphone, self.fax, self.email, self.email2,
        self.email3,self.homepage, self.byear, self.ayear, self.address2,self.secondaryphone,self.notes)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and\
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
