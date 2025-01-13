from google_play_scraper import reviews, Sort
import pandas as pd

# Tentukan ID aplikasi yang ingin diambil ulasannya
app_id = 'com.whatsapp'

# Ambil ulasan menggunakan google-play-scraper
def scrape_playstore_reviews(app_id, num_reviews=10000, lang='id', country='ID'):
    # Menyimpan semua ulasan dalam list
    reviews_data = []
    
    # Ambil ulasan aplikasi
    result, _ = reviews(
        app_id,
        lang=lang,  # Bahasa Indonesia
        country=country,  # Lokasi Indonesia
        count=num_reviews,  # Jumlah ulasan yang ingin diambil
        sort=Sort.RATING  # Urutan berdasarkan rating tertinggi (gunakan enum Sort)
    )

    # Menyimpan data ulasan ke dalam list
    for review in result:
        reviews_data.append({
            'review': review['content'],  # Teks ulasan
            'rating': review['score'],    # Rating (1-5)
            'date': review['at'],        # Waktu ulasan ditulis
            'user_name': review['userName'],  # Nama pengguna yang menulis ulasan
        })
    
    # Mengonversi data ulasan ke dalam DataFrame pandas
    df = pd.DataFrame(reviews_data)
    return df

# Menyimpan hasil scraping ke dalam file CSV
if __name__ == "__main__":
    # Tentukan jumlah ulasan yang ingin diambil
    num_reviews = 10000
    
    # Mengambil ulasan dari aplikasi yang diinginkan (WhatsApp)
    df_reviews = scrape_playstore_reviews('com.whatsapp', num_reviews=num_reviews)

    # Menyimpan hasil ulasan dalam format CSV
    df_reviews.to_csv('../Data/playstore_reviews_indonesia.csv', index=False)
    print(f"{len(df_reviews)} reviews scraped and saved to Data/playstore_reviews_indonesia.csv")
