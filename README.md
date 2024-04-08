# SEOMaker

SEOMaker to narzędzie stworzone w celu generowania treści SEO w pliku txt z plików docx.

## Funkcje
- **Interfejs użytkownika (GUI) oparty na Tkinter**: Umożliwia łatwą i szybką interakcję z programem.
- **Generowanie treści HTML**: Automatycznie tworzy kod HTML na podstawie wprowadzonego tekstu, ułatwiając proces przygotowywania atrakcyjnej karty produktu.
- **Automatyczne generowanie nazw obrazów**: Tworzy SEO-friendly nazwy plików graficznych, eliminując polskie znaki i zastępując skomplikowane symbole.
- **Edycja i parafrazowanie treści**: Zawiera narzędzie do ekstrakcji treści z gotowych fragmentów HTML, ułatwiając tworzenie unikalnych opisów produktów i artykułów.
- **Kopiowanie do schowka**: Umożliwia szybkie kopiowanie wygenerowanych treści HTML oraz nazw obrazów do schowka, co przyspiesza proces pracy i ułatwia przygotowywanie plików do wrzucenia na serwer.

## Co robi za nas SEOMaker?
- Uzupełnia wszystkie nagłówki oraz treść.
- Wypełnia nazwy grafik w formacie "przykladowa-nazwa-produktu-n" gdzie n to kolejna cyfra od 1 do n (n = liczba nagłówków).
- Wypełnia sekcje alt="nagłówek" przy piktogramach.
- Wypełnia sekcje alt="" przy grafikach wklejając nazwę produktu.
- Tworzy dla nas gotową do skopiowania nazwę grafik, wystarczy ją wkleić do zdjęć i ponumerować.
- Dodaje prompt przy kopiowaniu paragrafów przeznaczonych do parafrazy w modelu językowym.
- Ubiera za nas sparafrazowane treści z powrotem w odpowiedni html.

## Czego nie robi SEOMaker?
- Brak uzupełnienia piktogramów.
- Brak kontekstu/opisu grafiki w sekcjach alt="".
