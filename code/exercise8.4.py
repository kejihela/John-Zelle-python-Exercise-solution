def main():
    print("This program is to print the syracuse function ")
    syracuse = int(input("please input your syracuse value "))
    syracuse_sequence = []
    syracuse_sequence.append(syracuse)
    while syracuse > 1:
        if syracuse%2==0:
            syracuse = syracuse/2
            syracuse_sequence.append(syracuse)
        else:
            syracuse = (3*syracuse)+1
            syracuse_sequence.append(syracuse)
    print(syracuse_sequence)
main()
            
        

    
