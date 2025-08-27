# Zuerst importieren wir die benötigten Werkzeuge aus unserer 'transformers'-Bibliothek
from transformers import pipeline
import time

print("--- FINALES PROGRAMM: SMARTE TO-DO-LISTE MIT TINYLLAMA (Final Version) ---")
print("Lade das 'TinyLLama' Modell. Dies kann einen Moment dauern...")

# Wir verwenden das 'TinyLlama' Modell, da es als einziges korrekte Ergebnisse liefert.
generator = pipeline('text-generation', model='TinyLlama/TinyLlama-1.1B-Chat-v1.0')

print("Modell geladen. Generiere jetzt die Antwort...")

# Der unstrukturierte Satz, den wir aufräumen wollen
messy_sentence = "Ich darf nicht vergessen, morgen den Müll rauszubringen und den Hund zu füttern, und dann muss ich noch die Hausaufgaben für die Schule machen."

# Der einfache und zuverlässige Prompt, der nachweislich funktioniert
prompt = f"Erstelle aus dem folgenden Satz eine einfache To-Do-Liste mit Aufzählungszeichen:\n\n'{messy_sentence}'\n\nHier ist die To-Do-Liste:\n-"

# --- START DER ZEITMESSUNG ---
start_time = time.time()

# Wir geben dem Modell genug Platz für die Antwort
results = generator(prompt, max_length=200)

# --- ENDE DER ZEITMESSUNG ---
end_time = time.time()
duration = end_time - start_time


# --- SAUBERE AUSGABE ---
print("\n--- ANTWORT DES KI-MODELLS (TinyLlama) ---")
full_answer = results[0]['generated_text']
try:
    # Schritt 1: Wir extrahieren den Teil nach unserer Anweisung
    todo_list_full = full_answer.split("Hier ist die To-Do-Liste:\n-")[1]

    # Schritt 2: Wir entfernen den zusätzlichen Text, den das Modell generiert hat.
    clean_list = todo_list_full.split("\n\n")[0]

    print("-" + clean_list)

except IndexError:
    print("Could not parse the output cleanly. Raw output:")
    print(full_answer)

# Wir geben aus, wie lange es gedauert hat, um die Langsamkeit zu dokumentieren
print(f"\nGenerierung dauerte: {duration:.2f} Sekunden")