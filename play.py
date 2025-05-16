import time
import os
from colorama import init, Fore, Style

# Inisialisasi colorama
init()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_lyrics():
    
    lyrics = [
        ("title", "🎵 Where We Are - One Direction 🎵", 0.00),
        ("", "", 2.00),
        ("verse", "Remember when we would stay out too late", 4.00),
        ("verse", "We were young, havin' fun, made mistakes", 6.50),
        ("verse", "Did we ever know? Did we ever know?", 9.00),
        ("verse", "Did we ever know? Yeah", 11.50),
        ("verse", "All the things we'd just think up and say", 14.00),
        ("verse", "Never wrong, always right, not afraid", 16.50),
        ("verse", "Did we ever know? Did we ever know?", 19.00),
        ("verse", "Did we ever know?", 21.50),
        ("", "", 23.50),
        ("pre-chorus", "Is it all inside of my head?", 24.50),
        ("pre-chorus", "Maybe you still think I don't care", 27.00),
        ("pre-chorus", "But all I need is you", 29.50),
        ("pre-chorus", "Yeah, you know it's true, yeah, you know it's true", 32.00),
        ("", "", 34.50),
        ("chorus", "Forget about where we are and let go", 35.50),
        ("chorus", "We're so close", 38.00),
        ("chorus", "If you don't know where to start, just hold on", 40.00),
        ("chorus", "And don't run, no", 42.50),
        ("chorus", "We're looking back, we messed around", 45.00),
        ("chorus", "But that was then and this is now", 47.50),
        ("chorus", "All we need's enough love to hold us", 50.00),
        ("chorus", "Where we are", 52.50),
        ("post-chorus", "But that was then and this is now", 55.00),
        ("post-chorus", "All we need is enough love to hold us", 57.50),
        ("post-chorus", "Where we are", 60.00),
        ("", "", 62.50),
        ("verse", "Summer days rushin' by you and me", 63.50),
        ("verse", "Makes it harder to see underneath", 66.00),
        ("verse", "Did we ever know? Did we ever know?", 68.50),
        ("verse", "Did we ever know?", 71.00),
        ("", "", 73.00),
        ("pre-chorus", "Is it all inside of my head?", 74.00),
        ("pre-chorus", "Maybe you still think I don't care", 76.50),
        ("pre-chorus", "But all I need is you", 79.00),
        ("pre-chorus", "Yeah, you know it's true, yeah, you know it's true", 81.50),
        ("", "", 84.00),
        ("chorus", "Forget about where we are and let go", 85.00),
        ("chorus", "We're so close", 87.50),
        ("chorus", "If you don't know where to start, just hold on", 89.50),
        ("chorus", "And don't run, no", 92.00),
        ("chorus", "We're looking back, we messed around", 94.50),
        ("chorus", "But that was then and this is now", 97.00),
        ("chorus", "All we need's enough love to hold us", 99.50),
        ("chorus", "Where we are", 102.00),
        ("", "", 104.50),
        ("interlude", "Where we are, where we are", 105.50),
        ("interlude", "Where we are, where we are", 108.00),
        ("", "", 110.50),
        ("bridge", "With closed eyes and open mind", 111.50),
        ("bridge", "We can be there, we can be there", 114.00),
        ("bridge", "But this time, let's cross the line", 116.50),
        ("bridge", "Can you see it? Can you see it?", 119.00),
        ("", "", 121.50),
        ("chorus", "Forget about where we are and let go", 122.50),
        ("chorus", "We're so close (If you don't know)", 125.00),
        ("chorus", "If you don't know where to start, just hold on", 127.00),
        ("chorus", "And don't run, no (And don't run, no)", 129.50),
        ("chorus", "We're looking back, we messed around", 132.00),
        ("chorus", "But that was then and this is now", 134.50),
        ("chorus", "All we need's enough love to hold us", 137.00),
        ("chorus", "Where we are", 139.50),
    ]

    # Warna untuk setiap bagian (tanpa menampilkan label bagian)
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

    print(Fore.YELLOW + "🎶 Simulasi Where We Are - One Direction (Durasi 3:31) 🎶" + Style.RESET_ALL)
    print(Fore.WHITE + "Lirik akan ditampilkan sesuai irama lagu. Tekan Ctrl+C untuk menghentikan..." + Style.RESET_ALL)
    print(Fore.WHITE + "Catatan: Sesuaikan timestamp di script jika tempo belum pas!" + Style.RESET_ALL)
    print("\n")

    try:
        for i, (section, line, timestamp) in enumerate(lyrics):
            # Hitung delay berdasarkan selisih timestamp
            if i == 0:
                delay = timestamp
            else:
                delay = timestamp - lyrics[i-1][2]
            time.sleep(delay)  # Delay sesuai irama
            clear_terminal()
            print(Fore.YELLOW + "🎶 Where We Are - One Direction 🎶\n" + Style.RESET_ALL)
            print(color_map[section] + line + Style.RESET_ALL)
    except KeyboardInterrupt:
        clear_terminal()
        print(Fore.YELLOW + "🎵 Simulasi dihentikan. Terima kasih telah mencoba! 🎵" + Style.RESET_ALL)

if __name__ == "__main__":
    display_lyrics()
