import movie_svc
import requests.exceptions


def main():
    print_header()
    search_event_loop()


def print_header():
    print("-------------------------------")
    print('        Movie Search App')
    print("-------------------------------")


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input('Movie search text (x to exit): ')
            if search != 'x':
                results = movie_svc.find_movies(search)
                print("Found {} results.".format(len(results)))
                for r in results:
                    print('{} -- {}'.format(
                        r.year, r.title
                    ))
                print()
        # python looks at errors from top to bottom and executes the first match
        except ValueError as ve:
            print(ve)
        except requests.exceptions.ConnectionError:
            print("Error: Your network is down.")
        except Exception as x:
            print("Unexpected error. Details: {}".format(x))

    print('exiting...')


if __name__ == '__main__':
    main()
