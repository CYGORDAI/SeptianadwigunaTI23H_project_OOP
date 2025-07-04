# main.py
from db_connector import connect_to_db
from models.scrim_models import ScrimMatch, GameResult
from datetime import datetime

def schedule_scrim():
    print("\n--- Buat Jadwal Scrim Baru ---")
    opponent = input("Nama Squad Lawan: ")
    date_str = input("Tanggal Scrim (YYYY-MM-DD): ")
    time_str = input("Jam Scrim (HH:MM): ")
    match_format = input("Format Pertandingan (misal: Best of 3): ")

    try:
        scrim_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        new_scrim = ScrimMatch(opponent, scrim_datetime, match_format)
        
        conn = connect_to_db()
        if conn:
            new_scrim.save(conn)
            conn.close()
            print("\nJadwal scrim baru berhasil dibuat!")
        else:
            print("Gagal terhubung ke database.")
    except ValueError:
        print("Format tanggal atau waktu salah. Harap gunakan format yang benar.")

def update_scrim_result():
    conn = connect_to_db()
    if not conn:
        print("Gagal terhubung ke database.")
        return

    scrims = ScrimMatch.get_all(conn)
    
    print("\n--- Update Hasil Scrim ---")
    scheduled_scrims = [s for s in scrims if s.status == 'Scheduled']
    if not scheduled_scrims:
        print("Tidak ada scrim yang dijadwalkan untuk diupdate.")
        conn.close()
        return

    for s in scheduled_scrims:
        print(f"ID: {s.id} | Lawan: {s.opponent_squad} ({s.scrim_datetime.strftime('%Y-%m-%d')})")
    
    try:
        scrim_id = int(input("Pilih ID Scrim yang telah selesai: "))
        selected_scrim = next((s for s in scheduled_scrims if s.id == scrim_id), None)

        if not selected_scrim:
            print("ID tidak ditemukan.")
            return

        # Update hasil per game
        num_games = 3 if "3" in selected_scrim.match_format else 5
        for i in range(num_games):
            outcome = input(f"Hasil Game {i+1} (Win/Loss): ").capitalize()
            notes = input(f"Catatan singkat Game {i+1} (misal: 'draft bagus', 'kalah laning'): ")
            result = GameResult(game_number=i+1, outcome=outcome, notes=notes)
            selected_scrim.add_game_result(result)
            if 'Win' in [r.outcome for r in selected_scrim.results].count('Win') >= (num_games // 2 + 1) or \
               'Loss' in [r.outcome for r in selected_scrim.results].count('Loss') >= (num_games // 2 + 1):
                break # Berhenti jika sudah ada pemenang

        selected_scrim.final_score = input("Skor akhir (misal: 2-1): ")
        selected_scrim.notes = input("Catatan analisis keseluruhan scrim: ")
        selected_scrim.status = "Finished"
        
        selected_scrim.save(conn)
        print("Hasil scrim berhasil diupdate!")

    except (ValueError, IndexError):
        print("Input tidak valid.")
    finally:
        conn.close()

def view_history():
    print("\n--- Riwayat & Jadwal Scrim ---")
    conn = connect_to_db()
    if not conn:
        print("Gagal terhubung ke database.")
        return
        
    scrims = ScrimMatch.get_all(conn)
    conn.close()

    if not scrims:
        print("Belum ada jadwal scrim sama sekali.")
        return
    
    # Polymorphism in action!
    for scrim in scrims:
        scrim.display_summary()

def main_menu():
    while True:
        print("\n===== MLBB Scrim Tracker =====")
        print("1. Buat Jadwal Scrim Baru")
        print("2. Update Hasil Scrim Selesai")
        print("3. Lihat Semua Jadwal & Riwayat")
        print("4. Keluar")
        choice = input("Pilihanmu: ")

        if choice == '1':
            schedule_scrim()
        elif choice == '2':
            update_scrim_result()
        elif choice == '3':
            view_history()
        elif choice == '4':
            print("Good game, well played!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_menu()