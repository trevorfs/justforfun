import time
import os
from colorama import init, Fore, Style


init()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_lyrics(pause_time):
    lyrics = [
        ("title", "🎵 Where We Are - One Direction 🎵"),
        ("", ""),
        ("verse", "[Verse 1: Harry, Liam]"),
        ("verse", "Remember when we would stay out too late"),
        ("verse", "We were young, havin' fun, made mistakes"),
        ("verse", "Did we ever know? Did we ever know?"),
        ("verse", "Did we ever know? Yeah"),
        ("verse", "All the things we'd just think up and say"),
        ("verse", "Never wrong, always right, not afraid"),
        ("verse", "Did we ever know? Did we ever know?"),
        ("verse", "Did we ever know?"),
        ("", ""),
        ("pre-chorus", "[Pre-Chorus: Zayn]"),
        ("pre-chorus", "Is it all inside of my head?"),
        ("pre-chorus", "Maybe you still think I don't care"),
        ("pre-chorus", "But all I need is you"),
        ("pre-chorus", "Yeah, you know it's true, yeah, you know it's true"),
        ("", ""),
        ("chorus", "[Chorus: Harry, All]"),
        ("chorus", "Forget about where we are and let go"),
        ("chorus", "We're so close"),
        ("chorus", "If you don't know where to start, just hold on"),
        ("chorus", "And don't run, no"),
        ("chorus", "We're looking back, we messed around"),
        ("chorus", "But that was then and this is now"),
        ("chorus", "All we need's enough love to hold us"),
        ("chorus", "Where we are"),
        ("", ""),
        ("post-chorus", "[Post-Chorus: Harry]"),
        ("post-chorus", "But that was then and this is now"),
        ("post-chorus", "All we need is enough love to hold us"),
        ("post-chorus", "Where we are"),
        ("", ""),
        ("verse", "[Verse 2: Louis]"),
        ("verse", "Summer days rushin' by you and me"),
        ("verse", "Makes it harder to see underneath"),
        ("verse", "Did we ever know? Did we ever know?"),
        ("verse", "Did we ever know?"),
        ("", ""),
        ("pre-chorus", "[Pre-Chorus: Zayn]"),
        ("pre-chorus", "Is it all inside of my head?"),
        ("pre-chorus", "Maybe you still think I don't care"),
        ("pre-chorus", "But all I need is you"),
        ("pre-chorus", "Yeah, you know it's true, yeah, you know it's true"),
        ("", ""),
        ("chorus", "[Chorus: Harry, All]"),
        ("chorus", "Forget about where we are and let go"),
        ("chorus", "We're so close"),
        ("chorus", "If you don't know where to start, just hold on"),
        ("chorus", "And don't run, no"),
        ("chorus", "We're looking back, we messed around"),
        ("chorus", "But that was then and this is now"),
        ("chorus", "All we need's enough love to hold us"),
        ("chorus", "Where we are"),
        ("", ""),
        ("interlude", "[Interlude: Harry]"),
        ("interlude", "Where we are, where we are"),
        ("interlude", "Where we are, where we are"),
        ("", ""),
        ("bridge", "[Bridge: Niall, Louis & Harry]"),
        ("bridge", "With closed eyes and open mind"),
        ("bridge", "We can be there, we can be there"),
        ("bridge", "But this time, let's cross the line"),
        ("bridge", "Can you see it? Can you see it?"),
        ("", ""),
        ("chorus", "[Final Chorus: All, Harry, Zayn]"),
        ("chorus", "Forget about where we are and let go"),
        ("chorus", "We're so close (If you don't know)"),
        ("chorus", "If you don't know where to start, just hold on"),
        ("chorus", "And don't run, no (And don't run, no)"),
        ("chorus", "We're looking back, we messed around"),
        ("chorus", "But that was then and this is now"),
        ("chorus", "All we need's enough love to hold us"),
        ("chorus", "Where we are"),
    ]

  
    color_map = {
        "title": Fore.YELLOW + Style.BRIGHT,
        "verse": Fore.CYAN,
        "pre-chorus": Fore.WHITE,
        "chorus": Fore.MAGENTA + Style.BRIGHT,
        "post-chorus": Fore.MAGENTA,
        "interlude": Fore.BLUE,
        "bridge": Fore.GREEN,
        "": Fore.WHITE
    }

    print(Fore.YELLOW + "🎶 Memutar lagu: Where We Are - One Direction 🎶" + Style.RESET_ALL)
    print(Fore.WHITE + f"Jeda per baris: {pause_time} detik. Tekan Ctrl+C untuk menghentikan..." + Style.RESET_ALL)
    print("\n")

    try:
        for section, line in lyrics:
            clear_terminal()
            print(Fore.YELLOW + "🎶 Where We Are - One Direction 🎶\n" + Style.RESET_ALL)
            print(color_map[section] + line + Style.RESET_ALL)
            time.sleep(pause_time)  
    except KeyboardInterrupt:
        clear_terminal()
        print(Fore.YELLOW + "🎵 Lagu dihentikan. Terima kasih telah mendengarkan! 🎵" + Style.RESET_ALL)

def get_pause_time():
    while True:
        try:
            pause = float(input(Fore.WHITE + "Masukkan waktu jeda per baris (detik, misalnya 2.0): " + Style.RESET_ALL))
            if pause <= 0:
                print(Fore.RED + "Waktu jeda harus lebih dari 0!" + Style.RESET_ALL)
            else:
                return pause
        except ValueError:
            print(Fore.RED + "Masukkan angka yang valid (misalnya 2.0)!" + Style.RESET_ALL)

if __name__ == "__main__":
    clear_terminal()
    pause_time = get_pause_time()
    display_lyrics(pause_time)
