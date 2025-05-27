from lib.db.seed import seed_data



def display_author_profile(author):
    print(f"Author: {author.name}")
    
    

def main():
    author, magazines = seed_data()
    display_author_profile(author)

    print("\n[Add New Article]")
    print("------------------")
    title = input("Title: ").strip()

    print("Magazine:")
    for i, mag in enumerate(magazines):
        print(f"{i + 1}. {mag.name}")
    mag_choice = int(input("Select Magazine [1/2/...]: ")) - 1

    Article(title, magazines[mag_choice], author)

    print("\n[Updated Author Profile]\n")
    display_author_profile(author)

if __name__ == "__main__":
    main()
