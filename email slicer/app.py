# program that takes a particular email address and slices it into the username and domain name.
#  we'll slice the domain too
# Steps: Collect email from user
# split email using the @ the save the first part as the username and the second part as domain
# split the domain using the . and save the first part as the domain name and the second part as the domain extension

def main():
    print("Welcome to Caren's email slicer program!")
    print("This program will take an email address and slice it into the username and domain name.")
    print("")
    
    email_input = input("Enter your email address: ")
    (username, domain) = email_input.split("@") # split email using the @ the save the first part as the username and the second part as domain
    (domain, extension) = domain.split(".") # split the domain using the . and save the first part as the domain name and the second part as the domain extension
    
    print("Your username is: ", username)
    print("Domain: " + domain)
    print("Extension: " , extension)

while True:
    main()