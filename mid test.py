

def main():
    adress_book = {}
    while True :
        user = display_menu();
        if user ==1:
            name, number =get_contact()
            adress_book["Kim"]= "010-1111-1234"
        elif user ==2:
            name, number =get_contact()
            adress_book["Park"]= "010-222-2345"
        elif user ==3:
            name, number = get_contact()
            adress_book["Lee"]= "010-333-3456"


def get_contact():
    name = input("이름: ")
    number = input("전화번호: ")
    return name, number
def display_menu() :
    print("1.연락처 검색")
    select = int(input("메뉴 항목을 선택하시오: "))
    return select

main()
            

