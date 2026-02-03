import sys


# 1. Custom Exception එකක් සෑදීම
class DatabaseConnectionError(Exception):
    """දත්ත ගබඩාවට සම්බන්ධ වීමට නොහැකි වූ විට ඇතිවන error එක."""

    def __init__(self, message, db_name):
        self.message = message
        self.db_name = db_name
        super().__init__(self.message)


def connect_to_db(db_name):
    # උපකල්පනය කරමු DB එකේ නම වැරදි නම් error එකක් එනවා කියලා
    if db_name != "Production_DB":
        raise DatabaseConnectionError("සම්බන්ධ වීමට නොහැක", db_name)
    print(f"Connected to {db_name}")


def main():
    db = "Test_DB"

    try:
        connect_to_db(db)
    except DatabaseConnectionError as e:
        print(f"Custom Error: {e.message} in {e.db_name}")
        # Exception Chaining: මුල් error එකත් සමඟ අලුත් error එකක් පෙන්වීම
        # raise RuntimeError("Database connection failed") from e
    except Exception as e:
        print(f"Generic error: {e}")
    else:
        print("දත්ත ගබඩාව සාර්ථකව සම්බන්ධ විය!")
    finally:
        print("ක්‍රියාවලිය අවසන්. (Cleaning up resources...)")


if __name__ == "__main__":
    main()