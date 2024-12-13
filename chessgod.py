import os
import shutil

def extract_stockfish_binary():
    stockfish_asset_path = '/assets/stockfish/stockfish'  # Path in assets (adjust based on actual project)
    extracted_stockfish_path = '/storage/emulated/0/stockfish/stockfish'  # Writeable location on Android

    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(extracted_stockfish_path), exist_ok=True)

    # Attempt to copy Stockfish binary to the writeable directory
    try:
        # Here, replace this with your own method of accessing the asset if it's in the APK
        # For example, you could copy it manually before running the app
        shutil.copy(stockfish_asset_path, extracted_stockfish_path)
        print(f"Stockfish binary copied to {extracted_stockfish_path}")

        # Make the Stockfish binary executable
        os.chmod(extracted_stockfish_path, 0o755)
        return extracted_stockfish_path

    except Exception as e:
        print(f"Error copying Stockfish binary: {e}")
        return None