def main():
    print("wind speed problem program")
    for T, V in zip(range(-20, 70, 10), range(5, 50, 5)):
        answer = 35.74+0.6215*T-35.75*V**0.16+0.4275*T*V**0.16
        print(answer)
main()
        
                    
