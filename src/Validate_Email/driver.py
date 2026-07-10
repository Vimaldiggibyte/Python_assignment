from util import filter_emails


def main():
    n = int(input())

    emails = []

    for _ in range(n):
        emails.append(input())

    print(filter_emails(emails))


if __name__ == "__main__":
    main()
