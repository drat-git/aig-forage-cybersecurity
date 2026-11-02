"""Dictionary attack exercise adapted from the Forage AIG starter template."""

from zipfile import ZipFile, BadZipFile
from zlib import error as ZlibError


def attempt_extract(zf_handle, password):
    """Try one password as bytes; return whether ZIP extraction succeeds."""
    try:
        zf_handle.extractall(path="recovered", pwd=password)
    except (RuntimeError, BadZipFile, ZlibError):
        return False

    return True


def main():
    print("[+] Beginning bruteforce")

    with ZipFile("enc.zip") as zf:
        with open("rockyou.txt", "rb") as f:
            for line in f:
                password = line.rstrip(b"\r\n")

                if attempt_extract(zf, password):
                    print(
                        "[+] Password found:",
                        password.decode("utf-8", errors="replace")
                    )
                    print("[+] Files extracted to the recovered folder")
                    return

    print("[-] Password not found in list")


if __name__ == "__main__":
    main()
