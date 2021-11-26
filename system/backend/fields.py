from .models import Book, Student, Reservation, Issue


def book_fields():
    FIELDS_BOSNIAN, FIELDS_ENGLISH = [], []
    for data in Book._meta.get_fields():
        if data.name == "id":
            FIELDS_BOSNIAN.append("ID")
            FIELDS_ENGLISH.append("ID")
        elif data.name == "name":
            FIELDS_BOSNIAN.append("Naziv djela")
            FIELDS_ENGLISH.append("Book name")
        elif data.name == "author":
            FIELDS_BOSNIAN.append("Autor djela")
            FIELDS_ENGLISH.append("Author")
        elif data.name == "year":
            FIELDS_BOSNIAN.append("Godina izdanja")
            FIELDS_ENGLISH.append("Year")
        elif data.name == "quantity":
            FIELDS_BOSNIAN.append("Dostupno")
            FIELDS_ENGLISH.append("Quantity")

    return FIELDS_BOSNIAN, FIELDS_ENGLISH


def student_fields():
    FIELDS_BOSNIAN, FIELDS_ENGLISH = [], []
    for data in Student._meta.get_fields():
        if data.name == "id":
            FIELDS_BOSNIAN.append("ID")
            FIELDS_ENGLISH.append("ID")
        elif data.name == "first_name":
            FIELDS_BOSNIAN.append("Ime")
            FIELDS_ENGLISH.append("First name")
        elif data.name == "last_name":
            FIELDS_BOSNIAN.append("Prezime")
            FIELDS_ENGLISH.append("Last name")
        elif data.name == "classes":
            FIELDS_BOSNIAN.append("Razred")
            FIELDS_ENGLISH.append("Class")
        
    return FIELDS_BOSNIAN, FIELDS_ENGLISH


def reservation_fields():
    FIELDS_BOSNIAN, FIELDS_ENGLISH = [], []
    for data in Reservation._meta.get_fields():
        
        if data.name == "id":
            FIELDS_BOSNIAN.append("ID")
            FIELDS_ENGLISH.append("ID")
        elif data.name == "startDate":
            FIELDS_BOSNIAN.append("Početak rezervacije")
            FIELDS_ENGLISH.append("Reservation start")
        elif data.name == "endDate":
            FIELDS_BOSNIAN.append("Kraj rezervacije")
            FIELDS_ENGLISH.append("Reservation end")
        elif data.name == "professor":
            FIELDS_BOSNIAN.append("Profesor")
            FIELDS_ENGLISH.append("Professor")
        elif data.name == "book":
            FIELDS_BOSNIAN.append("Knjiga")
            FIELDS_ENGLISH.append("Book")
        elif data.name == "quantity":
            FIELDS_BOSNIAN.append("Rezervisano")
            FIELDS_ENGLISH.append("Quantity")
        elif data.name == "returned":
            FIELDS_BOSNIAN.append("Vraćeno knjiga")
            FIELDS_ENGLISH.append("Returned books")
        elif data.name == "issued":
            FIELDS_BOSNIAN.append("Izdano knjiga")
            FIELDS_ENGLISH.append("Issued books")
        elif data.name == "returnStatus":
            FIELDS_BOSNIAN.append("Status rezervacije")
            FIELDS_ENGLISH.append("Return status")
        
    return FIELDS_BOSNIAN, FIELDS_ENGLISH

def issue_fields():
    FIELDS_BOSNIAN, FIELDS_ENGLISH = [], []
    for data in Issue._meta.get_fields():
        if data.name == "id":
            FIELDS_BOSNIAN.append("ID")
            FIELDS_ENGLISH.append("ID")
        elif data.name == "reservation":
            FIELDS_BOSNIAN.append("Rezervacija")
            FIELDS_ENGLISH.append("Reservation")
        elif data.name == "student":
            FIELDS_BOSNIAN.append("Učenik")
            FIELDS_ENGLISH.append("Student")
        elif data.name == "leaseDate":
            FIELDS_BOSNIAN.append("Datum iznajmljivanja")
            FIELDS_ENGLISH.append("Lease date")
        elif data.name == "returnDate":
            FIELDS_BOSNIAN.append("Datum vraćanja")
            FIELDS_ENGLISH.append("Return date")
        elif data.name == "returnStatus":
            FIELDS_BOSNIAN.append("Vraćeno")
            FIELDS_ENGLISH.append("Return status")
        elif data.name == "debt":
            FIELDS_BOSNIAN.append("Dug")
            FIELDS_ENGLISH.append("Debt")
        
    return FIELDS_BOSNIAN, FIELDS_ENGLISH