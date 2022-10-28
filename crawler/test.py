import shelve

if __name__ == "__main__":
    with shelve.open('frontier.shelve') as db:
        for key, val in db.items():
            if "pdf" in val[0]:
                print(val)